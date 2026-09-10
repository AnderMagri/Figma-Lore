---
name: design-lore-systems
description: >
  Expert knowledge base for design systems. Token architecture (three-layer
  model: primitives, semantics, components), Figma variables (types, collections,
  modes, scoping, aliases), theming (light/dark, multi-brand, density), OKLCH
  colour space, colour systems (palette, semantic mapping, WCAG, 60-30-10 rule,
  dark-elevated vs dark-deep), naming conventions (W3C DTCG, Fills/Strokes/Alt,
  state names, t-shirt vs numeric scales), typography tokens (text styles,
  variables, responsive modes), spacing and elevation scales, grid layout tokens,
  library publishing, governance, auditing, and DS maturity. Use for: design
  tokens, variables, theming, primitives vs semantics, dark mode, multi-brand,
  colour systems, OKLCH, naming conventions, token architecture, type scale,
  spacing scale, DS audit, library management, Figma variables setup, or building
  a design system — even without the words "design system".
---

# Design Lore — Systems

The complete knowledge base for building, maintaining, and scaling design systems.
Token architecture, variables, theming, colour, typography, governance, and auditing.

> **Part of the Design Lore family.** For Figma mechanics (auto layout, components,
> file structure), use **figma-lore**. For deep UX psychology, use
> **design-lore-psychology**. For broad design theory and process, use **design-lore**.
> For ecommerce and fintech UX, use **design-lore-industry**.

> **Note on overlap.** `lore/02-design-system.jsonl` and parts of the colour,
> typography and governance modules are mirrored from **design-lore**. Where
> they overlap, design-lore is canonical — this skill is the focused extract.

## How to Use This Skill

1. **Grep `INDEX.tsv` first** to locate entries by title/topic/tag without
   reading whole modules
2. Identify the relevant module(s) from the index below
3. Read the applicable JSONL file using the Read tool
4. Apply the entries — every entry has `id`, `topic`, `title`, `content`, `tags`,
   and optionally `source`, `example`, `meta` (hard numbers — specs, dp/pt, ratios)
5. For complex tasks, consult multiple modules

---

## Module Index

| File | Covers | Key IDs |
|------|--------|---------|
| lore/02-design-system.jsonl | Token architecture, Figma variables, collections, modes, theming, styles, spacing, sizing, opacity, library, governance, audit, maturity checklist | ds-001 → ds-048 |
| lore/naming-conventions.jsonl | W3C DTCG format, Fills/Strokes/Alt neutral naming, state naming, numeric vs t-shirt scales, component token patterns, collection naming, boolean naming, grid token naming, slash hierarchy depth | nc-001 → nc-009 |
| lore/colour-advanced.jsonl | OKLCH colour space (what it is, vs HSL, building scales, in Figma + CSS), Dark Elevated vs Dark Deep strategies, 48-step linear neutral scale, 16×9 accent palette architecture, shade contrast rules, 60-30-10 rule, utility/overlay colours | ca-001 → ca-010 |
| lore/colour-system.jsonl | Colour system layers, palette construction, semantic mapping, dark mode colour, accessibility contrast, branding | ct-007, ct-008, ct-009, ct-004, ct-011 |
| lore/typography-system.jsonl | Type scale, font pairing, variable fonts, accessibility, typography tokens, bold/weight naming conventions | ty-006, ty-009, ty-010, ty-011, ty-014, ty-015 |
| lore/governance.jsonl | Design QA checklist, review gates, developer handoff specs, version control for design | do-002, do-003, do-005, do-007 |

---

## Quick Topic Routing

### Naming Conventions
**"W3C DTCG format / universal token standard / Token Studio / Style Dictionary"**
→ lore/naming-conventions.jsonl (nc-001)

**"Neutral colour naming / Fills Strokes Alt model"**
→ lore/naming-conventions.jsonl (nc-002)

**"State naming conventions / hover active focus disabled"**
→ lore/naming-conventions.jsonl (nc-003)

**"Token scale / numeric 100-900 vs t-shirt xs-xl vs named"**
→ lore/naming-conventions.jsonl (nc-004)

**"Component token naming patterns / button input card"**
→ lore/naming-conventions.jsonl (nc-005)

**"Collection naming / mode naming / variable organisation"**
→ lore/naming-conventions.jsonl (nc-006)

