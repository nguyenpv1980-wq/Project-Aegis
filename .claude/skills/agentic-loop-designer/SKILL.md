---
name: agentic-loop-designer
description: Design an agentic loop's shape and bounds — single-shot vs agentic as an EXPLICIT up-front decision (never default to a loop); clamped iteration ceilings; TYPED retryability (a policy rejection is TERMINAL, never retried; a transient failure is retried once on IDENTICAL input (reproducibility key) to classify flake vs deterministic); honest terminal states (an empty result is a legitimate stop, never forced into fabricated output); plan-act-observe-reflect with a defined stop. A loop needs an honest way to stop, including the honest empty set. Consumes iteration/cost caps from ai-cost-guardrail-designer (budget is an input; this owns loop SEMANTICS/stopping); designs the structure agent-failure-recovery plugs into; the loop runs INSIDE agent-harness-architect's harness. Use when deciding whether a task needs a loop, designing retry/stop behavior, or when an agent loops unbounded or fabricates on empty. DESIGNS the loop; manipulation attack review belongs to agent-goal-hijack-defender and ai-threat-modeler.
---

# Agentic Loop Designer

## Purpose

A loop needs an honest way to stop, including the honest empty set. This
skill designs the shape and bounds of an agentic loop — or establishes that
no loop is needed. The deliverable is a loop design with five load-bearing
parts: (1) the single-shot-vs-agentic decision made EXPLICITLY up front,
with the reasons recorded — a loop is a cost and a risk you take on purpose,
not a default; (2) clamped iteration ceilings that cannot be exceeded; (3)
TYPED retryability — every failure is classified before any retry: a policy
rejection is TERMINAL and never retried, a transient failure is retried
exactly once on IDENTICAL input so the second outcome classifies it as flake
or deterministic, and a reproducibility key (the hash of the exact input)
keeps that classification honest; (4) honest terminal states — success,
policy-stop, deterministic-failure, ceiling/budget-stop, and the honest
empty set: an empty result is a legitimate stop, never forced into
fabricated output; and (5) a plan → act → observe → reflect structure with
the stop check run every iteration. This skill DESIGNS the loop; the
security review of loop manipulation — hijacked goals, adversarial threat
paths — belongs to `agent-goal-hijack-defender` and `ai-threat-modeler`. It
PRODUCES the artifact those skills review.

## Use When

- Use when: deciding whether a task needs an agentic loop at all — the
  single-shot-vs-agentic call, made before any loop is built.
- Use when: designing or overhauling a loop's structure — iterations,
  retries, stop conditions, terminal states — for an agent that plans and
  acts over multiple steps.
- Use when: an agent loops unbounded, retries policy rejections, re-rolls
  failures with tweaked prompts until something passes, or pads an empty
  result into invented output.
- Use when: retry behavior needs to distinguish flake from deterministic
  failure and nobody can currently tell which is which.
- Auto-invocable: a pure design skill — it produces a loop specification and
  changes no live system.
- Do NOT use when: the job is the ATTACK REVIEW of the loop — can injected
  content redirect the agent's goal or plan — that is
  `agent-goal-hijack-defender`, with `ai-threat-modeler` for the broader
  adversarial threat map. This skill DESIGNS the loop; the security review
  of it belongs to those skills.
- Do NOT use when: the question is the BUDGET — token caps, spend limits,
  loop/recursion cost bounds as policy — that is `ai-cost-guardrail-designer`;
  its caps are an INPUT this design consumes, and this skill owns the loop's
  semantics and stopping, not its price.
- Do NOT use when: a run has already broken the working state (dirty tree,
  interrupted operation, partial commit) — recovery is
  `agent-failure-recovery`; this skill designs the loop structure
  (checkpoints, typed failures, resumable state) that recovery plugs into.
- Do NOT use when: the subject is the operating environment's gating —
  mediation point, pre-flight ladder, registry, instruction custody — that
  is `agent-harness-architect`; the loop this skill designs runs INSIDE that
  harness, and every iteration's calls still pass its ladder.
- Do NOT use when: designing multi-agent containment — cascade isolation,
  drift baselines, kill switches across a fleet — that is
  `agent-containment-reviewer`'s review lane; this skill designs ONE loop's
  internal semantics.

## Inputs to Inspect

1. The task itself: is the output reachable by a fixed pipeline
   (deterministic steps, no observation-dependent branching), or does the
   next step genuinely depend on what the last step observed? This decides
   single-shot vs agentic.
