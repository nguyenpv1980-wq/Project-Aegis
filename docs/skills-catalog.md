# Skills & Agents Catalog

Single source of truth for what skills and subagents exist, what is planned, and how the two
differ. The backlog below is derived from the **reconciled phase lists**
([`docs/reconciliation/step-0-reconciliation-v4.md`](reconciliation/step-0-reconciliation-v4.md) §3)
and the **category backlogs** under [`docs/skills/`](skills/). `scripts/validate-skills.py`
checks that every *implemented* skill is listed here and in `README.md`.

> **Phase 0 status:** no real skills are implemented yet. The only skill directory is
> `_template` (a reference template, ignored by the validator). Everything under "Backlog"
> is planned, not built.

---

## Skills vs. Agents

| | **Skill** (`.claude/skills/`) | **Subagent** (`.claude/agents/`) |
| --- | --- | --- |
| What it is | A reusable *procedure* — an ordered workflow Claude loads and executes. | A read-only *reviewer persona* spawned to judge a delimited task in its own context. |
| Invocation | Triggers on its `description`, or explicitly by name. | Delegated to via the Agent tool. |
| Tools | Inherits session tools; narrows via `allowed-tools`. | Declares its own tools; **read-only by default** (decision D2). |
| Best for | Repeatable transformations/generation with a defined output + evals. | Focused review/audit passes that benefit from isolation and a specialized lens. |
| Rule of thumb | If it *does* something and produces an artifact → skill. | If it *judges* something and returns findings → agent. |

Agents **compose** skills; they must not duplicate skill bodies. Role → subagent mapping is
in the reconciliation doc §5.

---

## Priority definitions

| Tier | Meaning |
| --- | --- |
| **P0** | Foundation + operating discipline + core engineering/SaaS/security/QA that must exist before the library is trustworthy. Phases 0–5 skew P0. |
| **P1** | High-value packs that build on P0: cloud/DevOps/reliability and AI security (Phases 6–7), plus P1 items inside earlier phases. |
| **P2** | Remaining 300-roadmap breadth, generated in Phase 8 batches of ≤20 after P0/P1 prove the pattern. |

---

## Implemented (Phase 0 — this branch)

### Foundation

| Item | Type | Status |
| --- | --- | --- |
| `docs/skill-generation-standard.md` | standard | ✅ |
| `docs/templates/skill-template.md` | template | ✅ |
| `docs/templates/evals-template.json` | template | ✅ |
| `docs/reconciliation/step-0-reconciliation-v4.md` | reconciliation record | ✅ |
| `docs/skills-catalog.md` | this catalog | ✅ |
| `scripts/validate-skills.py` | validator | ✅ |
| `.claude/skills/_template/` | reference template skill (ignored by validator) | ✅ |

### Subagents (read-only reviewers)

| Subagent | v4 role | Status |
| --- | --- | --- |
| `principal-architecture-reviewer` | Principal Claude Architect | ✅ |
| `secure-saas-reviewer` | SaaS Security & Tenant Isolation | ✅ |
| `qa-automation-lead` | QA Automation & Release Evidence | ✅ |
| `full-codebase-auditor` | Full Codebase Audit | ✅ |
| `senior-troubleshooting-lead` | Senior Troubleshooting | ✅ |
| `ai-security-red-team-reviewer` | AI Security & LLM Systems | ✅ |
| `release-readiness-reviewer` | Release Captain | ✅ |

### Skills

_None implemented yet._ Phase 1 (operating-discipline pack) is next.

---

## Backlog by phase (reconciled)

The v4 phase structure is canonical. Each phase's first-pass skills are listed; see the
reconciliation doc §3 for merge/move notes and the per-phase "expansion backlog."

### Phase 1 — AI operating-discipline pack (P0)
`agent-startup-context-gate`, `source-of-truth-reconciler`, `change-classification-gate`,
`human-approval-boundary`, `reviewable-diff-discipline`, `ai-closeout-reporter`,
`agent-failure-recovery`, `agent-instruction-consolidator`.
Source: [`docs/skills/08-ai-era-sdlc-agent-ops.md`](skills/08-ai-era-sdlc-agent-ops.md).

### Phase 2 — Core architecture & engineering (P0)
`domain-modeler`, `architecture-designer`, `adr-writer`, `docs-first-implementer`,
`tdd-engineer`, `systematic-debugger`, `code-reviewer`, `code-simplifier`,
`principal-code-analyst`, `full-codebase-auditor`.
Source: [`docs/skills/01-software-architecture-engineering.md`](skills/01-software-architecture-engineering.md),
[`04-backend-api-data-engineering.md`](skills/04-backend-api-data-engineering.md).

