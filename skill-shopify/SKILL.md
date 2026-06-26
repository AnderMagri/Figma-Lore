---
name: shopify-lore
description: >
  Shopify storefront design knowledge for Figma. Covers theme
  architecture (layouts, templates, sections, blocks), selling plans
  (subscriptions, pre-orders, TBYB), best practices (performance,
  accessibility), pricing, merchandising (variants, media,
  recommendations), navigation & search, Horizon design system
  (tokens, colour schemes, typography, spacing, components), design
  feasibility review (Native vs Liquid vs Custom for any UI element),
  and dev handoff (Figma-to-Shopify mapping, settings schema
  annotations, variant selector specs, metafields, token naming,
  breakpoints, edge cases, app block slots, handoff checklist).
  Trigger for Shopify theme, Liquid, selling plans, sections, blocks,
  variants, filtering, Horizon, tokens, storefront design in Figma,
  feasibility review, or dev handoff. For ecommerce UX use
  ecommerce-lore.
---

# Shopify Lore

Shopify platform-specific knowledge sourced from official shopify.dev
documentation — theme architecture, selling plans, pricing, merchandising,
navigation, and design principles for building storefronts in Figma.

> **Part of the Design Lore family.** This module covers Shopify platform
> specifics. For general ecommerce UX (conversion benchmarks, CRO, psychology),
> use **ecommerce-lore**. For crypto/fintech UX, use **design-lore-industry**.
> For core design knowledge, use **design-lore**.

## How to Use This Skill

1. Identify the relevant entry from the index below
2. Read the applicable JSONL entries
3. Pay attention to FIGMA IMPLICATION notes at the end of each entry
4. Cross-reference with ecommerce-lore for empirical conversion data

---

## Module Index

### Theme Design & Selling Plans
| File | Covers | Key IDs |
|------|--------|---------|
| lore/25-shopify-theme-design.jsonl | Theme design principles (merchant experience), theme design principles (customer experience), subscription product form, subscription selling plan selection & options, subscription cart/orders/multi-currency, pre-order & TBYB product form, pre-order & TBYB cart/orders/naming | sh-001 → sh-007 |

### Theme Architecture
| File | Covers | Key IDs |
|------|--------|---------|
| lore/26-shopify-theme-architecture.jsonl | Directory structure & hierarchy, layouts (theme.liquid, required objects), templates (types, JSON vs Liquid, naming), sections (schema, presets, rendering, app blocks), blocks (theme blocks, section blocks, app blocks, nesting, vs snippets) | sh-008 → sh-012 |

### Best Practices
| File | Covers | Key IDs |
|------|--------|---------|
| lore/27-shopify-best-practices.jsonl | Performance (JavaScript 16KB limit, lazy-load, CDN, Lighthouse scoring formula, responsive images), accessibility (WCAG, keyboard, contrast ratios, touch targets 44px, ARIA, focus management), sections & blocks best practices (modularity, settings, metafields, block layouts, app blocks) | sh-013 → sh-015 |

### Pricing & Payments
| File | Covers | Key IDs |
|------|--------|---------|
| lore/28-shopify-pricing-payments.jsonl | Discounts (line-item, cart-level, strikethrough, calculation order), Shop Pay Installments (banner placement, eligibility range $50–$3000) | sh-016 → sh-017 |

### Product Merchandising
| File | Covers | Key IDs |
|------|--------|---------|
| lore/29-shopify-product-merchandising.jsonl | Product variants (3 options max, deep linking, selectors, state management), product media (images, 3D, video), product recommendations (related vs complementary) | sh-018 |

### Navigation & Search
| File | Covers | Key IDs |
|------|--------|---------|
| lore/30-shopify-navigation-search.jsonl | Store navigation (menus, 3-level nesting, linklists), storefront search (query params, predictive search, sort, unavailable products), storefront filtering (sidebar, drawer, active filter chips, price range, availability) | sh-019 → sh-021 |

