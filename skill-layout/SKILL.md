---
name: layout-lore
description: >
  Layout and page architecture craft for web and product design. Covers
  layout first principles (order, grouping, rhythm, breathing), grid systems
  (column, modular, baseline, asymmetric, broken) and the parameters to
  specify per breakpoint, measure and vertical rhythm, whitespace as micro /
  macro / active, alignment and optical correction, responsive strategy (the
  seven reflow behaviours, deriving breakpoints from content, the real fold),
  above-the-fold decisions, section rhythm for long pages, and page
  archetypes with anatomy and pitfalls for landing pages, product detail
  pages, collection and search results, dashboards, forms and multi-step
  flows, and app shells and navigation. Also layout anti-patterns and how to
  specify a layout so it survives implementation. Trigger for layout, grid,
  columns, composition, whitespace, measure, alignment, page structure,
  landing page, dashboard layout, navigation pattern, responsive reflow, or
  requests to design or improve the layout of a page or screen.
---

# Layout Lore

How to structure a page — grids, measure, rhythm, whitespace, responsive
behaviour, and the anatomy of the page types you actually build.

> **Part of the Design Lore family.** For auto layout mechanics in Figma use
> **figma-autolayout-lore**. For spacing tokens and type scales use
> **design-system-lore**. For Gestalt and perception use **design-lore**. For
> evaluating a layout use **design-critique-lore**. For Shopify section and
> block architecture use **shopify-lore**.

## How to Use This Skill

1. For a new page, start from the archetype (ly-009 → ly-014), then apply the
   structural entries (ly-002 → ly-006)
2. For an existing layout that feels wrong, run ly-015 (anti-patterns) first —
   it names most problems in one pass
3. Before handoff, run ly-016
4. Pair with `design-critique-lore` (cr-002, cr-003, cr-006, cr-007) to review

---

## Module Index

| File | Covers | Key IDs |
|------|--------|---------|
| lore/43-layout-systems.jsonl | First principles, grid systems, measure and rhythm, whitespace, alignment and optics, responsive strategy, above the fold, section rhythm, page archetypes (landing, PDP, collection, dashboard, forms, app shell), anti-patterns, implementation spec | ly-001 → ly-016 |

---

## Quick Topic Routing

**"How do I structure this page?"** → ly-001, then the archetype
**"What grid should I use?"** → ly-002
**"The text is hard to read"** → ly-003 (measure, line height)
**"It feels cramped / empty"** → ly-004
**"Things don't line up"** → ly-005
**"How should this behave on mobile?"** → ly-006
**"What goes in the hero?"** → ly-007
**"The page feels long and samey"** → ly-008
**"Landing page"** → ly-009
**"Product page"** → ly-010
**"Collection / search results"** → ly-011
**"Dashboard / analytics"** → ly-012
**"Form / checkout / signup"** → ly-013
**"Navigation and app chrome"** → ly-014
**"Something is off and I can't name it"** → ly-015
**"Will engineering build this correctly?"** → ly-016

---

## Key Principles

- **Content first, structure second, style third.** A layout designed before its real content will break on contact with production.
- **Gap within a group must be visibly smaller than gap between groups.** Violating this changes meaning, not just appearance.
- **Measure is capped on the text, not the container.** 45–75 characters, regardless of how wide the page is.
- **Whitespace is a material, not leftover.** Isolation is the cheapest emphasis available.
- **Density is a user decision.** Professional tools need it; consumer products do not. Applying consumer airiness to a dense tool is a common and costly error.
- **Reflow is a set of decisions.** Name the behaviour for every region: reflow, stack, resize, scroll, disclose, transform, or drop.
- **Derive breakpoints from where content breaks**, then reconcile with devices. Design the 768–1024 middle explicitly.
- **Rank, don't equalise.** An equal-weight grid of six items asserts they matter equally. They don't.
- **Auto layout everywhere.** A layout built with absolute positioning is a screenshot, not a specification.
- **Design the zero, one, and four-hundred cases**, not just the three-items-of-similar-length case.
