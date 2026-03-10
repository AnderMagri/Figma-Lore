---
name: figma-lore
description: >
  Expert Figma and UI design knowledge base covering components, auto layout,
  design systems, tokens, colour systems, iOS/Android specs, responsive design,
  mobile UX, and design system auditing. Also covers deep design intelligence:
  Gestalt psychology, visual perception, heuristic evaluation, typography theory
  (kerning, optical spacing, type scale, variable fonts), applied colour theory,
  behavioural design (Hick's Law, Fitts's Law, cognitive bias, dark patterns),
  and a comprehensive art history library (classical through contemporary digital
  movements including Bauhaus, Swiss Style, Pop Art, Surrealism, Pixel Art,
  Glitch Art, Manga/Anime, Kawaii, Vaporwave, Cyberpunk, Psychedelic, Atomic Age,
  Brutalism, Glassmorphism, Neumorphism, Material Design, Bento Grid, and more).
  Use this skill whenever the user asks about Figma techniques, building
  components, design tokens, colour systems, iOS or Android design specs,
  responsive layouts, component architecture, design system governance, dark mode
  design, multi-brand systems, slots, variants, auto layout patterns, developer
  handoff, typography best practices, colour theory, visual perception, cognitive
  psychology in design, art movements applied to UI/UX, or any visual design
  question. When in doubt, consult this skill.
---

# Figma Lore

A curated knowledge base of Figma best practices, design system architecture,
platform specs, UX patterns, and deep design intelligence.

## How to Use This Skill

1. Identify the relevant module(s) from the index below
2. Read the applicable JSONL file using the view tool
3. Apply the entries — each entry has id, tags, title, and content
4. For complex tasks, consult multiple modules

---

## Module Index

### Figma & System Modules
| File | Covers | Key IDs |
|------|--------|---------|
| lore/00-figma-core.jsonl | Frames, groups, layers, constraints, boolean ops, masks, export, shortcuts | fc-001 → fc-041 |
| lore/01-auto-layout.jsonl | Auto layout direction, sizing, padding, alignment, patterns, responsive | al-001 → al-035 |
| lore/02-design-system.jsonl | Token architecture, variables, theming, styles, spacing, colour palettes, colour systems, multi-brand | ds-001 → ds-056 |
| lore/03-components.jsonl | Component creation, variants, properties, slots, nesting, naming, architecture | cp-001 → cp-043 |
| lore/04-ios-design.jsonl | iPhone/iPad specs, safe areas, SF Pro, SF Symbols, HIG patterns | ios-001 → ios-050 |
| lore/05-android-design.jsonl | Material 3, Pixel specs, window classes, navigation, M3 components | an-001 → an-052 |
| lore/06-responsive.jsonl | Breakpoints, constraints, auto layout responsive patterns, pixel density | rs-001 → rs-030 |
| lore/07-mobile-ux.jsonl | Navigation, thumb zones, gestures, loading states, empty states, forms, dark mode | ux-001 → ux-035 |
| lore/08-organization.jsonl | File structure, library architecture, naming, versioning, governance, handoff | og-001 → og-027 |
| lore/09-audit-optimization.jsonl | Detached instances, hardcoded values, audit scripts, health score | au-001 → au-025 |
| lore/10-execution-recipes.jsonl | Step-by-step recipes for creating components, tokens, DS bootstrap, gotchas | ex-001 → ex-038 |

### Design Intelligence Modules
| File | Covers | Key IDs |
|------|--------|---------|
| lore/11-gestalt-perception.jsonl | Gestalt laws (proximity, similarity, closure, continuity, figure-ground, symmetry, common fate, prägnanz), preattentive attributes, scanning patterns, heuristic evaluation | gp-001 → gp-016 |
| lore/12-typography-deep.jsonl | Type anatomy, classification, optical vs mechanical spacing, kerning, tracking, leading, type scale, alignment, measure, pairing, variable fonts, rendering, emotion, design system tokens | ty-001 → ty-014 |
| lore/13-colour-theory.jsonl | HSL/HSB, colour harmonies, temperature, contrast/WCAG, simultaneous contrast, colour psychology by hue, colour systems, palette construction, dark mode colour, light physics, branding, cultural context | ct-001 → ct-012 |
| lore/14-behavioural-design.jsonl | Mental models, cognitive load, Hick's Law, Fitts's Law, Jakob's Law, Miller's Law, anchoring bias, Peak-End Rule, endowment effect, variable rewards, dark patterns, ethical nudges, emotional design | bd-001 → bd-013 |
| lore/15-art-history-part1.jsonl | Renaissance, Baroque, Art Nouveau, Bauhaus, De Stijl/Constructivism, Art Deco, Swiss Style, Pop Art, Surrealism, Atomic/Space Age, Psychedelic/Acid, 70s, Punk/Zine, Memphis Group, Hyperrealism, Grunge/90s | ah-001 → ah-016 |
| lore/15-art-history-part2.jsonl | Manga/Anime, Kawaii, Yami Kawaii, Vaporwave, Cyberpunk, Pixel Art, Glitch Art, Skeuomorphism, Flat Design, Material Design, Neumorphism, Glassmorphism, Web Brutalism, Minimalism, Retrowave/Synthwave, Contemporary Japanese, Maximalism, 3D Illustration, Neo-Brutalism, Bento Grid, Biophilic Design, How to Apply Art History | ah-017 → ah-038 |

