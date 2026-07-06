# 150 Claude Skills Roadmap

This document defines a prioritized skill backlog for Claude as an engineering operator across WayPoint, Brigara OS / opsflow, Carrot & Daikon Ordering System, Memora, Evanna-AI, and SaaS-Founder-Coaching.

The emphasis is intentionally weighted toward:

1. Software architecture and engineering best practices
2. Software development lifecycle for the AI era
3. QA, testing, validation, and harness engineering
4. SaaS platform architecture and engineering
5. SaaS platform security engineering and design, especially RLS and tenant isolation
6. AI software engineering and design
7. Project-specific domain execution

This is not a random prompt library. It is a structured engineering capability map for turning Claude into a safer, more disciplined software architecture, implementation, validation, and review partner.

## Priority legend

| Priority | Meaning |
|---|---|
| P0 | Foundational. Claude should use this constantly before or during engineering work. |
| P1 | High-value. Claude should use this for most meaningful implementation, review, or architecture work. |
| P2 | Specialized. Claude should use this when the project/domain calls for it. |

## Skill backlog

| # | Skill | Classification | Priority | Usage |
|---:|---|---|---|---|
| 1 | Architecture Decision Record Authoring | Software Architecture & Engineering | P0 | Creates ADRs that capture context, decision, alternatives, consequences, rollback, and operational impact. |
| 2 | System Context Mapping | Software Architecture & Engineering | P0 | Maps actors, systems, trust boundaries, data flows, integrations, and ownership before design or implementation. |
| 3 | Module Boundary Design | Software Architecture & Engineering | P0 | Defines clear module ownership, public APIs, internal helpers, allowed dependencies, and prohibited coupling. |
| 4 | Layered Architecture Enforcement | Software Architecture & Engineering | P0 | Keeps UI, domain, application services, platform services, data access, and infrastructure concerns separated. |
| 5 | Modular Monolith Design | Software Architecture & Engineering | P0 | Designs SaaS systems as modular monoliths before prematurely splitting into microservices. |
| 6 | Domain Model Discovery | Software Architecture & Engineering | P0 | Extracts entities, workflows, invariants, lifecycle states, and business rules from code and docs. |
| 7 | Bounded Context Identification | Software Architecture & Engineering | P0 | Separates domains such as projects, tasks, billing, notifications, imports, inventory, and AI into bounded contexts. |
| 8 | API Contract Design | Software Architecture & Engineering | P0 | Defines request/response schemas, validation, error shapes, idempotency, versioning, and compatibility requirements. |
| 9 | Backward-Compatible Change Design | Software Architecture & Engineering | P0 | Prefers additive changes, compatibility shims, safe migrations, and staged rollout instead of breaking changes. |
| 10 | Refactor Safety Planning | Software Architecture & Engineering | P0 | Requires behavior inventory, tests, rollback plan, risk boundaries, and no opportunistic scope expansion. |
| 11 | Dependency Direction Guard | Software Architecture & Engineering | P0 | Detects architecture violations where feature modules import platform internals or infrastructure leaks upward. |
| 12 | Interface-First Engineering | Software Architecture & Engineering | P0 | Designs interfaces, command shapes, adapters, and contracts before changing implementation internals. |
| 13 | State Machine Modeling | Software Architecture & Engineering | P1 | Models workflows with explicit states, legal transitions, terminal states, retries, and invalid transition handling. |
| 14 | Event-Driven Workflow Design | Software Architecture & Engineering | P1 | Uses events for asynchronous reactions while keeping command execution deterministic and auditable. |
| 15 | Idempotency-First Design | Software Architecture & Engineering | P0 | Prevents duplicate side effects from retries, double-clicks, network failures, and automation replays. |
| 16 | Consistency Boundary Design | Software Architecture & Engineering | P1 | Decides where strong consistency is required and where eventual consistency, queues, or repair jobs are acceptable. |
| 17 | Data Ownership Modeling | Software Architecture & Engineering | P0 | Defines which module owns each table, record type, mutation path, and read model. |
| 18 | Error Taxonomy Design | Software Architecture & Engineering | P1 | Creates safe, consistent errors for validation, auth, authorization, conflicts, dependency failure, and unknown failure. |
| 19 | Observability-by-Design | Software Architecture & Engineering | P0 | Adds correlation IDs, structured logs, audit trails, metrics, traces, and diagnostic context from the beginning. |
| 20 | Operational Runbook Authoring | Software Architecture & Engineering | P1 | Documents how to deploy, verify, rollback, recover, rotate secrets, inspect logs, and troubleshoot failures. |
| 21 | Performance Budget Design | Software Architecture & Engineering | P1 | Sets budgets for page load, query count, payload size, edge function time, AI latency, and background job cost. |
| 22 | Scalability Constraint Mapping | Software Architecture & Engineering | P1 | Identifies scaling bottlenecks in database, RLS policies, queues, cron, browser automation, storage, and AI calls. |
| 23 | Integration Boundary Design | Software Architecture & Engineering | P1 | Wraps external APIs behind adapters with retries, rate limits, timeouts, auth, and deterministic test doubles. |
| 24 | Migration Architecture Planning | Software Architecture & Engineering | P0 | Plans schema/data migrations with prechecks, backups, phased rollout, verification, and rollback notes. |
| 25 | Architecture Drift Review | Software Architecture & Engineering | P0 | Compares current code to documented architecture and flags drift, stale docs, risky shortcuts, and hidden coupling. |
| 26 | AI-Era SDLC Operating Model | AI-Era SDLC | P0 | Defines how humans, Claude, Codex, Lovable, and other agents plan, implement, test, review, and close work. |
| 27 | Agent Startup Context Gate | AI-Era SDLC | P0 | Forces Claude to read required docs, project memory, status, architecture, security, and tests before work. |
| 28 | Phase-Locked Execution | AI-Era SDLC | P0 | Prevents Claude from jumping ahead, adding bonus scope, or implementing outside the approved phase. |
| 29 | Change Classification Gate | AI-Era SDLC | P0 | Classifies changes before work as UI, frontend logic, schema, RLS, backend, AI, integration, billing, refactor, bug fix, or docs. |
| 30 | Human Approval Boundary | AI-Era SDLC | P0 | Stops when work requires explicit approval for schema, RLS, production data, deployments, package changes, or unclear security. |
| 31 | AI Task Decomposition | AI-Era SDLC | P0 | Breaks broad requests into small, reviewable units with acceptance criteria, risks, tests, and deliverables. |
| 32 | Prompt-to-Implementation Traceability | AI-Era SDLC | P1 | Connects user prompt, phase plan, touched files, tests, PR, and closeout evidence into a traceable chain. |
| 33 | Agent Work Authorization Matrix | AI-Era SDLC | P1 | Defines what Claude may plan, edit, test, commit, deploy, or merge without additional approval. |
| 34 | Source-of-Truth Reconciliation | AI-Era SDLC | P0 | Resolves conflicts between chat memory, repo docs, code, PR history, current requirements, and user direction. |
| 35 | AI Pair-Programming Checklist | AI-Era SDLC | P1 | Guides Claude through inspect, plan, implement, validate, summarize, and handoff without skipping engineering discipline. |
| 36 | Reviewable Diff Discipline | AI-Era SDLC | P0 | Keeps changes small, intentional, isolated, and understandable for human review. |
| 37 | No-Silent-Assumptions Protocol | AI-Era SDLC | P0 | Requires Claude to state assumptions, ask when ambiguity changes outcome, and stop when security or data behavior is unclear. |
| 38 | Agent-Safe Git Workflow | AI-Era SDLC | P0 | Uses branch, status, diff, exact staging, commit messages, PR summaries, and clean working tree discipline. |
| 39 | Pull Request Authoring | AI-Era SDLC | P1 | Writes PRs with phase, classification, summary, changed files, validation, screenshots when relevant, risks, and rollback. |
| 40 | PR Comment Triage | AI-Era SDLC | P1 | Classifies review comments as blocker, valid improvement, misunderstanding, out of scope, or follow-up. |
| 41 | AI Closeout Report | AI-Era SDLC | P0 | Produces final status with what changed, what did not change, tests run, known risks, and next action. |
| 42 | Agent Instruction Consolidation | AI-Era SDLC | P0 | Keeps Claude, Codex, Copilot, Cursor, Gemini, and Boost OS instructions aligned and non-conflicting. |
| 43 | AI Work Evidence Pack | AI-Era SDLC | P1 | Collects command outputs, test logs, GitHub Actions results, screenshots, migration proofs, and smoke-test evidence. |
| 44 | Agent Failure Recovery | AI-Era SDLC | P1 | Recovers from failed tests, broken branches, interrupted runs, partial commits, stale generated files, and blocked permissions. |
| 45 | AI SDLC Governance Review | AI-Era SDLC | P1 | Audits whether an AI-assisted change followed planning, approval, testing, security, documentation, and closeout controls. |
| 46 | Test Strategy Authoring | QA / Testing / Validation | P0 | Defines unit, integration, RLS, E2E, regression, AI-router, smoke, and production monitoring coverage for a change. |
| 47 | Risk-Based Validation Matrix | QA / Testing / Validation | P0 | Selects docs-only, fast, full, backup-gated, or deployment-gated validation based on changed files and risk. |
| 48 | Unit Test Harness Design | QA / Testing / Validation | P1 | Builds isolated tests for validators, reducers, pure functions, state machines, mappers, and UI logic. |
| 49 | Integration Test Harness Design | QA / Testing / Validation | P0 | Tests module behavior through realistic service, command, database, auth, and permission boundaries. |
| 50 | RLS Test Harness Design | QA / Testing / Validation | P0 | Proves same-tenant access succeeds, cross-tenant access fails, unauthorized writes fail, and service-role boundaries hold. |
| 51 | E2E Test Design | QA / Testing / Validation | P1 | Tests critical user journeys through Playwright or equivalent browser automation with stable selectors and deterministic data. |
| 52 | Production-Safe E2E Split | QA / Testing / Validation | P0 | Separates fixture/dev-only E2E routes from production-safe smoke tests so internal fixtures never hit production. |
| 53 | Regression-First Bug Fixing | QA / Testing / Validation | P0 | Reproduces a bug with a failing test before fixing it, then preserves the regression test. |
| 54 | Contract Test Design | QA / Testing / Validation | P1 | Validates API, command, edge function, integration, and provider contracts without relying only on UI tests. |
| 55 | Snapshot Test Governance | QA / Testing / Validation | P2 | Uses visual or structural snapshots only when stable and meaningful, with clear update rules. |
| 56 | Search Parameter Test Harness | QA / Testing / Validation | P1 | Tests URL-driven filters, tabs, dialogs, pagination, and deep links across route pages. |
| 57 | Test Data Isolation | QA / Testing / Validation | P0 | Ensures tests create isolated data, use test tenants, clean up safely, and never pollute demo or production tenants. |
| 58 | Seed Fixture Design | QA / Testing / Validation | P1 | Creates deterministic fixtures for roles, tenants, locations, users, tasks, imports, vendors, and billing cases. |
| 59 | Mock and Fake Strategy | QA / Testing / Validation | P1 | Chooses between mocks, fakes, adapters, fixtures, live staging, and contract tests based on risk. |
| 60 | CI Shard Design | QA / Testing / Validation | P1 | Splits large suites into reliable shards with run IDs, isolated resources, deterministic ordering, and useful artifacts. |
| 61 | CI Gate Failure Classifier | QA / Testing / Validation | P0 | Distinguishes product failure, test failure, infra flake, timeout-only interruption, missing secret, and skipped runtime. |
| 62 | Hidden Runtime Marker Detection | QA / Testing / Validation | P0 | Scans logs for silent runtime errors, unhandled rejections, console errors, auth failures, and skipped validations. |
| 63 | Local Pre-Push Validation | QA / Testing / Validation | P0 | Runs the right local tests, typecheck, build, guard scripts, and pre-push validation before pushing. |
| 64 | GitHub Actions Monitoring | QA / Testing / Validation | P0 | Watches exact workflow runs, avoids blind timers, reports failed jobs, and verifies required checks before merge. |
| 65 | Docs-Only Validation | QA / Testing / Validation | P0 | Confirms doc-only changes run lightweight checks and do not waste full validation cycles. |
| 66 | Backup-Gated Validation | QA / Testing / Validation | P0 | Requires verified backups, migration proof, remote smoke checks, and rollback notes for schema/RLS/storage changes. |
| 67 | Performance Regression Testing | QA / Testing / Validation | P1 | Detects query count, payload size, render cost, edge function latency, and AI latency regressions. |
| 68 | Accessibility Test Review | QA / Testing / Validation | P1 | Checks keyboard flow, labels, contrast, focus states, screen reader hints, and dialog behavior. |
| 69 | Security Test Review | QA / Testing / Validation | P0 | Tests auth bypasses, permission escalation, tenant leaks, storage leaks, SQL injection, XSS, and secret exposure. |
| 70 | QA Evidence Closeout | QA / Testing / Validation | P0 | Produces validation evidence with commands, results, skipped tests, reasons, CI links, and remaining risks. |
| 71 | Multi-Tenant SaaS Blueprint | SaaS Platform Architecture | P0 | Defines tenants, memberships, roles, invitations, teams, plans, entitlements, audit, billing, and support surfaces. |
| 72 | Tenant Isolation Architecture | SaaS Platform Architecture | P0 | Makes tenant isolation a database, application, storage, logging, and integration design concern. |
| 73 | RBAC / Permission Model Design | SaaS Platform Architecture | P0 | Designs roles, permissions, role assignments, helper functions, admin overrides, and project/location-specific authority. |
| 74 | Entitlement and Plan Limit Design | SaaS Platform Architecture | P1 | Adds plan-aware limits for users, teams, AI calls, storage, integrations, features, and support levels. |
| 75 | SaaS Command Bus Architecture | SaaS Platform Architecture | P0 | Uses command dispatch for protected writes, auditability, validation, idempotency, and server-derived scope. |
| 76 | SaaS Event Bus Architecture | SaaS Platform Architecture | P1 | Uses events for notifications, digests, imports, integrations, and side effects without hiding behavior in UI code. |
| 77 | SaaS Notification Architecture | SaaS Platform Architecture | P1 | Designs in-app source of truth plus opt-in email, push, SMS, and digest delivery. |
| 78 | SaaS Audit Log Architecture | SaaS Platform Architecture | P0 | Captures actor, tenant, command, resource, correlation ID, before/after context, and security-relevant outcomes. |
| 79 | SaaS Admin Console Design | SaaS Platform Architecture | P1 | Designs super admin, tenant admin, support, audit, costs, user management, and feature flag surfaces. |
| 80 | SaaS Billing Architecture | SaaS Platform Architecture | P1 | Designs subscriptions, invoices, usage, metering, plan upgrades, trials, billing events, and reconciliation. |
| 81 | SaaS Usage Metering | SaaS Platform Architecture | P1 | Tracks AI, storage, events, API calls, imports, users, and feature usage for cost control and product decisions. |
| 82 | Cost Rollup Architecture | SaaS Platform Architecture | P1 | Aggregates cost entries into daily rollups with exact, estimated, allocated, and manual adjustment categories. |
| 83 | Feature Flag Architecture | SaaS Platform Architecture | P1 | Enables tenant/user/role-scoped feature rollout, kill switches, experiments, and staged migrations. |
| 84 | SaaS Onboarding Workflow | SaaS Platform Architecture | P2 | Designs tenant creation, first admin, team setup, invitations, sample data, and first-value experience. |
| 85 | Invitation and Membership Flow | SaaS Platform Architecture | P1 | Handles invited users, accepted users, expired invites, role assignment, tenant membership, and audit. |
| 86 | SaaS Data Retention Design | SaaS Platform Architecture | P1 | Defines retention, soft delete, archive, restore, purge, export, and legal hold behavior. |
| 87 | SaaS Import Pipeline Design | SaaS Platform Architecture | P1 | Handles file upload, inspection, mapping, preview, human review, confirmation, and auditable writes. |
| 88 | SaaS Integration Framework | SaaS Platform Architecture | P1 | Standardizes integration auth, webhook intake, retries, logs, rate limits, error handling, and tenant scoping. |
| 89 | SaaS Background Job Design | SaaS Platform Architecture | P1 | Designs cron, scheduled jobs, worker queues, retries, idempotency, dead letters, and alerting. |
| 90 | SaaS Supportability Design | SaaS Platform Architecture | P1 | Adds support request visibility, correlation lookup, safe admin impersonation alternatives, and tenant-aware diagnostics. |
| 91 | SaaS Data Export Design | SaaS Platform Architecture | P2 | Exports tenant data safely with authorization, redaction, status tracking, and download expiration. |
| 92 | SaaS Search Architecture | SaaS Platform Architecture | P1 | Designs scoped search, permissions-filtered results, indexing, ranking, redaction, and audit of sensitive searches. |
| 93 | SaaS Storage Architecture | SaaS Platform Architecture | P0 | Separates public assets, private files, signed URLs, bucket policies, file ownership, virus scanning, and retention. |
| 94 | SaaS Deployment Architecture | SaaS Platform Architecture | P1 | Defines environments, secrets, migrations, previews, production deployment, rollback, smoke tests, and monitoring. |
| 95 | SaaS Observability Dashboard | SaaS Platform Architecture | P1 | Surfaces health, errors, slow paths, failed jobs, AI cost spikes, integration failures, and tenant-impacting incidents. |
| 96 | RLS Policy Authoring | SaaS Security / RLS | P0 | Writes precise policies for SELECT, INSERT, UPDATE, DELETE with tenant, role, membership, and resource checks. |
| 97 | RLS Deny-by-Default Review | SaaS Security / RLS | P0 | Confirms tables expose nothing unless an explicit, tested policy allows it. |
| 98 | Tenant ID Enforcement | SaaS Security / RLS | P0 | Requires tenant-owned tables to include non-null tenant scope or a documented alternate isolation model. |
| 99 | SECURITY DEFINER Helper Design | SaaS Security / RLS | P0 | Designs safe Postgres helpers with fixed search paths, no recursion, least privilege, and predictable behavior. |
| 100 | RLS Recursion Avoidance | SaaS Security / RLS | P0 | Avoids policies that recursively query the protected table and cause runtime failure or bypass pressure. |
| 101 | Role Source-of-Truth Guard | SaaS Security / RLS | P0 | Keeps roles out of profile records and uses authoritative role assignment tables and helper functions. |
| 102 | Server-Derived Scope Enforcement | SaaS Security / RLS | P0 | Rejects frontend-provided tenant, actor, project, import, or resource hints when they conflict with trusted server data. |
| 103 | Protected Write Path Guard | SaaS Security / RLS | P0 | Ensures sensitive writes happen through server commands or edge functions, not direct client writes. |
| 104 | Sensitive Column Masking | SaaS Security / RLS | P0 | Prevents exposure of phone numbers, credentials, secrets, provider payloads, internal notes, and unrelated member data. |
| 105 | Service Role Containment | SaaS Security / RLS | P0 | Keeps service role usage inside server-only paths and prevents logs, client bundles, or tests from leaking keys. |
| 106 | Storage RLS and Signed URL Security | SaaS Security / RLS | P0 | Validates bucket policies, signed URL expiration, ownership, path redaction, and private file access. |
| 107 | Cross-Tenant Leak Review | SaaS Security / RLS | P0 | Inspects queries, joins, RPCs, edge functions, caches, logs, search results, and notifications for tenant leaks. |
| 108 | Auth Session Security Review | SaaS Security / RLS | P0 | Reviews login, logout, reset password, session refresh, MFA, SSO, and profile fallback behavior. |
| 109 | Admin Authorization Review | SaaS Security / RLS | P0 | Tests super admin, tenant admin, support, approver, manager, staff, and member permissions. |
| 110 | Least Privilege Edge Function Design | SaaS Security / RLS | P0 | Gives each function only the scope, secrets, tables, and actions it needs. |
| 111 | Secret Rotation Runbook | SaaS Security / RLS | P1 | Documents rotation, verification, rollback, impacted services, and outage risks for credentials and API keys. |
| 112 | Encryption Boundary Review | SaaS Security / RLS | P1 | Confirms when AES, vault storage, hashing, or provider-managed encryption is required and how keys are protected. |
| 113 | Security Regression Harness | SaaS Security / RLS | P0 | Creates permanent tests for every fixed auth, RLS, tenant isolation, storage, and sensitive data bug. |
| 114 | Security Impact Note Authoring | SaaS Security / RLS | P0 | Documents security impact before RLS, auth, storage, command-gateway, or sensitive schema changes. |
| 115 | Threat Modeling | SaaS Security / RLS | P1 | Models attackers, trust boundaries, assets, abuse paths, tenant escalation, integration abuse, and AI-specific threats. |
| 116 | Abuse Case Design | SaaS Security / RLS | P1 | Turns threats into abuse cases and negative tests, not just happy-path QA. |
| 117 | Secure Error Response Design | SaaS Security / RLS | P0 | Returns safe errors without leaking whether records, tenants, emails, users, credentials, or private files exist. |
| 118 | Audit-Ready Evidence Design | SaaS Security / RLS | P1 | Produces evidence for compliance: access control, changes, approvals, activity, logs, and verification. |
| 119 | Production Data Safety Gate | SaaS Security / RLS | P0 | Blocks cleanup, backfill, delete, migration, and bootstrap grants without explicit target confirmation and backup evidence. |
| 120 | Security Drift Detection | SaaS Security / RLS | P0 | Compares docs, migrations, policies, tests, and generated types to catch stale or weakened security posture. |
| 121 | AI Router Architecture | AI Software Engineering & Design | P0 | Centralizes provider calls, model routing, secrets, logging, cost controls, entitlement checks, and fallback behavior. |
| 122 | AI Provider Adapter Design | AI Software Engineering & Design | P0 | Wraps OpenAI, Anthropic, Gemini, Lovable AI, or future providers behind stable internal interfaces. |
| 123 | Prompt Contract Design | AI Software Engineering & Design | P0 | Defines system prompt, developer prompt, input schema, output schema, refusal paths, and validation rules. |
| 124 | Structured Output Validation | AI Software Engineering & Design | P0 | Validates AI JSON or tool output with schemas, repairs only safe errors, and rejects unsafe or malformed responses. |
| 125 | AI Advisory-Only Workflow | AI Software Engineering & Design | P0 | Keeps AI suggestions separate from writes until a human reviews and confirms. |
| 126 | AI Human-in-the-Loop Design | AI Software Engineering & Design | P0 | Designs review queues, confidence labels, evidence, approval buttons, edit-before-apply, and audit logs. |
| 127 | AI Cost Guardrail Design | AI Software Engineering & Design | P0 | Applies token caps, model selection, request budgets, tenant quotas, feature budgets, and cost alerting. |
| 128 | AI Usage Telemetry | AI Software Engineering & Design | P1 | Logs safe metadata such as model, feature, latency, tokens, cost estimate, error class, and correlation ID. |
| 129 | AI Redaction Pipeline | AI Software Engineering & Design | P0 | Redacts secrets, credentials, sensitive columns, PII, raw provider payloads, and private tenant data before AI calls. |
| 130 | AI Prompt Injection Defense | AI Software Engineering & Design | P0 | Treats external content as untrusted data and prevents it from changing system rules, tools, or data-access policy. |
| 131 | RAG Retrieval Boundary Design | AI Software Engineering & Design | P1 | Scopes retrieval by tenant, user, role, document permission, retention policy, and citation/evidence rules. |
| 132 | AI Evaluation Harness | AI Software Engineering & Design | P1 | Tests quality, safety, hallucination, schema adherence, refusal, latency, and cost across representative scenarios. |
| 133 | AI Golden Dataset Management | AI Software Engineering & Design | P1 | Maintains curated examples, expected outputs, adversarial cases, and regression baselines for AI features. |
| 134 | AI Regression Testing | AI Software Engineering & Design | P1 | Detects behavior changes after prompt, model, provider, retrieval, or schema updates. |
| 135 | AI Fallback and Degradation | AI Software Engineering & Design | P1 | Defines model fallback, cached responses, manual review fallback, disabled states, and safe user messaging. |
| 136 | AI Rate Limit Handling | AI Software Engineering & Design | P1 | Handles provider rate limits, retries, queueing, exponential backoff, user feedback, and no duplicate side effects. |
| 137 | AI Output Evidence Design | AI Software Engineering & Design | P1 | Shows source summaries, confidence, extracted evidence, trace snippets, and why a recommendation was made. |
| 138 | AI Autonomy Boundary Design | AI Software Engineering & Design | P0 | Defines which actions AI may perform automatically, which require confirmation, and which are never allowed. |
| 139 | AI Safety Review Checklist | AI Software Engineering & Design | P0 | Reviews data leakage, prompt injection, tool misuse, unsafe writes, hallucination, cost blowups, and audit gaps. |
| 140 | AI Feature Kill Switch | AI Software Engineering & Design | P1 | Adds provider, model, tenant, and feature-level disable controls for incidents or runaway costs. |
| 141 | AI Import Candidate Extraction | AI Software Engineering & Design | P1 | Extracts tasks, items, memories, or fields from text/images/spreadsheets into editable candidates rather than direct writes. |
| 142 | AI Summarization Design | AI Software Engineering & Design | P1 | Summarizes meetings, memories, tasks, alerts, and evidence with clear scope, source boundaries, and uncertainty. |
| 143 | AI Planning Assistant Design | AI Software Engineering & Design | P1 | Turns goals into phased plans with dependencies, acceptance criteria, risk, test plan, and human approval gates. |
| 144 | AI Code Review Assistant | AI Software Engineering & Design | P1 | Reviews diffs for architecture drift, security risk, missing tests, hidden coupling, and incomplete validation. |
| 145 | AI Incident Analysis Assistant | AI Software Engineering & Design | P2 | Summarizes logs, failed jobs, alerts, recent deploys, blast radius, likely cause, and next safe actions. |
| 146 | WayPoint Mission Control Workflow | Project / Domain Specialization | P2 | Applies phase-locked project/task/collaboration/notification/import patterns for WayPoint. |
| 147 | Brigara OS Restaurant Ops Workflow | Project / Domain Specialization | P2 | Handles restaurant checklists, scheduling, HR, inventory, finance, audits, sensors, commissary, and notifications. |
| 148 | Carrot & Daikon Ordering Workflow | Project / Domain Specialization | P2 | Handles inventory counts, PAR, supplier thresholds, hub routing, approvals, price snapshots, and vendor cart automation. |
| 149 | Memora Capture and Recall Workflow | Project / Domain Specialization | P2 | Handles personal/work/study spaces, capture, OCR, duplicate detection, smart search, digest, and cost metering. |
| 150 | SaaS Founder Coaching Curriculum Workflow | Project / Domain Specialization | P2 | Builds lessons, quizzes, labs, playbooks, governance topics, and founder-friendly SaaS architecture explanations. |

## Recommended implementation order

Start with the first 25 skills as the engineering foundation, then implement the SDLC and QA skills before adding project/domain-specific skills. The fastest path to better Claude output is not more prompts. It is stronger operating discipline, clearer architecture boundaries, safer security gates, and better validation evidence.

### First 15 to build

1. Agent Startup Context Gate
2. Phase-Locked Execution
3. Change Classification Gate
4. Human Approval Boundary
5. Architecture Decision Record Authoring
6. System Context Mapping
7. Module Boundary Design
8. RLS Policy Authoring
9. RLS Test Harness Design
10. Command Bus Architecture
11. Risk-Based Validation Matrix
12. GitHub Actions Monitoring
13. AI Router Architecture
14. AI Prompt Injection Defense
15. AI Closeout Report

## Documentation notes

- Keep individual skill implementation docs small and executable.
- Each skill should eventually have a `SKILL.md` with purpose, when to use, required inputs, steps, outputs, examples, anti-patterns, and validation checklist.
- Do not store project secrets, private keys, Supabase service role keys, vendor credentials, provider payloads, or customer data in this repository.
- When a skill depends on a specific private repo, document the pattern generically and point to the private repo docs from that repo, not from this public repository.
