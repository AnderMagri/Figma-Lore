---
name: figma-lore-autolayout
description: >
  Expert knowledge base for Figma Auto Layout. Direction (horizontal, vertical,
  wrap, grid 2025), sizing (Hug Contents, Fill Container, Fixed, min/max),
  padding, gap, alignment (9-point grid, align-self, baseline), absolute
  positioning, responsive patterns, layout optimization (redundant nesting,
  single-child anti-patterns, same-direction flattening, Dev Mode CSS output),
  component AL recipes (button, input, form field, checkbox, badge, list item,
  modal, icon button, alert, toggle, bottom nav, avatar), slots (Figma 2025),
  responsive-first philosophy, resize cascade checklist, text-fill rule. Use for:
  auto layout, frame sizing, Hug vs Fill vs Fixed, gap and padding, responsive
  Figma layouts, layout optimization, nested frames, redundant frames, slots,
  frame sizing issues, text overflow, layouts that break on resize, or any Figma
  layout and component structure question — even without "auto layout".
---

# Figma Lore — Auto Layout

Everything about Figma Auto Layout: fundamentals, sizing, patterns, responsive behaviour,
optimization, performance, and Figma 2025 features including slots.

> **Part of the Design Lore family.** For design system theory (tokens, variables,
> theming), use **design-lore-systems**. For components (variants, properties,
> naming), use **figma-lore**. For design theory and process, use **design-lore**.

## How to Use This Skill

1. Identify the relevant module(s) from the index below
2. Read the applicable JSONL file using the Read tool
3. Apply the entries — each entry has id, cat, t (title), tags, and d (content)
4. For complex layout tasks, check both modules — advanced entries complement core entries

---

## Module Index

| File | Covers | Key IDs |
|------|--------|---------|
| lore/01-auto-layout.jsonl | Fundamentals, direction, wrap, grid, spacing, sizing, padding, alignment, absolute position, responsive patterns, layout patterns, shortcuts, philosophy, resize checklist | al-001 → al-038 |
| lore/01b-autolayout-advanced.jsonl | Redundant nesting, hierarchy optimization, single-child anti-pattern, same-direction nesting, Dev Mode CSS output, common mistakes/fixes, slots (2025): how slots work, sizing slots, slots vs instance swap, building a slotted component | al-039 → al-048 |
| lore/01c-component-recipes.jsonl | Precise optimized AL recipes for: button (default/full-width/icon-only), input field, form field group (label+input+helper), checkbox/radio, badge/tag/chip, list item, modal/dialog, icon button, alert/banner, toggle/switch, bottom navigation bar, avatar with status badge | al-049 → al-060 |

---

## Quick Topic Routing

### Fundamentals
**"Add / remove auto layout"**
→ lore/01-auto-layout.jsonl (al-001, al-002)

**"What is auto layout / how it works"**
→ lore/01-auto-layout.jsonl (al-003, al-004)

**"Horizontal vs vertical direction"**
→ lore/01-auto-layout.jsonl (al-005, al-006)

**"Wrap mode / multi-row layout"**
→ lore/01-auto-layout.jsonl (al-007)

**"Grid layout in Figma (2025)"**
→ lore/01-auto-layout.jsonl (al-008, al-027, al-028)

**"Freeform mode"**
→ lore/01-auto-layout.jsonl (al-029)

### Sizing
**"Hug Contents / shrink to fit"**
→ lore/01-auto-layout.jsonl (al-012)

**"Fill Container / stretch to parent"**
→ lore/01-auto-layout.jsonl (al-013)

**"Fixed size"**
→ lore/01-auto-layout.jsonl (al-014)

**"Hug + Fill combination"**
→ lore/01-auto-layout.jsonl (al-015)

**"Min width / max width / min height / max height"**
→ lore/01-auto-layout.jsonl (al-016)

**"Text sizing — Fill Container rule"**
→ lore/01-auto-layout.jsonl (al-037)

### Spacing & Alignment
**"Gap / packed spacing"**
→ lore/01-auto-layout.jsonl (al-009)

**"Space between / distribute evenly"**
→ lore/01-auto-layout.jsonl (al-010)

**"Negative gap / overlapping elements / stacked avatars"**
→ lore/01-auto-layout.jsonl (al-011, al-035)

**"Padding / uniform vs independent"**
→ lore/01-auto-layout.jsonl (al-017)

**"Alignment grid / justify and align"**
→ lore/01-auto-layout.jsonl (al-018)

**"Align self / individual child override"**
→ lore/01-auto-layout.jsonl (al-019)

**"Baseline alignment for text"**
→ lore/01-auto-layout.jsonl (al-020)

### Absolute Positioning
**"Absolute position within auto layout / badges / overlays"**
→ lore/01-auto-layout.jsonl (al-021)

### Layout Patterns
**"Navbar pattern"**
→ lore/01-auto-layout.jsonl (al-022)

**"Card component pattern"**
→ lore/01-auto-layout.jsonl (al-023)

**"Form layout pattern"**
→ lore/01-auto-layout.jsonl (al-024)