---

## Quick Topic Routing

### Figma & Systems
**"Build a button / card / input / navbar component"**
→ lore/10-execution-recipes.jsonl (ex-004 to ex-010) + lore/03-components.jsonl

**"Set up design tokens / variables / colour system"**
→ lore/02-design-system.jsonl (ds-001 to ds-015 for tokens, ds-031 to ds-056 for colour)

**"Light and dark mode"**
→ lore/02-design-system.jsonl (ds-049 to ds-056) + lore/13-colour-theory.jsonl (ct-009) + lore/07-mobile-ux.jsonl (ux-031, ux-032)

**"Multi-brand colour system"**
→ lore/02-design-system.jsonl (ds-046 to ds-056) + lore/13-colour-theory.jsonl (ct-007, ct-008)

**"Slots in Figma"**
→ lore/03-components.jsonl (cp-027, cp-027b, cp-028, cp-028b)

**"iOS / Android specs"**
→ lore/04-ios-design.jsonl or lore/05-android-design.jsonl

**"Audit a design system"**
→ lore/09-audit-optimization.jsonl + lore/10-execution-recipes.jsonl (ex-034, ex-035)

### Typography
**"Kerning / optical spacing"** → lore/12-typography-deep.jsonl (ty-003, ty-004)
**"Type scale / hierarchy"** → lore/12-typography-deep.jsonl (ty-006, ty-014)
**"Font pairing"** → lore/12-typography-deep.jsonl (ty-009, ty-013)
**"Accessible type"** → lore/12-typography-deep.jsonl (ty-011, ty-012)
**"Variable fonts"** → lore/12-typography-deep.jsonl (ty-010)

### Colour
**"Colour system / tokens"** → lore/13-colour-theory.jsonl (ct-007, ct-008) + lore/02-design-system.jsonl (ds-046→ds-056)
**"WCAG contrast"** → lore/13-colour-theory.jsonl (ct-004)
**"Colour psychology / brand"** → lore/13-colour-theory.jsonl (ct-006, ct-011, ct-012)
**"Colour harmony / palette"** → lore/13-colour-theory.jsonl (ct-002, ct-008)

### Perception & Psychology
**"Gestalt / visual hierarchy"** → lore/11-gestalt-perception.jsonl (gp-001 → gp-009)
**"Heuristic evaluation"** → lore/11-gestalt-perception.jsonl (gp-013, gp-014, gp-015)
**"Cognitive bias / conversion"** → lore/14-behavioural-design.jsonl (bd-007 to bd-010)
**"Dark patterns / ethics"** → lore/14-behavioural-design.jsonl (bd-011, bd-012)
**"UX laws"** → lore/14-behavioural-design.jsonl (bd-003 to bd-006)
**"Emotional design"** → lore/14-behavioural-design.jsonl (bd-013)

### Art & Aesthetic Direction
**"What style for this brand/product"** → lore/15-art-history-part1.jsonl + lore/15-art-history-part2.jsonl (ah-038 for framework)
**"Bauhaus / Swiss Style / modernism"** → lore/15-art-history-part1.jsonl (ah-004, ah-007)
**"Japanese aesthetics / Kawaii / Manga / Vaporwave"** → lore/15-art-history-part2.jsonl (ah-017 to ah-021)
**"Pixel art / Glitch art / retro digital"** → lore/15-art-history-part2.jsonl (ah-022, ah-023, ah-031)
**"Current UI trends (Glass, Bento, Brutalism, Minimal)"** → lore/15-art-history-part2.jsonl (ah-025→ah-030, ah-035, ah-036)
**"Luxury / premium aesthetic"** → lore/15-art-history-part1.jsonl (ah-002, ah-006)
**"Retro / vintage"** → lore/15-art-history-part1.jsonl (ah-010, ah-012) + lore/15-art-history-part2.jsonl (ah-031)
**"Wellness / organic / nature"** → lore/15-art-history-part1.jsonl (ah-003) + lore/15-art-history-part2.jsonl (ah-037)

---

## Key Design Principles (Always Apply)

- **Token chain is sacred**: Component → Semantic → Primitive. Never skip layers.
- **Auto layout everywhere**: 95%+ of components must use auto layout.
- **Name everything**: No default layer names (Frame 1, Rectangle 3). Ever.
- **Variables over hardcode**: All colours, spacing, and radii must use variables.
- **Mobile-first**: Design at 393×852 (iOS) or 412×915 (Android) as primary.
- **Touch targets**: 44×44pt iOS, 48×48dp Android. Non-negotiable.
- **WCAG AA**: 4.5:1 contrast for normal text, 3:1 for large text and UI components.
- **Gestalt before pixels**: Every layout decision answers to gestalt principles first.
- **Type scale not arbitrary sizes**: Every type size belongs to a defined scale.
- **Colour has meaning**: Every colour token has semantic intent, not just aesthetic preference.
- **Art history is a library**: Every aesthetic direction has historical precedent — know what you're referencing.
