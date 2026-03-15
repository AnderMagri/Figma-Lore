---
name: figma-lore
description: >
  Expert Figma knowledge base. Covers frames, groups, layers, constraints,
  boolean operations, masks, export, keyboard shortcuts, auto layout (direction,
  sizing, padding, alignment, responsive patterns, wrap, min/max), components
  (creation, variants, properties, slots, nesting, naming, architecture),
  file and library organisation (structure, naming, versioning, governance,
  handoff), design system auditing (detached instances, hardcoded values, audit
  scripts, health scores), and step-by-step execution recipes (building buttons,
  cards, inputs, navbars, token setup, DS bootstrap, common gotchas). Trigger
  for any question about Figma mechanics, auto layout, components, variants,
  slots, file structure, library management, design system audits, or
  Figma-specific how-to recipes.
---

# Figma Lore

Everything about the Figma tool itself — mechanics, features, shortcuts,
component architecture, file organisation, auditing, and step-by-step recipes.

> **Part of the Design Lore family.** For design theory, platform specs,
> typography, colour, and process, use **design-lore**. For deep UX psychology,
> use **design-lore-psychology**. For ecommerce and crypto/fintech UX, use
> **design-lore-industry**.

## How to Use This Skill

1. Identify the relevant module(s) from the index below
2. Read the applicable JSONL file using the view tool
3. Apply the entries — each entry has id, tags, title, and content
4. For complex tasks, consult multiple modules

---

## Module Index

| File | Covers | Key IDs |
|------|--------|---------|
| lore/00-figma-core.jsonl | Frames, groups, layers, constraints, boolean ops, masks, export, shortcuts | fc-001 → fc-041 |
| lore/01-auto-layout.jsonl | Auto layout direction, sizing, padding, alignment, patterns, responsive | al-001 → al-035 |
| lore/03-components.jsonl | Component creation, variants, properties, slots, nesting, naming, architecture | cp-001 → cp-043 |
| lore/08-organization.jsonl | File structure, library architecture, naming, versioning, governance, handoff | og-001 → og-027 |
| lore/09-audit-optimization.jsonl | Detached instances, hardcoded values, audit scripts, health score | au-001 → au-025 |
| lore/10-execution-recipes.jsonl | Step-by-step recipes for creating components, tokens, DS bootstrap, gotchas | ex-001 → ex-038 |

---

## Quick Topic Routing

### Figma Core
**"Frames vs groups"** → lore/00-figma-core.jsonl (fc-001 to fc-005)
**"Constraints / resizing"** → lore/00-figma-core.jsonl (fc-010 to fc-015)
**"Boolean operations"** → lore/00-figma-core.jsonl (fc-020 to fc-025)
**"Masks"** → lore/00-figma-core.jsonl (fc-026 to fc-028)
**"Export settings"** → lore/00-figma-core.jsonl (fc-035 to fc-041)
**"Keyboard shortcuts"** → lore/00-figma-core.jsonl (fc-030 to fc-034)

### Auto Layout
**"Auto layout basics / direction / sizing"** → lore/01-auto-layout.jsonl (al-001 to al-010)
**"Padding / spacing / alignment"** → lore/01-auto-layout.jsonl (al-011 to al-020)
**"Responsive auto layout / wrap / min-max"** → lore/01-auto-layout.jsonl (al-021 to al-035)

### Components
**"Build a button / card / input / navbar"** → lore/10-execution-recipes.jsonl (ex-004 to ex-010) + lore/03-components.jsonl
**"Variants / properties / boolean props"** → lore/03-components.jsonl (cp-010 to cp-020)
**"Slots in Figma"** → lore/03-components.jsonl (cp-027, cp-027b, cp-028, cp-028b)
**"Component naming / architecture"** → lore/03-components.jsonl (cp-030 to cp-043)

### Organisation & Auditing
**"File structure / library setup"** → lore/08-organization.jsonl (og-001 to og-015)
**"Naming conventions"** → lore/08-organization.jsonl (og-016 to og-020)
**"Versioning / governance"** → lore/08-organization.jsonl (og-021 to og-027)
**"Audit a design system"** → lore/09-audit-optimization.jsonl + lore/10-execution-recipes.jsonl (ex-034, ex-035)
**"Detached instances / hardcoded values"** → lore/09-audit-optimization.jsonl (au-001 to au-010)

### Recipes
**"Set up design tokens in Figma"** → lore/10-execution-recipes.jsonl (ex-001 to ex-003)
**"Bootstrap a design system"** → lore/10-execution-recipes.jsonl (ex-030 to ex-038)
**"Common Figma gotchas"** → lore/10-execution-recipes.jsonl (ex-035 to ex-038)

---

## Key Principles

- **Auto layout everywhere**: 95%+ of components must use auto layout.
- **Name everything**: No default layer names (Frame 1, Rectangle 3). Ever.
- **Variables over hardcode**: All colours, spacing, and radii must use variables.
- **Token chain is sacred**: Component → Semantic → Primitive. Never skip layers.