**"Boolean variable naming / show-hide / feature flags"**
→ lore/naming-conventions.jsonl (nc-007)

**"Grid and layout token naming / columns gutter margin"**
→ lore/naming-conventions.jsonl (nc-008)

**"Slash hierarchy depth / grouping strategy"**
→ lore/naming-conventions.jsonl (nc-009) + lore/02-design-system.jsonl (ds-037)

### OKLCH and Advanced Colour
**"OKLCH / modern colour space / what it is"**
→ lore/colour-advanced.jsonl (ca-001)

**"OKLCH vs HSL / why HSL is wrong for design systems"**
→ lore/colour-advanced.jsonl (ca-002)

**"Building a colour scale in OKLCH / step by step"**
→ lore/colour-advanced.jsonl (ca-003)

**"OKLCH in Figma / OKLCH in CSS / Color 4"**
→ lore/colour-advanced.jsonl (ca-004)

**"Dark mode strategies / Dark Elevated vs Dark Deep"**
→ lore/colour-advanced.jsonl (ca-005)

**"48-step neutral scale / linear progression palette"**
→ lore/colour-advanced.jsonl (ca-006)

**"Accent palette architecture / 16 colours 9 shades"**
→ lore/colour-advanced.jsonl (ca-007)

**"Shade contrast rules / which shade for buttons borders text"**
→ lore/colour-advanced.jsonl (ca-008)

**"60-30-10 rule applied to design tokens"**
→ lore/colour-advanced.jsonl (ca-009)

**"Utility colours / overlay / tint / opacity"**
→ lore/colour-advanced.jsonl (ca-010)

### Token Architecture
**"Three-layer token model / primitives vs semantics"**
→ lore/02-design-system.jsonl (ds-001 to ds-005)

**"Token naming conventions"**
→ lore/02-design-system.jsonl (ds-023, ds-024)

**"Token layer rules / when to use each layer"**
→ lore/02-design-system.jsonl (ds-005, ds-014)

**"Component tokens / button tokens / input tokens"**
→ lore/02-design-system.jsonl (ds-004, ds-033)

### Figma Variables
**"Variable types in Figma (color/number/string/boolean)"**
→ lore/02-design-system.jsonl (ds-006)

**"Variable aliases / how to reference one variable from another"**
→ lore/02-design-system.jsonl (ds-007)

**"Variable collections / organization"**
→ lore/02-design-system.jsonl (ds-008, ds-037)

**"Variable modes / light-dark / responsive"**
→ lore/02-design-system.jsonl (ds-009, ds-010)

**"Variable scoping / prevent misuse"**
→ lore/02-design-system.jsonl (ds-021, ds-022)

**"How to create variables in Figma / step-by-step"**
→ lore/02-design-system.jsonl (ds-036)

**"Boolean variables / visibility toggles"**
→ lore/02-design-system.jsonl (ds-044)

### Theming
**"Light/dark mode setup / step-by-step"**
→ lore/02-design-system.jsonl (ds-011) + lore/colour-system.jsonl (ct-009)

**"Light/dark mode colour rules"**
→ lore/02-design-system.jsonl (ds-012) + lore/colour-system.jsonl (ct-009)

**"Multi-brand / white-label system"**
→ lore/02-design-system.jsonl (ds-013)

**"Theme switching in Figma"**
→ lore/02-design-system.jsonl (ds-034)

**"Density modes / compact vs comfortable"**
→ lore/02-design-system.jsonl (ds-043)

**"Applying and inheriting modes across frames"**
→ lore/02-design-system.jsonl (ds-010)

### Colour System
**"Building a colour palette from scratch"**
→ lore/colour-system.jsonl (ct-008) + lore/02-design-system.jsonl (ds-031)

**"Semantic colour mapping for light and dark"**
→ lore/02-design-system.jsonl (ds-032) + lore/colour-system.jsonl (ct-007, ct-009)

**"Colour system layers / primitive → semantic → component"**
→ lore/colour-system.jsonl (ct-007) + lore/02-design-system.jsonl (ds-001 to ds-005)

**"WCAG contrast / accessibility"**
→ lore/colour-system.jsonl (ct-004) + lore/02-design-system.jsonl (ds-038)

**"Dark mode colour principles"**
→ lore/colour-system.jsonl (ct-009) + lore/02-design-system.jsonl (ds-011, ds-012)