### Horizon Theme Design System (Reference Implementation)
| File | Covers | Key IDs |
|------|--------|---------|
| lore/31-shopify-horizon-design-system.jsonl | Horizon DS overview (web-native, server-rendered, block-first), token architecture (200+ CSS properties, Liquid-generated, settings-driven), colour system (scheme-based, brightness-aware opacity, RGB variants, static vs dynamic), typography system (4 font families, fluid clamp() scaling, auto-classification, independent heading config), spacing & layout (responsive scaling, gap system, flex-first, page width options), component architecture (127 blocks, 41 sections, private/public naming, snippet primitives), settings schema (full merchant config as variable source of truth) | sh-022 → sh-028 |

### Design Feasibility Review
| File | Covers | Key IDs |
|------|--------|---------|
| lore/32-shopify-design-feasibility.jsonl | Feasibility framework (Native / Liquid / Custom tiers + review process), filter & navigation feasibility (storefront filtering, price slider, swatches, sort, search, mega menu — each with tier, WHY, and implementation note), product & collection feasibility (quick view, infinite scroll, recently viewed, reviews, wishlist, bundles, variants, media — each classified), global & checkout feasibility (announcement bar, currency, loyalty, age gate, countdown timer, checkout limits, hard limits like 3-variant max and 16KB JS budget) | sh-029 → sh-032 |

### Developer Handoff
| File | Covers | Key IDs |
|------|--------|---------|
| lore/33-shopify-dev-handoff.jsonl | Figma frame → Shopify file mapping (naming conventions, layer hierarchy, template/section/block prefixes), settings schema annotation (all setting types, format, examples per section type, merchant config vs hardcoded decision guide), variant selector specs (type, all states, accessibility, colour swatch annotation, selling plan radio rules), metafield annotation (namespace.key format, all types, empty state rule, metafield definitions table), token naming & responsive breakpoints (full token catalogue, spacing scale, breakpoints 375/750/1200px, annotation practice), edge cases & Liquid conditionals (@if format, availability states, content edge cases, component variant naming), app block slots & final handoff checklist (where app blocks go, constraints, 20-point handoff checklist) | sh-033 → sh-039 |

---

## Quick Topic Routing

### Theme Design & Selling Plans
**"Shopify theme design principles / merchant experience"** → sh-001
**"Shopify customer experience / accessible / intuitive / cohesive"** → sh-002
**"Subscription product form / subscription pricing / selling plan price"** → sh-003
**"Selling plan selection / subscription radio / subscription options"** → sh-004
**"Subscription cart / selling plan name / multi-currency / subscription policy"** → sh-005
**"Pre-order / TBYB / try before you buy / deferred payment / deposit"** → sh-006
**"Pre-order cart / TBYB cart / checkout charge / pre-order naming"** → sh-007

### Theme Architecture
**"Shopify directory structure / theme files / hierarchy"** → sh-008
**"Shopify layout / theme.liquid / header footer"** → sh-009
**"Shopify templates / JSON vs Liquid / template types"** → sh-010
**"Shopify sections / schema / presets / section rendering"** → sh-011
**"Shopify blocks / theme blocks / section blocks / nesting"** → sh-012

### Best Practices
**"Shopify performance / Lighthouse / JavaScript / lazy-load / CDN"** → sh-013
**"Shopify accessibility / WCAG / keyboard / contrast / touch targets"** → sh-014
**"Sections blocks best practices / modularity / metafields"** → sh-015

### Pricing & Payments
**"Shopify discounts / strikethrough / cart discount / line item discount"** → sh-016
**"Shop Pay Installments / BNPL / payment terms banner"** → sh-017

### Product Merchandising
**"Product variants / options / swatches / selectors / media / recommendations"** → sh-018

### Navigation & Search
**"Shopify navigation / menus / header nav / mega menu"** → sh-019
**"Shopify search / predictive search / search results / sort"** → sh-020
**"Shopify filtering / storefront filters / price filter / sidebar filter"** → sh-021

### Design Feasibility Review
**"Can we build this in Shopify / is this doable / feasibility review"** → sh-029
**"Filter feasibility / price slider native / swatch filter / sort dropdown Shopify"** → sh-030
**"Quick view native / infinite scroll / recently viewed / wishlist Shopify"** → sh-031
**"Countdown timer / age gate / loyalty / checkout custom / Shopify hard limits"** → sh-032