### Phase 3 — SaaS & tenant isolation (P0/P1)
`saas-platform-architect`, `tenant-modeler`, `tenant-isolation-reviewer`,
`multi-tenant-data-architect`, `authorization-matrix-designer`, `plan-entitlement-architect`,
`audit-log-architect`, `saas-cost-architect`, `api-event-architect`.
Source: [`docs/skills/02-saas-platform-architecture.md`](skills/02-saas-platform-architecture.md).

### Phase 4 — Security, RLS & supply chain (P0/P1)
`threat-modeler`, `appsec-implementer`, `multi-tenant-security-tester`, `rls-policy-auditor`,
`secrets-identity-hardener`, `supply-chain-security-reviewer`, `security-pr-reviewer`,
`secure-migration-reviewer`, `static-analysis-reviewer`.
Source: [`docs/skills/03-saas-security-rls.md`](skills/03-saas-security-rls.md).

### Phase 5 — QA, E2E, manual QA & evidence (P0/P1)
`qa-strategy-architect`, `test-plan-designer`, `test-coverage-mapper`, `qa-automation-architect`,
`playwright-e2e-engineer`, `clickthrough-test-engineer`, `manual-test-case-creator`,
`screenshot-evidence-planner`, `vitest-unit-component-engineer`, `vite-build-qa-engineer`,
`flaky-test-detective`, `test-data-architect`, `regression-suite-curator`.
Source: [`docs/skills/06-qa-test-engineering.md`](skills/06-qa-test-engineering.md),
[`05-frontend-ux-engineering.md`](skills/05-frontend-ux-engineering.md).

### Phase 6 — Cloud, DevOps, reliability & release (P1)
`cloud-architecture-decider`, `azure-saas-architect`, `aws-saas-architect`, `iac-reviewer`,
`ci-pipeline-architect`, `release-readiness-reviewer`, `rollback-runbook-author`,
`observability-operator`, `slo-reliability-architect`, `incident-response-runbook`.
Source: [`docs/skills/07-devops-release-reliability.md`](skills/07-devops-release-reliability.md).

> Note: `release-readiness-reviewer` and `full-codebase-auditor` exist as **subagents**
> (review lens) and are also planned as **skills** (procedure). Different namespaces
> (`.claude/agents/` vs `.claude/skills/`); the agent composes the skill.

### Phase 7 — AI security & LLM systems (P1)
`ai-threat-modeler`, `prompt-injection-defender`, `rag-security-architect`,
`agent-tool-safety-guard`, `llm-output-safety-reviewer`, `ai-evaluation-harness`,
`ai-cost-guardrail-designer`, `ai-governance-risk-reviewer`, `ai-router-architect`,
`structured-output-validator`.
Source: [`docs/skills/09-ai-software-engineering.md`](skills/09-ai-software-engineering.md).

### Phase 8 — Backlog expansion (P2)
Remaining roadmap skills, generated in validated batches of ≤20 (see reconciliation §4.1).

---

## Capability map (300-skill roadmap)

The full backlog lives in [`docs/300-repeatable-software-saas-skills-roadmap.md`](300-repeatable-software-saas-skills-roadmap.md):

| Category | Count | Document |
| --- | ---: | --- |
| Software Architecture & Engineering | 55 | [`01`](skills/01-software-architecture-engineering.md) |
| SaaS Platform Architecture | 35 | [`02`](skills/02-saas-platform-architecture.md) |
| SaaS Security, Multi-Tenancy & RLS | 40 | [`03`](skills/03-saas-security-rls.md) |
| Backend, API & Data Engineering | 30 | [`04`](skills/04-backend-api-data-engineering.md) |
| Frontend & UX Engineering | 20 | [`05`](skills/05-frontend-ux-engineering.md) |
| QA, Test Architecture & Validation | 55 | [`06`](skills/06-qa-test-engineering.md) |
| DevOps, Release & Reliability | 25 | [`07`](skills/07-devops-release-reliability.md) |
| AI-Era SDLC & Agent Operating Discipline | 20 | [`08`](skills/08-ai-era-sdlc-agent-ops.md) |
| AI Software Engineering & LLM Systems | 20 | [`09`](skills/09-ai-software-engineering.md) |
| **Total** | **300** | |

---

## Evals & validation note

Every implemented skill must ship `evals/evals.json` (and `evals/trigger-evals.json` when its
trigger overlaps another skill). **Evals are structurally validated only — there is no runner
yet (decision D3).** Run `python scripts/validate-skills.py` before every commit that touches
`.claude/skills/`.
