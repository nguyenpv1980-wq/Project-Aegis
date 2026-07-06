---
name: skill-name-matches-directory
description: One or two sentences, trigger-oriented and specific. State WHEN to use this skill and WHAT it produces, in words a model can match against a user request. Keep under 1024 characters. Replace this text.
# disable-model-invocation: true   # <-- UNCOMMENT if this skill has ANY side effect
#                                       (writes outside scratch, network, deploy, spend)
# allowed-tools: Read, Grep, Glob  # <-- OPTIONAL and NARROW only. Omit to inherit
#                                       the session default. Never use "*" or broad grants.
---

# Skill Name

> Copy this directory to `.claude/skills/<your-skill-name>/`, rename it, and fill in
> every section. Also create `evals/evals.json` (from `docs/templates/evals-template.json`).
> Delete these blockquote instructions when done. See
> [docs/skill-generation-standard.md](../../../docs/skill-generation-standard.md).
> The nine sections below are all required and validated.

## Purpose

<!-- One paragraph. What does this skill produce, and what value does it deliver? -->

## Use When

<!-- Concrete trigger conditions. Mirror the frontmatter description with nuance. -->

- Use when: …
- Use when: …
- Do NOT use when: …

## Inputs to Inspect

<!-- The repo files, docs, code, tests, and prior artifacts to read BEFORE acting. -->

- …

## Workflow

<!-- The ordered steps the model follows. This is the operational core of the skill. -->

1. …
2. …
3. …

## Output Format

<!-- The exact shape of the deliverable: file path(s), report structure, data schema. -->

## Validation Checklist

<!-- The model runs this before declaring the task done. -->

- [ ] …
- [ ] …

## Gotchas

<!-- Known failure modes, sharp edges, platform quirks. -->

- …

## Stop Conditions

<!-- When to halt and ask the human instead of proceeding. -->

- Stop and ask if: input is ambiguous or missing.
- Stop and ask before: any irreversible or destructive action.

## Supporting Files

<!-- List references/, assets/, scripts/, evals/ this skill relies on, or "None". -->

- `evals/evals.json` — representative trigger + behavior cases.