### Developer Handoff
**"Figma to Shopify / frame mapping / section naming / dev handoff structure"** → sh-033
**"Settings schema annotation / @setting types / merchant config / handoff annotations"** → sh-034
**"Variant selector annotation / swatch spec / pill selector / subscription radio"** → sh-035
**"Metafield annotation / namespace key / metafield type / empty state"** → sh-036
**"Token naming / CSS custom properties / responsive breakpoints / Shopify breakpoints"** → sh-037
**"Edge cases / sold out state / no image / Liquid conditionals / component variants"** → sh-038
**"App block slots / app block constraints / handoff checklist / feasibility legend"** → sh-039

### Horizon Theme Design System
**"Horizon theme / Shopify flagship theme / reference implementation"** → sh-022
**"Shopify token architecture / CSS custom properties / Liquid tokens"** → sh-023
**"Shopify colour system / colour schemes / brightness detection / opacity"** → sh-024
**"Shopify typography / fluid type / clamp / 4 font families / heading config"** → sh-025
**"Shopify spacing / gap scale / responsive scaling / flex layout / page width"** → sh-026
**"Horizon blocks / block-first / component architecture / section vs block"** → sh-027
**"Shopify settings schema / merchant config / variables source of truth"** → sh-028

---

## Key Principles

- **Antifragile design**: Components must work with missing images, variable text, and placeholder content.
- **No price in strings**: Never hard-code prices in text — they break with currency switching and rounding.
- **Percentages over dollars**: Use percentage savings in selling plan names and descriptions.
- **Radio over buttons**: Selling plan selectors should be radio inputs — buttons compete with the main CTA.
- **Vertical stacking**: Selling plan groups stack vertically, never side-by-side on mobile.
- **Badge discipline**: Show subscription/pre-order badges only when there's a one-time alternative to differentiate from.
- **CTA reflects purchase type**: Button label must change to match the selected selling plan type.
- **16KB JS budget**: Theme JavaScript must stay under 16KB minified — design for CSS-first interactions.
- **44px touch targets**: All interactive elements must be at least 44×44px.
- **Three option max**: Products support max 3 options — design variant selectors accordingly.
- **Sections are independent**: No section should depend on adjacent sections for visual coherence.
- **Figma mirrors Shopify**: Layer structure should map 1:1 to Layout → Template → Section → Block hierarchy.
- **Settings schema = Figma variables**: The settings_schema.json IS the variable architecture — match it 1:1.
- **Block-first composition**: Horizon uses 127 blocks vs 41 sections — blocks are the primary unit, not sections.
- **Liquid-generated tokens**: Design tokens are dynamic, not static CSS — Figma variables must reflect this flexibility.
- **Brightness-aware colour**: Colour schemes auto-adjust opacity based on background brightness.
- **Fluid typography**: Sizes ≥3rem scale with clamp() — design for the range, not fixed values.
- **Feasibility tiers**: Every UI element is Native (zero code), Liquid (dev effort, no app), or Custom/App (significant effort or third-party). Always classify before presenting designs.
- **Checkout is locked**: Standard Shopify cannot customize the checkout layout or flow — requires Shopify Plus + Checkout Extensibility.
- **3 variant options max**: Products support maximum 3 options (e.g., Size + Color + Material). Cannot design around a 4th option natively.
- **16KB JS budget**: Every custom Liquid feature costs JS budget — design CSS-first, evaluate JS cost per feature.
- **Empty state mandatory**: Every Liquid-rendered element (metafield, image, reviews, description) must have a designed empty/absent state.
- **Annotations drive schema**: The settings_schema.json developers build is derived entirely from designer annotations — unannotated elements become mismatched merchant controls.
- **Token name = CSS variable**: Figma variable names must exactly match the CSS custom property names — one-to-one translation, no guessing.
- **App block slots, not app UI**: Designers provide the slot dimensions and constraints; app styling is app-controlled and cannot be guaranteed to match the design system.
- **Green/Amber/Red feasibility legend**: Use colour-coded annotations in every handoff file — green=Native, amber=Liquid, red=Custom/App.
