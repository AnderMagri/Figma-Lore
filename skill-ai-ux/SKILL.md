---
name: ai-ux-lore
description: >
  Designing AI and agentic products. Covers what changes when the system is
  probabilistic, mixed-initiative flow and control handoffs, capability
  discoverability, latency and streaming as designed states, correction loops
  and editability, generative UI, context and memory visibility, frustration
  repair; trust calibration with a stakes-by-confidence language matrix,
  transparency and citation patterns, refusal design, consent and agency,
  harm anticipation, escalation, bias in AI interfaces; persona architecture,
  tone calibration, error personality, behavioural consistency, failure
  taxonomies, quality rubrics and AI metrics; agent roles, task decomposition,
  handoff protocols, human-in-the-loop checkpoints, observability, failure
  recovery, agentic anti-patterns; and prompts as a design surface — system
  prompt structure, constraints, examples, context engineering, versioning.
  Trigger for AI product design, agentic UX, assistant design, AI trust,
  hallucination handling, AI error states, or agent workflows.
---

# AI UX Lore

Designing products where the system is probabilistic, the capability is
invisible, the latency is structural, and the failure states are the product.

> **Part of the Design Lore family.** For AI-specific heuristic evaluation use
> **design-critique-lore** (he-016). For general interaction principles use
> **design-lore**. For crypto and fintech UX use **design-lore-industry**. For
> the Claude API, model IDs, and SDK specifics use the `claude-api` skill —
> this skill covers the design of AI products, not their implementation.

## How to Use This Skill

1. Designing a new AI feature → start at 44 (ax-001), then ax-004, ax-005
2. Something feels untrustworthy → 45 (at-001, at-002)
3. Writing the voice → 46 (ab-001, ab-002, ab-003)
4. Multi-agent or workflow feature → 47
5. Reviewing or improving the system prompt → 48
6. Measuring whether it works → 46 (ab-005, ab-006, ab-007)

---

## Module Index

| File | Covers | Key IDs |
|------|--------|---------|
| lore/44-ai-interaction-design.jsonl | What changes with probabilistic systems, mixed-initiative flow, capability discoverability, latency and streaming, correction loops, generative UI, context visibility, frustration repair | ax-001 → ax-008 |
| lore/45-ai-trust-alignment.jsonl | Trust calibration and its five failure modes, the stakes × confidence language matrix, transparency patterns, guardrails and refusal, consent and agency, harm anticipation, escalation, bias | at-001 → at-008 |
| lore/46-ai-behaviour-evaluation.jsonl | Persona architecture, tone calibration, error personality, behavioural consistency, failure taxonomy, output quality rubrics, AI metrics | ab-001 → ab-007 |
| lore/47-ai-agent-orchestration.jsonl | Agent roles, task decomposition, handoff protocols, human-in-the-loop, state and observability, failure recovery, agentic anti-patterns | ao-001 → ao-007 |
| lore/48-ai-prompt-architecture.jsonl | The prompt as a design surface, system prompt structure, constraint specification, examples and few-shot, context engineering, reasoning structure, prompt versioning | pa-001 → pa-007 |

---

## Quick Topic Routing

**"Design an AI feature"** → 44 (ax-001)
**"Who leads, the user or the AI?"** → 44 (ax-002)
**"Nobody knows what to type"** → 44 (ax-003)
**"It's slow"** → 44 (ax-004)
**"Users have to redo the output"** → 44 (ax-005)
**"Should the AI generate the UI?"** → 44 (ax-006)
**"Memory and context"** → 44 (ax-007) + 48 (pa-005)
**"Users don't trust it / trust it too much"** → 45 (at-001, at-002)
**"Show sources and reasoning"** → 45 (at-003) + 48 (pa-006)
**"Refusals feel bad"** → 45 (at-004)
**"Is this manipulative?"** → 45 (at-005)
**"What could go wrong before launch?"** → 45 (at-006)
**"Write the assistant's voice"** → 46 (ab-001, ab-002)
**"What does it say when it's wrong?"** → 46 (ab-003)
**"Name and count the failures"** → 46 (ab-005)
**"Define and measure quality"** → 46 (ab-006, ab-007)
**"Multi-agent system"** → 47
**"Where do humans approve?"** → 47 (ao-004)
**"Review the system prompt"** → 48 (pa-001, pa-002, pa-003)

---

## Key Principles

- **The first question about any AI feature: what does the user do when it's wrong?** If the answer is "notice and start over", it's a demo.
- **The failure states are the product.** Wrong, slow, refused, partially right, and confidently wrong decide whether the feature succeeds.
- **A text box is a recall test.** Capability discoverability is the largest usability gap in AI products.
- **Trust has two failure directions.** Overtrust and undertrust; neither appears in accuracy metrics.
- **Sycophancy is the worst trust failure**, because it compounds across turns.
- **Prefer "I don't know" to a confident wrong answer.**
- **Editability beats accuracy.** Move the product up the correction ladder before chasing quality.
- **Distinguish cannot / will not / need more info / broke.** Collapsing them destroys the user's ability to adapt.
- **Answer first, explain second, no closing offer of help.** The highest-value output constraints there are.
- **The system prompt is the design.** If you haven't read it, you haven't seen the interface.
- **Separate the producer from the verifier.** An agent checking its own work confirms it.
- **Defer irreversible actions to a commit phase**, so a failed run is a discardable draft.

---

## Attribution

The agentic-experience-design framing, and much of the source material for
mixed-initiative flow, trust calibration, transparency, guardrails, harm
anticipation, persona and error personality, failure taxonomies, agent
orchestration, and prompt architecture is adapted from
[Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills)
(MIT), extended with domain application and additional entries.