2. The current loop, if one exists: its iteration behavior, what it retries,
   how it stops today, and any history of runaway runs or fabricated
   endings.
3. The failure surface: which step failures are policy rejections, which
   are transient (network, rate limit, timeout), and which are
   deterministic — and whether the code can currently tell them apart.
4. The caps in force (`ai-cost-guardrail-designer` output if present):
   iteration/cost/recursion bounds the loop must respect as inputs.
5. The harness context (`agent-harness-architect` output if present): the
   ladder each iteration's calls pass, and what a mid-loop policy denial
   looks like to the loop.
6. What downstream consumes the terminal state: does the caller distinguish
   "empty result" from "failure" from "gave up at ceiling" — or does
   everything collapse into one shape that invites padding?

## Workflow

1. **Make the single-shot-vs-agentic decision explicitly.** If a fixed
   pipeline reaches the output, design that instead — a summarization, a
   transformation, a lookup does not need a loop. Record the decision and
   its reasons. A loop entered by default is an unbounded liability entered
   silently.
2. **Structure the loop: plan → act → observe → reflect.** Each iteration
   plans the next step, acts, observes the real outcome (not the intended
   one), and reflects against the goal. The stop check runs EVERY iteration
   — not only on success.
3. **Clamp the iterations.** A hard ceiling the loop cannot exceed,
   consuming the bounds `ai-cost-guardrail-designer` prices. Hitting the
   ceiling is a named terminal state that reports honestly ("stopped at
   ceiling with partial result X"), never a silent truncation dressed as
   completion.
4. **Type the retryability.** Classify EVERY failure before any retry:
   - **Policy rejection → TERMINAL.** A denial from the harness ladder, an
     authorization failure, a refused action is never retried — retrying a
     policy stop is an attempt to wear the gate down, and each attempt burns
     budget probing a boundary that will not move.
   - **Transient failure → retry ONCE on IDENTICAL input.** The retry's
     purpose is classification: same input, second outcome. Pass = flake
     (continue); identical failure = deterministic (terminal, surface it).
     A **reproducibility key** — the hash of the exact input — proves the
     input was identical; a "retry" with a tweaked prompt is a NEW attempt
     wearing a retry's clothes, and it destroys the classification.
   - **Deterministic failure → TERMINAL.** Surface it with its evidence;
     do not re-roll hoping for a different answer.
5. **Define the honest terminal states.** Enumerate them: success;
   policy-stop; deterministic-failure; ceiling/budget-stop; and the honest
   EMPTY SET — "nothing matched" is a legitimate, first-class answer. The
   loop never pads, invents, or force-fills an empty result into output
   that looks like success. Downstream must be able to distinguish every
   terminal state.
6. **Design the checkpoint/resume sockets.** Persist enough state per
   iteration that a broken run can be diagnosed and resumed —
   `agent-failure-recovery` handles the recovery; this design gives it
   something to recover.
7. **Prove the stops can fire.** Design the tests: the ceiling actually
   halts a run; a policy rejection is demonstrably not retried; the retry
   classifier is fed a deterministic failure and correctly terminates (and
   a flake, and correctly continues); the empty set reaches the caller as
   empty. A verifier that cannot fail is theater with an exit code — a stop
   condition that has never fired in a test is an unbounded loop you
   haven't met yet.
8. **Deliver the design** in the Output Format, seams cited: budget, the
   harness, recovery, and the attack review — composed, never restated.

## Output Format

```
AGENTIC LOOP DESIGN — <task/agent>
Decision: <single-shot | agentic> — <reasons; what observation-dependence
  justifies the loop, or why a fixed pipeline suffices>
Structure: plan → act → observe → reflect; stop check every iteration
Ceilings: <hard iteration cap; per-iteration and total bounds consumed from
  ai-cost-guardrail-designer>
Retryability (typed):
  policy rejection → TERMINAL, never retried
  transient → retry ONCE on identical input (reproducibility key: <input
    hash>); pass=flake, identical-fail=deterministic
  deterministic → TERMINAL, surfaced with evidence
Terminal states: <success | policy-stop | deterministic-failure |
  ceiling-stop | HONEST EMPTY SET> — each distinguishable downstream;
  empty is never padded into output
Checkpoints/resume: <per-iteration persisted state; what
  agent-failure-recovery can plug into>
Stop proofs: <ceiling-fires test; policy-not-retried test; classifier
  must-fail test (deterministic + flake); empty-reaches-caller test>
Handoffs: budget/caps → ai-cost-guardrail-designer; call gating →
  agent-harness-architect; broken-state recovery → agent-failure-recovery;
  attack review → agent-goal-hijack-defender + ai-threat-modeler
Open questions / risks: <each with risk-if-wrong / who answers>
```

## Validation Checklist

- [ ] The single-shot-vs-agentic decision is explicit and recorded; the
      loop exists because observation-dependence requires it, not by
      default.
- [ ] The loop is plan → act → observe → reflect with the stop check every
      iteration.
- [ ] A hard iteration ceiling exists, consumes the priced caps, and
      hitting it is an honest named terminal state.
- [ ] Every failure is typed before any retry; policy rejections are
      TERMINAL and demonstrably never retried.
- [ ] The transient retry is exactly once, on IDENTICAL input, under a
      reproducibility key — and its outcome classifies flake vs
      deterministic.
- [ ] The terminal states are enumerated and downstream-distinguishable,
      including the honest empty set; nothing pads empty into output.
- [ ] Per-iteration checkpoints give `agent-failure-recovery` a socket.
- [ ] Every stop has a designed proof it can fire — ceiling, policy-stop,
      classifier, and empty-set delivery all have must-fail/must-fire
      tests.
- [ ] The yields are stated: manipulation attack review →
      agent-goal-hijack-defender + ai-threat-modeler; seams cited, not
      restated.

## Gotchas

- "Make it agentic" is a cost decision disguised as an architecture
  decision: a loop buys adaptability with unboundedness, and most
  transformations don't need the purchase. The explicit up-front decision
  is the cheapest control in this skill.
- Retrying a policy rejection is not resilience — it is probing a gate.
  The commonest form: catching ALL exceptions in one handler and retrying,
  which silently converts denials into retry storms.
- A retry with a tweaked prompt classifies nothing: two different inputs
  with two outcomes tells you the inputs differed. Identical input is what
  makes the second run evidence — that is what the reproducibility key is
  for.
- The empty set is where fabrication pressure concentrates: a loop that
  "must return something" will eventually return something false. Empty
  reaching the caller as empty is a feature the design must defend, not a
  UX bug to paper over.
- A ceiling that only lives in a prompt ("stop after 10 tries") is not a
  ceiling — the clamp must be enforced by the code that runs the loop, not
  requested of the model inside it.
- Terminal states that collapse into one shape ("done") invite the padding
  they were meant to prevent: if the caller cannot tell ceiling-stop from
  success, the loop will be pressured to make them look alike.
- A stop condition that has never fired in a test may be unreachable in
  the code path that matters — theater with an exit code. Fire each one
  deliberately before trusting it.

## Stop Conditions

- The request is to force output on the empty set — "never return nothing,
  generate something plausible" → refuse; an empty result is a legitimate
  terminal state, and fabricating past it is the exact failure this design
  exists to prevent. Escalate if the requirement survives.
- The request is to retry policy rejections until they pass → refuse;
  policy stops are terminal by design, and automated gate-probing is not a
  loop feature this skill will design.
- The failure surface cannot be typed — the system cannot distinguish a
  policy denial from a transient error from a deterministic bug → fix the
  error taxonomy first (`error-taxonomy-designer` for the model, the
  harness for denial signaling); typed retryability over untyped failures
  is guesswork.
- No iteration/cost caps exist to consume → obtain them from
  `ai-cost-guardrail-designer` (or a human names the bound); a loop
  designed without a ceiling input is a loop with a default ceiling of
  infinity.
- Wiring the designed loop into a live agent → implementation under the
  repo's approval path; this skill designs, it does not deploy.
- The real concern is goal hijack, adversarial manipulation, or the threat
  map → hand to `agent-goal-hijack-defender` / `ai-threat-modeler` and
  stop.

## Supporting Files

- `evals/evals.json` — behavior cases: the research-loop design, the
  loop-by-default challenge, the retry-typing edge, the fabricate-on-empty
  refusal, and the hijack-review should-not-trigger.
- `evals/trigger-evals.json` — discrimination against
  `ai-cost-guardrail-designer` (budget authoring vs consumption),
  `agent-failure-recovery` (broken-state recovery vs loop structure),
  `agent-harness-architect` (in-batch: call gating vs loop semantics),
  `agent-containment-reviewer` (multi-agent containment review vs one
  loop's design), and the design-vs-review seam against
  `agent-goal-hijack-defender` / `ai-threat-modeler`.
- No `references/` — the loop contract above is the complete procedure;
  detail lives in the produced design artifact.
