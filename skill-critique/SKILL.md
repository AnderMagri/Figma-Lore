---
name: design-critique-lore
description: >
  Structured design critique and expert evaluation. Covers heuristic
  evaluation in depth — all ten Nielsen heuristics with failure modes and
  domain specifics, severity ratings, the protocol, finding and report
  formats, plus Shneiderman, Gerhardt-Powals, WCAG-as-heuristics, and
  heuristic sets for AI, ecommerce, crypto/fintech and accessibility.
  Also per-dimension critique rubrics (observation / problem / fix, rated
  pass / minor / major) for composition, hierarchy, typography, colour,
  spacing, density, affordance, copy, brand, responsive behaviour, state
  completeness, task efficiency, data display and motion; plus critique
  practice — facilitation, feedback language, design rationale, red-teaming
  assumptions, pre-mortems, defending decisions, product framing, reviewing
  AI-generated work, and self-critique. Trigger for design critique,
  heuristic evaluation, usability review, design review, auditing a screen,
  severity ratings, defending a design decision, or requests to evaluate or
  find problems in a design.
---

# Design Critique Lore

How to evaluate an interface rigorously and say something useful about it —
heuristic evaluation, structured critique rubrics, and the practice of
critique as a working discipline.

> **Part of the Design Lore family.** For design theory, Gestalt, and
> behavioural principles use **design-lore**. For Figma prototyping and
> motion use **figma-prototyping-lore**. For layout and page architecture use
> **layout-lore**. For AI product evaluation use **ai-ux-lore**. For Shopify
> and ecommerce specifics use **shopify-lore** and **ecommerce-lore**.

## How to Use This Skill

1. For a full review, run `41 (cr-001)` as the pass order, pulling in the
   relevant dimension entries as you go
2. For a formal evaluation, run `40 (he-013)` as the protocol and
   `40 (he-014)` as the finding format
3. For a specific dimension, go straight to that entry in module 41
4. For the meeting, the write-up, or the argument, use module 42

---

## Module Index

| File | Covers | Key IDs |
|------|--------|---------|
| lore/40-heuristic-evaluation.jsonl | Nielsen's 10 in depth, severity ratings, full protocol, finding and report format, other heuristic sets (Shneiderman, Gerhardt-Powals, Tognazzini, WCAG, HEART), AI / ecommerce / crypto / accessibility heuristics, evaluating a Figma file | he-001 → he-020 |
| lore/41-critique-rubrics.jsonl | The standard critique pass, then per-dimension rubrics: composition, hierarchy, typography, colour, spacing, density, affordance, copy, brand, responsive, states, task efficiency, data display, motion, and turning findings into a plan | cr-001 → cr-016 |
| lore/42-critique-practice.jsonl | Facilitation, feedback language, design rationale, red-teaming assumptions, pre-mortems, defending decisions, product framing and metrics, critiquing AI-generated work, review cadence, self-critique | cx-001 → cx-010 |

---

## Quick Topic Routing

### Evaluation
**"Run a heuristic evaluation"** → 40 (he-013, he-014) + he-002…he-011
**"What severity is this?"** → 40 (he-012)
**"Heuristics for an AI product"** → 40 (he-016)
**"Heuristics for a storefront"** → 40 (he-017)
**"Heuristics for a wallet or exchange"** → 40 (he-018)
**"Accessibility review"** → 40 (he-019)
**"Evaluate this Figma file"** → 40 (he-020)
**"Data-dense dashboard evaluation"** → 40 (he-015, Gerhardt-Powals)

### Critique a screen
**"Critique this design"** → 41 (cr-001) then the dimensions
**"Is the hierarchy right?"** → 41 (cr-003)
**"Is the typography right?"** → 41 (cr-004)
**"Colour and contrast"** → 41 (cr-005)
**"Spacing feels off"** → 41 (cr-006)
**"Too much / too little on screen"** → 41 (cr-007)
**"Does this look clickable?"** → 41 (cr-008)
**"Copy review"** → 41 (cr-009)
**"Will this survive real content?"** → 41 (cr-011, cr-012)
**"Charts and numbers"** → 41 (cr-014)

### Practice
**"Run a critique session"** → 42 (cx-001, cx-002)
**"Write up the decision"** → 42 (cx-003)
**"Stress-test my own thinking"** → 42 (cx-004, cx-005)
**"Stakeholder wants X"** → 42 (cx-006, cx-007)
**"Review AI-generated screens"** → 42 (cx-008)
**"I've been staring at this too long"** → 42 (cx-010)

---

## Key Principles

- **Observation → Problem → Fix.** Separate the checkable fact from the interpretation from the recommendation. Agreement happens on the observation.
- **Ask for the states first.** Critiquing an ideal-state-only design is premature; the missing states ARE the finding.
- **Tie every finding to the screen's purpose or a named principle.** Anything tied to neither is preference — say it, and label it.
- **Severity = frequency × impact × persistence.** Not how much it annoys you, and not how easy it is to fix.
- **3–5 evaluators, working independently.** One evaluator finds about a third of the problems; discussing before finishing destroys the coverage gain.
- **Heuristic violations are hypotheses, not verdicts.** Some are correct trade-offs; the heuristics contradict each other constantly.
- **A fix is a specific change, not a direction.** "Move shipping cost above the payment step", not "improve cost transparency".
- **Attack your own load-bearing assumptions before the review does.**
- **Name what works.** A critique that only lists failures gets discounted.
- **Every finding gets a disposition** — accepted, deferred with a reason, or rejected with a reason.
