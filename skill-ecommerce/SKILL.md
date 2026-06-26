---
name: ecommerce-lore
description: >
  General ecommerce UX knowledge base. Platform-agnostic conversion benchmarks,
  product page anatomy, ATC button UX, checkout flow & abandonment, conversion
  psychology (Cialdini applied), mobile commerce (thumb zones, touch targets,
  sticky ATC), page section architecture, trust signals hierarchy, collection
  page UX (filtering, grid, breadcrumbs), performance (Core Web Vitals),
  responsive breakpoints, Figma grid setup, product card dimensions,
  mobile/desktop frame setup, app ecosystem, and design system readiness.
  Trigger for ecommerce, conversion, CRO, product pages, checkout,
  ATC, collection pages, trust signals, or mobile commerce questions.
  For Shopify platform-specific knowledge (Liquid, selling plans, theme
  architecture), use **shopify-lore**.
---

# Ecommerce Lore

General ecommerce UX patterns, conversion data, and empirical design
knowledge — applicable across Shopify, WooCommerce, headless, and
any storefront platform.

> **Part of the Design Lore family.** This module covers general ecommerce UX.
> For Shopify platform-specific knowledge (theme architecture, Liquid, selling
> plans, subscriptions, preorders), use **shopify-lore**. For crypto/fintech
> UX, use **design-lore-industry**.

## How to Use This Skill

1. Identify the relevant entry from the index below
2. Read the applicable JSONL entries
3. Cross-reference with shopify-lore for platform-specific implementation
4. Apply audit flags at the end of each entry to check for common failures

---

## Module Index

### Ecommerce UX
| File | Covers | Key IDs |
|------|--------|---------|
| lore/23-ecommerce-ux.jsonl | Conversion benchmarks, product page anatomy, ATC button UX, checkout flow & abandonment, conversion psychology (Cialdini applied), mobile commerce (thumb zones, touch targets), page section architecture, trust signals hierarchy, collection page UX (filtering, grid, breadcrumbs), page performance (Core Web Vitals), breakpoints, Figma grid setup per breakpoint (390/768/1440), product card pixel dimensions, mobile frame setup (header/safe area/sticky ATC), desktop frame setup (1440px frame / 1200px container), app ecosystem, DS readiness checklist | ec-001 → ec-016 |

---

## Quick Topic Routing

**"Ecommerce conversion / CRO / benchmarks"** → lore/23-ecommerce-ux.jsonl (ec-001)
**"Product page / product detail page"** → lore/23-ecommerce-ux.jsonl (ec-002)
**"Add to cart button / ATC UX"** → lore/23-ecommerce-ux.jsonl (ec-003)
**"Checkout flow / cart abandonment"** → lore/23-ecommerce-ux.jsonl (ec-004)
**"Conversion psychology / social proof / scarcity"** → lore/23-ecommerce-ux.jsonl (ec-005)
**"Mobile commerce / mobile shopping"** → lore/23-ecommerce-ux.jsonl (ec-006)
**"Page architecture / section order / homepage"** → lore/23-ecommerce-ux.jsonl (ec-007)
**"Trust signals / reviews / ecommerce trust"** → lore/23-ecommerce-ux.jsonl (ec-008)
**"Collection page / product grid / filtering"** → lore/23-ecommerce-ux.jsonl (ec-009)
**"Page performance / page speed / Core Web Vitals"** → lore/23-ecommerce-ux.jsonl (ec-010)
**"Breakpoints / responsive / 750px"** → lore/23-ecommerce-ux.jsonl (ec-011)
**"Grid / Figma columns / product card sizes"** → lore/23-ecommerce-ux.jsonl (ec-012)
**"Mobile frame / header / safe area / sticky ATC"** → lore/23-ecommerce-ux.jsonl (ec-013)
**"Desktop frame / 1440px / 1200px container"** → lore/23-ecommerce-ux.jsonl (ec-014)
**"Design system checklist / DS readiness"** → lore/23-ecommerce-ux.jsonl (ec-015)
**"Apps / app ecosystem / reviews app / Klaviyo / page builder"** → lore/23-ecommerce-ux.jsonl (ec-016)

---

## Key Principles

- **Trust before conversion**: Trust signals must precede any conversion ask.
- **Mobile-first, always**: 60–70% of ecommerce traffic is mobile — design there first.
- **Fees before commitment**: Never surprise users with costs after they've committed.
- **Script budget**: Every third-party script adds weight — 5–6 frontend scripts max before performance degrades.
- **Design for real stores**: Account for installed apps, widgets, and their overlap — not idealised mockups.
