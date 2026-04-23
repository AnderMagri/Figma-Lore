# Design Lore

> A deep design knowledge base for Claude — available as persistent **Skills**
> (install once, works automatically) or as files you attach to any conversation.

Design Lore (formerly Figma Lore) started as a Figma-specific knowledge base
and has grown into a comprehensive **design intelligence library** split into
four focused skills for accurate triggering and clean separation of concerns.

---

## Four Skills, One Library

| Skill | ZIP | Modules | When it triggers |
|---|---|---|---|
| **figma-lore** | `figma-lore-skill.zip` | 00, 01, 03, 08, 09, 10 | Figma mechanics, auto layout, components, variants, slots, file structure, library management, audits, recipes |
| **design-lore** | `design-lore-skill.zip` | 02, 04–07, 11–21 | Design systems, tokens, colour, typography, iOS/Android specs, Gestalt, UX laws, art history, research, strategy, interaction, prototyping, ops, UX writing |
| **design-lore-psychology** | `design-lore-psychology-skill.zip` | 22 | Deep UX analysis, psychology, archetypes, theory-led audits, persuasion, phenomenology, semiotics |
| **design-lore-industry** | `design-lore-industry-skill.zip` | 23–24 | Shopify, ecommerce, conversion, crypto, Web3, DeFi, fintech, wallets, banking |

Install all four for complete coverage, or pick only the ones you need.

---

## What's Covered

### Figma Lore (Modules 00, 01, 03, 08–10)
- Figma core — frames, groups, layers, constraints, boolean ops, masks, export, shortcuts
- Auto layout — all sizing modes, padding, alignment, responsive patterns, wrap, min/max
- Components — variants, properties, slots, nesting, naming, architecture
- Organisation — file structure, library architecture, naming, versioning, governance, handoff
- Auditing — detached instances, hardcoded values, audit scripts, health scores
- Execution recipes — step-by-step guides for components, tokens, DS bootstrap, gotchas

### Design Lore (Modules 02, 04–07, 11–21)
- Design systems — token architecture, variables, theming, colour systems, multi-brand
- iOS design — HIG specs, safe areas, SF Pro, SF Symbols, touch targets
- Android / Material 3 — window classes, M3 components, tonal colour, navigation
- Responsive design — breakpoints, pixel density, constraint patterns
- Mobile UX — gestures, thumb zones, loading states, empty states, forms
- **Gestalt & Perception** — all 8 Gestalt laws, preattentive attributes, scanning patterns, heuristic evaluation
- **Typography Deep** — type anatomy, kerning, tracking, type scale, pairing, variable fonts, accessibility
- **Colour Theory** — HSL/HSB, harmonies, WCAG contrast, psychology by hue, dark mode, branding
- **Behavioural Design** — cognitive load, Hick's Law, Fitts's Law, anchoring, dark patterns, emotional design
- **Art History** — 38 art movements with UI applications (Bauhaus, Swiss Style, Vaporwave, Bento Grid, and more)
- **Design Research** — affinity diagrams, card sorting, empathy maps, JTBD, journey maps, usability testing
- **UX Strategy** — competitive analysis, design briefs, HEART framework, RICE, Kano, RACI
- **Interaction Design** — animation, error handling, gestures, loading states, micro-interactions, state machines
- **Prototyping & Testing** — A/B tests, accessibility testing, heuristic evaluation, wireframes, user flows
- **Design Ops** — critique, QA, sprints, handoff, version control
- **Designer Toolkit** — case studies, UX writing, data visualisation, presentations

### Psychology (Module 22)
- **Russian Activity Theory** — Vygotsky, Leontiev, Luria, Bakhtin, Engeström
- **Jungian Depth Psychology** — 12 archetypes, Shadow/Persona, collective unconscious
- **Phenomenology** — Husserl, Heidegger, Merleau-Ponty, Don Ihde
- **Semiotics** — Peirce, Saussure, Barthes
- **Psychoanalytic** — Freud, Lacan, Winnicott
- **Ecological & Motivational** — Gibson, Csikszentmihalyi, Deci & Ryan, Maslow
- **Existential** — Sartre & Kierkegaard
- **Narrative** — Campbell, Propp, Bateson
- **Persuasion & Power** — Lefebvre, Pavlov, Bernays, Cialdini, Sun Tzu, ethics spectrum

### Industry (Modules 23–24)
- **Ecommerce** — Shopify conversion benchmarks, product pages, ATC button, checkout, mobile commerce, trust signals, collection pages, app ecosystem
- **Crypto & Fintech** — wallet UX, seed phrases, exchange trading, DeFi, on/off-ramp, KYC, fintech dashboards, credit card UX, trust & security, error states, WalletConnect

