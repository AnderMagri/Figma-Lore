---
name: figma-prototyping-lore
description: >
  Figma prototyping and animation. Covers the interaction model (all triggers
  and actions, flows, hotspots), overlays, scroll and overflow (fixed, sticky,
  preserve scroll position), transitions and Smart Animate matching rules,
  every easing and spring preset, duration scales, choreography and stagger,
  variables, conditionals, expression syntax, variable modes, interactive
  components, Figma Motion (timeline, keyframes, animation styles, motion
  variables, Dev Mode export, figma.motion Plugin API), Figma Sites
  interactions, motion systems (duration and easing tokens, reduced motion,
  performance, CSS / motion.dev handoff, motion specs), and build recipes for
  sheets, toasts, Shopify variant pickers and cart drawers, filters, forms,
  wallet connect, AI failure states, theme toggles, and state inventories.
  Trigger for Figma prototypes, Smart Animate, transitions, easing, springs,
  Figma Motion, keyframes, animation duration, motion tokens, reduced motion,
  prototype variables, or motion handoff.
---

# Figma Prototyping Lore

Everything about making Figma designs move — the prototyping interaction model,
Smart Animate, Figma Motion's timeline, motion systems, and the recipes that
turn all of it into working prototypes.

> **Part of the Design Lore family.** For Figma tool mechanics (frames,
> components, variants, libraries) use **figma-lore**. For auto layout use
> **figma-autolayout-lore**. For design theory, interaction principles, and
> research methods use **design-lore**. For critique and heuristic evaluation
> use **design-critique-lore**. For Shopify specifics use **shopify-lore**.

## How to Use This Skill

1. **Grep `INDEX.tsv` first** to locate entries by title/topic/tag without
   reading whole modules
2. Identify the relevant module(s) from the index below
3. Read the applicable JSONL file
4. Apply the entries — each has id, topic, title, content, tags
5. For build tasks, start from module 39 (recipes) and pull mechanics from 34–37
6. For review tasks, start from module 38 (critique checklist) and 37 (fm-010)

---

## Module Index

| File | Covers | Key IDs |
|------|--------|---------|
| lore/34-figma-prototyping-core.jsonl | Interaction model, flows, all triggers and actions, overlays, scroll/overflow/sticky, device and presentation, fidelity, testing, handoff, QA | fp-001 → fp-030 |
| lore/35-figma-transitions-motion.jsonl | All transition types, transition semantics, Smart Animate matching and properties, easing presets, spring presets, duration craft, choreography, platform conventions | ft-001 → ft-012 |
| lore/36-figma-advanced-prototyping.jsonl | Variables, Set variable, expression syntax, conditionals, variable modes, interactive components, text input, state modelling, limits | fa-001 → fa-012 |
| lore/37-figma-motion.jsonl | Figma Motion timeline, keyframes, animation styles, animated components, motion variables, export and Dev Mode, `figma.motion` Plugin API, Figma Sites interactions, motion review | fm-001 → fm-010 |
| lore/38-motion-system-handoff.jsonl | Motion as tokens, duration and easing scales, reduced motion, performance, code mapping (CSS / motion.dev), motion spec template, motion personality, critique checklist | ms-001 → ms-009 |
| lore/39-prototype-recipes.jsonl | Step-by-step builds: bottom sheet, toast, Shopify PDP and cart, filters, multi-step form, wallet connect, AI states, theme toggle, skeleton, state inventory | pr-001 → pr-012 |

---

## Quick Topic Routing

### Mechanics
**"Which trigger should I use?"** → 34 (fp-003, fp-004)
**"Which action does what?"** → 34 (fp-005)
**"Navigate to or Change to?"** → 34 (fp-006)
**"Overlay or new frame?"** → 34 (fp-008, fp-009)
**"Why won't my prototype scroll?"** → 34 (fp-010, fp-011)
**"Sticky header / fixed CTA"** → 34 (fp-011)
**"Filter without jumping to top"** → 34 (fp-012) + 39 (pr-005)

### Animation
**"Which transition means what?"** → 35 (ft-002)
**"Smart Animate isn't working"** → 35 (ft-003, ft-004, ft-009)
**"Which easing / which spring?"** → 35 (ft-005, ft-006)
**"How long should this be?"** → 35 (ft-007) + 38 (ms-002)
**"Stagger and choreography"** → 35 (ft-011)
**"Should this animate at all?"** → 35 (ft-010) + 38 (ms-009)

### Advanced
**"Expression syntax"** → 36 (fa-004)
**"Conditionals / validation"** → 36 (fa-005) + 39 (pr-006)
**"Make typing work"** → 36 (fa-009)
**"Live theme toggle"** → 36 (fa-006) + 39 (pr-009)
**"Interactive components"** → 36 (fa-007, fa-008)
**"When do I leave Figma?"** → 36 (fa-012) + 34 (fp-029)

### Figma Motion
**"Timeline / keyframes"** → 37 (fm-001, fm-002)
**"Motion vs prototyping"** → 37 (fm-004)
**"Animation styles / animated components"** → 37 (fm-003)
**"Export and Dev Mode handoff"** → 37 (fm-005) + 38 (ms-006, ms-007)
**"Scripting motion"** → 37 (fm-006)
**"Figma Sites scroll effects"** → 37 (fm-009)

### System & Handoff
**"Motion tokens"** → 38 (ms-001, ms-002, ms-003)
**"Reduced motion"** → 38 (ms-004)
**"Will this jank?"** → 38 (ms-005)
**"Motion spec"** → 38 (ms-007)

---

## Key Principles

- **Every interaction is trigger + action + animation.** Name all three deliberately; defaults are not decisions.
- **State inside a component is `Change to`. State that IS the screen is `Navigate to`.** Getting this wrong is what causes frame explosions.
- **Variables replace duplicated frames.** The moment you duplicate a frame to represent data, stop and make a variable.
- **Transitions are grammar.** Smart animate = same object. Push = sibling. Overlay = on top. Dissolve = elsewhere.
- **Smart Animate matches on layer name AND hierarchy.** Duplicate frames to start; verify matching by hovering in the Prototype tab.
- **Exits are faster than entrances** and use the opposite easing.
- **Nothing over 500ms without a written reason.**
- **Reduced motion is not optional**, and it is a design decision about which motion is informational.
- **Transform and opacity only.** Anything else janks.
- **Prototype the riskiest assumption**, not the happy path. Build the state inventory before the animation.