**"Brand colour / 60-30-10 rule"**
→ lore/colour-system.jsonl (ct-011)

### Styles (Figma)
**"When to use styles vs variables"**
→ lore/02-design-system.jsonl (ds-014)

**"Text styles / typography styles"**
→ lore/02-design-system.jsonl (ds-016, ds-017) + lore/typography-system.jsonl (ty-014, ty-015)

**"Color styles / gradient styles"**
→ lore/02-design-system.jsonl (ds-015)

**"Effect styles / shadows / elevation"**
→ lore/02-design-system.jsonl (ds-018, ds-019)

**"Grid styles / breakpoints"**
→ lore/02-design-system.jsonl (ds-020)

### Typography System
**"Type scale / size hierarchy"**
→ lore/typography-system.jsonl (ty-006) + lore/02-design-system.jsonl (ds-016)

**"Typography variables in Figma / setup workflow"**
→ lore/02-design-system.jsonl (ds-046)

**"Responsive typography / desktop and mobile modes"**
→ lore/02-design-system.jsonl (ds-047)

**"Typography variable types / string vs number / naming"**
→ lore/02-design-system.jsonl (ds-048) + lore/typography-system.jsonl (ty-014)

**"Text style naming / bold and weight variants"**
→ lore/typography-system.jsonl (ty-015) + lore/02-design-system.jsonl (ds-016)

**"Font pairing strategy"**
→ lore/typography-system.jsonl (ty-009)

**"Variable fonts"**
→ lore/typography-system.jsonl (ty-010)

**"Type accessibility / contrast and legibility"**
→ lore/typography-system.jsonl (ty-011) + lore/colour-system.jsonl (ct-004)

### Spacing, Sizing & Elevation
**"Spacing scale / 4px grid"**
→ lore/02-design-system.jsonl (ds-029, ds-030)

**"Spacing application / padding and gap patterns"**
→ lore/02-design-system.jsonl (ds-030)

**"Border-radius scale"**
→ lore/02-design-system.jsonl (ds-039)

**"Icon sizing / touch targets"**
→ lore/02-design-system.jsonl (ds-040)

**"Opacity scale"**
→ lore/02-design-system.jsonl (ds-041)

**"Elevation / shadow scale"**
→ lore/02-design-system.jsonl (ds-018, ds-019)

### Library & Governance
**"Library publishing workflow"**
→ lore/02-design-system.jsonl (ds-025)

**"Library file structure / foundation vs core vs pattern"**
→ lore/02-design-system.jsonl (ds-026)

**"Library versioning / changelog"**
→ lore/02-design-system.jsonl (ds-042) + lore/governance.jsonl (do-007)

**"Design system governance / contribution model / deprecation"**
→ lore/02-design-system.jsonl (ds-027)

**"Design system maturity checklist"**
→ lore/02-design-system.jsonl (ds-045)

### Auditing
**"Design system audit / detached instances / hardcoded values"**
→ lore/02-design-system.jsonl (ds-028)

**"QA checklist / implementation verification"**
→ lore/governance.jsonl (do-002)

**"Developer handoff / token-based specs"**
→ lore/governance.jsonl (do-005)

**"Design review gates"**
→ lore/governance.jsonl (do-003)

**"Design version control"**
→ lore/governance.jsonl (do-007)

---

## Non-Negotiable Principles

- **Token chain is sacred**: Component → Semantic → Primitive. Never skip layers or use primitives directly in components.
- **Variables over hardcode**: Every colour, spacing, radius, and opacity value must reference a variable. No literal hex, no magic numbers.
- **Scoping prevents drift**: Always scope variables to their applicable properties. A colour variable must not appear in spacing dropdowns.
- **Modes power theming**: Light/dark, multi-brand, and density are all modes — the same semantic variable gets different primitive references per mode.
- **Styles compose, variables atomise**: Variables define individual values; text styles and effect styles compose them. Use both.
- **8–12 text styles max**: More than 12 text styles signals a broken type scale. Audit and consolidate.
- **4px base grid**: All spacing tokens must be multiples of 4. No arbitrary pixel values.
- **WCAG AA is a floor, not a ceiling**: Every colour token combination must pass 4.5:1 for normal text. Verify in all modes.
- **Governance is a feature**: A DS without a contribution process, deprecation policy, and versioned changelog is not a system — it is a shared file.