#### Art Styles Covered
Classical: Renaissance, Baroque, Art Nouveau, Arts & Crafts, Bauhaus, De Stijl,
Constructivism, Art Deco, Swiss/International Style

Mid-century: Atomic Age, Space Age, Pop Art, Surrealism, Psychedelic/Acid,
1970s Folk, Punk/Zine, Memphis Group, Hyperrealism, Grunge/90s

Japanese & Digital Culture: Manga/Anime, Kawaii, Yami Kawaii, Vaporwave,
Cyberpunk, City Pop, Showa Retro, Contemporary Japanese aesthetics

Digital & UI Movements: Pixel Art, Glitch Art, Skeuomorphism, Flat Design,
Material Design, Neumorphism, Glassmorphism, Web Brutalism, Minimalism,
Retrowave/Synthwave, Maximalism, 3D Illustration, Neo-Brutalism, Bento Grid,
Biophilic/Organic Design

---

## Repo Structure

```
Figma-Lore/
│
├── README.md                              ← you are here
│
├── figma-lore-skill.zip                   ← Figma tool skill (modules 00,01,03,08–10)
├── design-lore-skill.zip                  ← design theory skill (modules 02,04–07,11–21)
├── design-lore-psychology-skill.zip       ← psychology skill (module 22)
├── design-lore-industry-skill.zip         ← industry skill (modules 23–24)
│
├── skill-figma/                           ← Figma tool mechanics
│   ├── SKILL.md
│   └── lore/
│       ├── 00-figma-core.jsonl
│       ├── 01-auto-layout.jsonl
│       ├── 03-components.jsonl
│       ├── 08-organization.jsonl
│       ├── 09-audit-optimization.jsonl
│       └── 10-execution-recipes.jsonl
│
├── skill-design/                                 ← Design theory & process
│   ├── SKILL.md
│   └── lore/
│       ├── 02-design-system.jsonl
│       ├── 04-ios-design.jsonl
│       ├── 05-android-design.jsonl
│       ├── 06-responsive.jsonl
│       ├── 07-mobile-ux.jsonl
│       ├── 11-gestalt-perception.jsonl
│       ├── 12-typography-deep.jsonl
│       ├── 13-colour-theory.jsonl
│       ├── 14-behavioural-design.jsonl
│       ├── 15-art-history-part1.jsonl
│       ├── 15-art-history-part2.jsonl
│       ├── 16-design-research.jsonl
│       ├── 17-ux-strategy.jsonl
│       ├── 18-interaction-design.jsonl
│       ├── 19-prototyping-testing.jsonl
│       ├── 20-design-ops.jsonl
│       └── 21-designer-toolkit.jsonl
│
├── skill-psychology/                      ← Deep UX psychology
│   ├── SKILL.md
│   └── lore/
│       └── 22-deep-ux-psychology.jsonl
│
└── skill-industry/                        ← Ecommerce & crypto/fintech
    ├── SKILL.md
    └── lore/
        ├── 23-ecommerce-ux.jsonl
        └── 24-crypto-fintech-ux.jsonl
```

---

## Installing the Skills

### Requirements
- Claude account on any plan (Free, Pro, Max, Team, or Enterprise)
- **Code execution** enabled: Settings → Capabilities → "Code execution and file creation"

### Option A — Use the pre-built ZIPs (easiest)

1. Download the ZIP(s) you want from this repo:
   - `figma-lore-skill.zip` — Figma mechanics (recommended for Figma users)
   - `design-lore-skill.zip` — design theory & process (recommended for everyone)
   - `design-lore-psychology-skill.zip` — deep psychology (optional)
   - `design-lore-industry-skill.zip` — ecommerce & crypto (optional)
