# Figma Lore

> A deep design knowledge base for Claude — available as a persistent **Skill**
> (install once, works automatically) or as files you attach to any conversation.

Figma Lore started as a Figma-specific knowledge base and has grown into a
broader **design intelligence library** covering Figma mechanics, design systems,
platform specs, visual perception, typography, colour theory, behavioural
psychology, and a full art history reference for aesthetic decision-making.

---

## What's Covered

### Figma & Systems (Modules 00–10)
- Figma core — frames, constraints, shortcuts, export, boolean ops
- Auto layout — all sizing modes, padding, alignment, responsive patterns
- Design tokens — three-layer architecture, variables, aliasing, theming
- Colour systems — Global → System → Component, light/dark mode, multi-brand
- Components — variants, properties, slots, nesting, naming, architecture
- iOS design — HIG specs, safe areas, SF Pro, SF Symbols, touch targets
- Android / Material 3 — window classes, M3 components, tonal colour, nav
- Responsive design — breakpoints, pixel density, constraint patterns
- Mobile UX — gestures, thumb zones, loading states, empty states, forms
- Design system governance — library structure, versioning, auditing, handoff
- Execution recipes — step-by-step guides for components, tokens, DS bootstrap

### Design Intelligence (Modules 11–15)
- **Gestalt & Perception** — all 8 Gestalt laws applied to UI, preattentive
  attributes, F/Z scanning patterns, heuristic evaluation methodology
- **Typography Deep** — type anatomy, classification, optical vs mechanical
  spacing, kerning, tracking, leading, type scale, measure, pairing, variable
  fonts, screen rendering, accessibility, design system type tokens
- **Colour Theory** — HSL/HSB, harmonies, temperature, WCAG contrast,
  simultaneous contrast, psychology by hue, palette construction, dark mode
  colour, light physics, branding, cultural colour context
- **Behavioural Design** — mental models, cognitive load, Hick's Law,
  Fitts's Law, Jakob's Law, Miller's Law, anchoring, Peak-End Rule, endowment
  effect, variable rewards, dark patterns, ethical nudges, emotional design
- **Art History & Aesthetics** — 38 art movements and aesthetic styles with
  specific UI/design applications for each (see full list below)

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

Plus: a framework entry (ah-038) for applying art history to real brand/UI decisions.

---

## Repo Structure

```
Figma-Lore/
│
├── README.md                      ← you are here
├── figma-lore-skill.zip           ← pre-built, ready to install
│
└── skill/                         ← Claude Skill package
    ├── SKILL.md                   ← skill definition and full module index
    └── lore/                      ← all knowledge modules
        ├── 00-figma-core.jsonl
        ├── 01-auto-layout.jsonl
        ├── 02-design-system.jsonl
        ├── 03-components.jsonl
        ├── 04-ios-design.jsonl
        ├── 05-android-design.jsonl
        ├── 06-responsive.jsonl
        ├── 07-mobile-ux.jsonl
        ├── 08-organization.jsonl
        ├── 09-audit-optimization.jsonl
        ├── 10-execution-recipes.jsonl
        ├── 11-gestalt-perception.jsonl
        ├── 12-typography-deep.jsonl
        ├── 13-colour-theory.jsonl
        ├── 14-behavioural-design.jsonl
        ├── 15-art-history-part1.jsonl
        └── 15-art-history-part2.jsonl
```

---

## Installing the Skill

### Requirements
- Claude account on any plan (Free, Pro, Max, Team, or Enterprise)
- **Code execution** enabled: Settings → Capabilities → "Code execution and file creation"

### Option A — Use the pre-built ZIP (easiest)

1. Download `figma-lore-skill.zip` from this repo
2. Go to [claude.ai/customize/skills](https://claude.ai/customize/skills)
3. Click **"+"** → **"Upload a skill"** → upload the ZIP
4. Toggle the skill **on**

Done. Claude now loads the relevant lore automatically for any Figma, design
system, typography, colour, or aesthetic question.

### Option B — Build the ZIP yourself

```bash
git clone https://github.com/AnderMagri/Figma-Lore.git
cd Figma-Lore/skill
zip -r ../figma-lore-skill.zip .
```

Then upload as above. The ZIP must have `SKILL.md` at the root — the `cd skill`
before zipping is what ensures this.

### Updating to a new version

```bash
git pull
cd skill && zip -r ../figma-lore-skill.zip . && cd ..
```

In Claude: Customize → Skills → find the skill → delete → upload the new ZIP.

---

## Option C — Attach files directly (no install)

For one-off questions, attach individual `.jsonl` files from `skill/lore/`
directly to any Claude conversation.

| I want help with… | Attach this file |
|---|---|
| Components, variants, slots | `03-components.jsonl` |
| Auto layout, responsive | `01-auto-layout.jsonl` |
| Design tokens, variables | `02-design-system.jsonl` |
| Colour systems, dark mode | `02-design-system.jsonl` + `13-colour-theory.jsonl` |
| iOS specs / HIG | `04-ios-design.jsonl` |
| Material 3 / Android | `05-android-design.jsonl` |
| Mobile UX, gestures, forms | `07-mobile-ux.jsonl` |
| Design system audit | `09-audit-optimization.jsonl` |
| Step-by-step recipes | `10-execution-recipes.jsonl` |
| Gestalt, visual hierarchy | `11-gestalt-perception.jsonl` |
| Typography theory | `12-typography-deep.jsonl` |
| Colour theory | `13-colour-theory.jsonl` |
| Cognitive bias, UX laws | `14-behavioural-design.jsonl` |
| Art styles, brand aesthetics | `15-art-history-part1.jsonl` + `15-art-history-part2.jsonl` |

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

**Adding entries:** append to the relevant file in `skill/lore/`, open a PR
with a description of what was added and why.

**Adding a module:** create `skill/lore/NN-name.jsonl`, add a row to the
module index in `skill/SKILL.md`, and update this README.

**Fixing errors:** open a PR and cite your source (Apple HIG, Material Design
docs, Figma release notes, NNG, etc.).

**Scope:** this lore is intentionally broad. Anything that makes a designer's
or design engineer's work better is in scope — Figma mechanics, psychology,
art history, typography, colour, platform specs.

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

---

*Maintained by [@AnderMagri](https://github.com/AnderMagri)*