**"Sidebar layout pattern"**
→ lore/01-auto-layout.jsonl (al-025)

**"Header-content-footer / sticky footer"**
→ lore/01-auto-layout.jsonl (al-026)

**"Responsive wrap grid pattern"**
→ lore/01-auto-layout.jsonl (al-030)

**"Adaptive text container / min-max for text"**
→ lore/01-auto-layout.jsonl (al-031)

**"Common spacing values / reference"**
→ lore/01-auto-layout.jsonl (al-032)

### Responsive & Philosophy
**"Responsive-first philosophy / resize cascade"**
→ lore/01-auto-layout.jsonl (al-036)

**"Resize cascade checklist / verify before handoff"**
→ lore/01-auto-layout.jsonl (al-038)

**"Text fill rule / text width should always fill"**
→ lore/01-auto-layout.jsonl (al-037)

### Optimization & Common Mistakes
**"Redundant nesting / unnecessary wrapper frames"**
→ lore/01b-autolayout-advanced.jsonl (al-039)

**"Hierarchy optimization / flatten where possible"**
→ lore/01b-autolayout-advanced.jsonl (al-040)

**"Single-child frame anti-pattern"**
→ lore/01b-autolayout-advanced.jsonl (al-041)

**"Same-direction nested AL / when to flatten"**
→ lore/01b-autolayout-advanced.jsonl (al-042)

**"Dev Mode CSS output / how AL maps to code"**
→ lore/01b-autolayout-advanced.jsonl (al-043)

**"Common auto layout mistakes and fixes"**
→ lore/01b-autolayout-advanced.jsonl (al-044)

**"Groups inside auto layout / convert to frame"**
→ lore/01-auto-layout.jsonl (al-033) + lore/01b-autolayout-advanced.jsonl (al-044)

**"Spacer frames / avoid spacers"**
→ lore/01-auto-layout.jsonl (al-033)

### Shortcuts & Tips
**"Auto layout shortcuts / keyboard shortcuts"**
→ lore/01-auto-layout.jsonl (al-034)

### Component Recipes (Precise AL Structures)
**"Button AL structure / button layout / icon + label"**
→ lore/01c-component-recipes.jsonl (al-049)

**"Input field AL structure / text input / placeholder"**
→ lore/01c-component-recipes.jsonl (al-050)

**"Form field group / label + input + helper text / error state"**
→ lore/01c-component-recipes.jsonl (al-051)

**"Checkbox AL structure / radio button"**
→ lore/01c-component-recipes.jsonl (al-052)

**"Badge AL structure / tag / chip / pill"**
→ lore/01c-component-recipes.jsonl (al-053)

**"List item AL structure / avatar + content + trailing"**
→ lore/01c-component-recipes.jsonl (al-054)

**"Modal AL structure / dialog / header body footer"**
→ lore/01c-component-recipes.jsonl (al-055)

**"Icon button AL structure"**
→ lore/01c-component-recipes.jsonl (al-056)

**"Alert AL structure / banner / notification"**
→ lore/01c-component-recipes.jsonl (al-057)

**"Toggle AL structure / switch component"**
→ lore/01c-component-recipes.jsonl (al-058)

**"Bottom navigation bar AL structure / mobile tab bar"**
→ lore/01c-component-recipes.jsonl (al-059)

**"Avatar with status badge / absolute position overlap"**
→ lore/01c-component-recipes.jsonl (al-060)

### Slots (Figma 2025)
**"What are slots / how do slots work"**
→ lore/01b-autolayout-advanced.jsonl (al-045)

**"Slot sizing / Fill and Hug for slot frames"**
→ lore/01b-autolayout-advanced.jsonl (al-046)

**"Slots vs Instance Swap properties"**
→ lore/01b-autolayout-advanced.jsonl (al-047)

**"How to add a slot to a component / step-by-step"**
→ lore/01b-autolayout-advanced.jsonl (al-048)

---

## Core Rules (Always Apply)

- **Auto layout everywhere**: 95%+ of layout work must use auto layout. Manual positioning is for overlapping decorative elements only.
- **Text width = Fill Container**: Text layers inside AL frames always use Fill width. Fixed-width text is almost always wrong.
- **No groups inside AL**: Groups break AL sizing. Always convert to frames before placing inside AL.
- **No spacer frames**: Use gap and padding, never empty spacer frames.
- **Every frame earns its place**: Before adding a wrapper frame, verify it provides independent background, clip, different alignment, or scroll behaviour. If not, eliminate it.
- **Resize cascade is the test**: If manually repositioning anything after resizing the parent, the layout is broken. Fix the root sizing mode.
- **Fixed only for known-dimension elements**: Icons, avatars, and images with fixed aspect ratios use Fixed. Everything else prefers Hug or Fill.
- **Slots use Fill + Hug**: Slot frames set to Fill width and Hug height let content grow naturally without detaching instances.
- **Same-direction nesting is a smell**: Two vertical AL frames with the same gap and no visual differentiation should be one frame.
