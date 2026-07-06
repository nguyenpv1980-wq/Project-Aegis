#!/usr/bin/env python3
"""Validate skills under .claude/skills/ against the repo skill-generation standard.

Checks performed per skill (see docs/skill-generation-standard.md):
  * SKILL.md exists and has a parseable YAML-ish frontmatter block.
  * frontmatter `name` exactly equals the skill's directory name.
  * frontmatter `description` present, non-empty, and < 1024 characters.
  * no BROAD `allowed-tools` grant (e.g. "*", "all", bare "Bash").
  * SKILL.md body is < 500 lines.
  * all nine required sections present (v4 standard): Purpose, Use When,
    Inputs to Inspect, Workflow, Output Format, Validation Checklist, Gotchas,
    Stop Conditions, Supporting Files.
  * evals convention (repo decision D3 — structural only, no runner):
    evals/evals.json exists and parses; evals/trigger-evals.json parses if present.

Repo-level checks:
  * README-catalog integrity: every skill is listed in docs/skills-catalog.md
    AND in README.md.
  * bundled-name collision: no skill name duplicates another skill, and no
    skill name shadows a reserved bundled skill name.

The `_template` directory is ALWAYS ignored (it is a template, not a shipped skill).
When `_template` is the only skill directory, the script prints "no skills found"
and exits 0.

Exit code 0 = clean (possibly with warnings), non-zero = at least one error.
No third-party dependencies.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# --- configuration ---------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
CATALOG = REPO_ROOT / "docs" / "skills-catalog.md"
README = REPO_ROOT / "README.md"

IGNORED_DIRS = {"_template"}
MAX_SKILL_LINES = 500
MAX_DESCRIPTION_CHARS = 1024

REQUIRED_SECTIONS = [
    "Purpose",
    "Use When",
    "Inputs to Inspect",
    "Workflow",
    "Output Format",
    "Validation Checklist",
    "Gotchas",
    "Stop Conditions",
    "Supporting Files",
]

# Names shipped/bundled elsewhere in the Claude ecosystem that a repo skill must
# not shadow, to avoid ambiguous invocation. Extend as needed.
RESERVED_BUNDLED_NAMES = {
    "watch",
    "docx",
    "pdf",
    "pptx",
    "xlsx",
    "schedule",
    "skill-creator",
    "verify",
    "code-review",
    "simplify",
    "loop",
    "run",
    "init",
    "review",
    "security-review",
}

# allowed-tools values that count as "broad" and are rejected.
BROAD_TOOL_TOKENS = {"*", "all", "any", "bash"}


# --- tiny frontmatter parser ----------------------------------------------


def parse_frontmatter(text: str):
    """Return (frontmatter_dict, body_str) or (None, text) if no frontmatter.

    Deliberately minimal: supports `key: value` scalars and simple inline lists
    `key: [a, b]` — enough for skill frontmatter without a YAML dependency.
    """
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None, text
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text
    fm: dict[str, object] = {}
    for raw in lines[1:end]:
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip("\"'") for v in value[1:-1].split(",")]
            fm[key] = [v for v in items if v]
        else:
            fm[key] = value.strip("\"'")
    body = "\n".join(lines[end + 1 :])
    return fm, body


def section_headers(body: str) -> set[str]:
    """Return the set of `##`-level section titles present in the body."""
    out = set()
    for line in body.splitlines():
        m = re.match(r"^##\s+(.*\S)\s*$", line)
        if m:
            out.add(m.group(1).strip())
    return out


# --- validation ------------------------------------------------------------


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def discover_skills() -> list[Path]:
    if not SKILLS_DIR.is_dir():
        return []
    out = []
    for child in sorted(SKILLS_DIR.iterdir()):
        if not child.is_dir():
            continue
        if child.name in IGNORED_DIRS:
            continue
        out.append(child)
    return out


def validate_skill(skill_dir: Path, rep: Report) -> str | None:
    """Validate one skill directory. Returns the skill name (for collision checks)."""
    name_ctx = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        rep.error(f"[{name_ctx}] missing SKILL.md")
        return None

    text = skill_md.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if fm is None:
        rep.error(f"[{name_ctx}] SKILL.md has no parseable frontmatter block")
        return None

    # name matches directory
    fm_name = fm.get("name")
    if not fm_name:
        rep.error(f"[{name_ctx}] frontmatter missing `name`")
    elif fm_name != skill_dir.name:
        rep.error(
            f"[{name_ctx}] frontmatter name '{fm_name}' != directory '{skill_dir.name}'"
        )

    # description
    desc = fm.get("description")
    if not desc or not str(desc).strip():
        rep.error(f"[{name_ctx}] frontmatter missing/empty `description`")
    elif len(str(desc)) >= MAX_DESCRIPTION_CHARS:
        rep.error(
            f"[{name_ctx}] description is {len(str(desc))} chars "
            f"(must be < {MAX_DESCRIPTION_CHARS})"
        )

    # allowed-tools must not be broad
    tools = fm.get("allowed-tools")
    if tools is not None:
        tool_list = tools if isinstance(tools, list) else [tools]
        for t in tool_list:
            if str(t).strip().lower() in BROAD_TOOL_TOKENS:
                rep.error(
                    f"[{name_ctx}] broad allowed-tools grant '{t}' is forbidden; "
                    f"scope it narrowly or omit the field"
                )

    # side-effect skills should disable model invocation (advisory)
    dmi = str(fm.get("disable-model-invocation", "")).lower()
    if dmi not in ("true", "false", ""):
        rep.warn(f"[{name_ctx}] disable-model-invocation should be true/false")

    # line count
    n_lines = len(text.splitlines())
    if n_lines >= MAX_SKILL_LINES:
        rep.error(
            f"[{name_ctx}] SKILL.md is {n_lines} lines (must be < {MAX_SKILL_LINES})"
        )

    # required sections
    present = section_headers(body)
    missing = [s for s in REQUIRED_SECTIONS if s not in present]
    if missing:
        rep.error(f"[{name_ctx}] missing required section(s): {', '.join(missing)}")

    # evals convention (structural only — no runner yet, per decision D3)
    evals_json = skill_dir / "evals" / "evals.json"
    if not evals_json.is_file():
        rep.error(f"[{name_ctx}] missing evals/evals.json")
    else:
        try:
            json.loads(evals_json.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            rep.error(f"[{name_ctx}] evals/evals.json does not parse as JSON: {exc}")

    # trigger-evals.json is optional, but must parse when present
    trigger_json = skill_dir / "evals" / "trigger-evals.json"
    if trigger_json.is_file():
        try:
            json.loads(trigger_json.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            rep.error(
                f"[{name_ctx}] evals/trigger-evals.json does not parse as JSON: {exc}"
            )

    return skill_dir.name


def check_catalog_integrity(skill_names: list[str], rep: Report) -> None:
    catalog_text = CATALOG.read_text(encoding="utf-8") if CATALOG.is_file() else ""
    readme_text = README.read_text(encoding="utf-8") if README.is_file() else ""
    if not CATALOG.is_file():
        rep.error(f"catalog not found at {CATALOG.relative_to(REPO_ROOT)}")
    if not README.is_file():
        rep.error(f"README not found at {README.relative_to(REPO_ROOT)}")
    for name in skill_names:
        if name and name not in catalog_text:
            rep.error(f"[{name}] not listed in docs/skills-catalog.md")
        if name and name not in readme_text:
            rep.error(f"[{name}] not listed in README.md")


def check_name_collisions(skill_names: list[str], rep: Report) -> None:
    seen: set[str] = set()
    for name in skill_names:
        if not name:
            continue
        if name in seen:
            rep.error(f"duplicate skill name '{name}'")
        seen.add(name)
        if name in RESERVED_BUNDLED_NAMES:
            rep.error(
                f"skill name '{name}' collides with a reserved bundled skill name"
            )


def main() -> int:
    rep = Report()
    skills = discover_skills()

    if not skills:
        print("no skills found (only _template present or skills dir empty) - nothing to validate")
        return 0

    print(f"Validating {len(skills)} skill(s) under .claude/skills/ ...\n")

    names: list[str] = []
    for skill_dir in skills:
        name = validate_skill(skill_dir, rep)
        names.append(name or "")

    check_name_collisions(names, rep)
    check_catalog_integrity([n for n in names if n], rep)

    for w in rep.warnings:
        print(f"WARN  {w}")
    for e in rep.errors:
        print(f"ERROR {e}")

    print()
    if rep.errors:
        print(f"FAILED: {len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
        return 1
    print(f"OK: {len(skills)} skill(s) valid, {len(rep.warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