2. Go to [claude.ai/customize/skills](https://claude.ai/customize/skills)
3. Click **"+"** → **"Upload a skill"** → upload each ZIP
4. Toggle the skill(s) **on**

### Option B — Build the ZIPs yourself

```bash
git clone https://github.com/AnderMagri/Figma-Lore.git
cd Figma-Lore

# Figma
cd skill-figma && zip -r ../figma-lore-skill.zip . && cd ..

# Design
cd skill && zip -r ../design-lore-skill.zip . && cd ..

# Psychology
cd skill-psychology && zip -r ../design-lore-psychology-skill.zip . && cd ..

# Industry
cd skill-industry && zip -r ../design-lore-industry-skill.zip . && cd ..
```

### Updating to a new version

```bash
git pull
cd skill-figma && zip -r ../figma-lore-skill.zip . && cd ..
cd skill && zip -r ../design-lore-skill.zip . && cd ..
cd skill-psychology && zip -r ../design-lore-psychology-skill.zip . && cd ..
cd skill-industry && zip -r ../design-lore-industry-skill.zip . && cd ..
```

In Claude: Customize → Skills → find each skill → delete → upload the new ZIP.

---

## Option C — Attach files directly (no install)

For one-off questions, attach individual `.jsonl` files directly to any Claude
conversation.

| I want help with… | Attach this file |
|---|---|
| Figma frames, shortcuts, export | `skill-figma/lore/00-figma-core.jsonl` |
| Auto layout | `skill-figma/lore/01-auto-layout.jsonl` |
| Components, variants, slots | `skill-figma/lore/03-components.jsonl` |
| File structure, libraries | `skill-figma/lore/08-organization.jsonl` |
| Design system audit | `skill-figma/lore/09-audit-optimization.jsonl` |
| Step-by-step recipes | `skill-figma/lore/10-execution-recipes.jsonl` |
| Design tokens, variables | `skill-design/lore/02-design-system.jsonl` |
| iOS specs / HIG | `skill-design/lore/04-ios-design.jsonl` |
| Material 3 / Android | `skill-design/lore/05-android-design.jsonl` |
| Responsive design | `skill-design/lore/06-responsive.jsonl` |
| Mobile UX, gestures, forms | `skill-design/lore/07-mobile-ux.jsonl` |
| Gestalt, visual hierarchy | `skill-design/lore/11-gestalt-perception.jsonl` |
| Typography theory | `skill-design/lore/12-typography-deep.jsonl` |
| Colour theory | `skill-design/lore/13-colour-theory.jsonl` |
| Cognitive bias, UX laws | `skill-design/lore/14-behavioural-design.jsonl` |
| Art styles, brand aesthetics | `skill-design/lore/15-art-history-part1.jsonl` + `skill-design/lore/15-art-history-part2.jsonl` |
| User research, personas | `skill-design/lore/16-design-research.jsonl` |
| UX strategy, metrics | `skill-design/lore/17-ux-strategy.jsonl` |
| Animation, gestures, loading | `skill-design/lore/18-interaction-design.jsonl` |
| A/B tests, usability, wireframes | `skill-design/lore/19-prototyping-testing.jsonl` |
| Critiques, sprints, handoff, QA | `skill-design/lore/20-design-ops.jsonl` |
| Case studies, UX writing | `skill-design/lore/21-designer-toolkit.jsonl` |
| Deep UX psychology, archetypes | `skill-psychology/lore/22-deep-ux-psychology.jsonl` |
| Shopify, ecommerce, conversion | `skill-industry/lore/23-ecommerce-ux.jsonl` |
| Crypto, fintech, wallets, DeFi | `skill-industry/lore/24-crypto-fintech-ux.jsonl` |

---

## Lore Entry Format

Each `.jsonl` file contains one JSON object per line:

```json
{
  "id": "gp-001",
  "topic": "gestalt-overview",
  "title": "Gestalt Psychology — The Foundation of Visual Perception",
  "content": "Full explanation with rules, values, and design guidance.",
  "tags": ["gestalt", "perception", "visual-design"],
  "source": "optional citation"
}
```

---

## Contributing

**Adding entries:** append to the relevant file, open a PR with a description
of what was added and why.

**Adding a module:** create the JSONL file in the appropriate skill directory,
add a row to the module index in that skill's `SKILL.md`, and update this README.

**Fixing errors:** open a PR and cite your source (Apple HIG, Material Design
docs, Figma release notes, NNG, etc.).

**Scope:** this lore is intentionally broad. Anything that makes a designer's
or design engineer's work better is in scope — Figma mechanics, psychology,
art history, typography, colour, platform specs, research, strategy, ops,
ecommerce, and fintech.

---

## Credits

Built from Figma documentation, Apple HIG, Google Material Design 3, Nielsen
Norman Group research, and community work including:

- Pavel Kiselev — colour system architecture (UX Collective)
- Figma 2025 release notes — slots, grid layout mode, variable fonts
- Nielsen & Molich (1990), NNG (Kate Moran & Kelley Gordon, 2023) — heuristic evaluation
- Colin Ware — preattentive attributes and information visualisation
- Don Norman — emotional design framework
- Thaler & Sunstein — nudge theory
- Josef Müller-Brockmann — grid systems and Swiss typography
- [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) — design research, UX strategy, interaction design, prototyping, design ops, and designer toolkit modules (MIT license)

---

*Maintained by [@AnderMagri](https://github.com/AnderMagri)*
