# Design Lore

> A deep design knowledge base for Claude — available as persistent **Skills**
> (install once, works automatically) or as files you attach to any conversation.

Design Lore (formerly Figma Lore) started as a Figma-specific knowledge base
and has grown into a comprehensive **design intelligence library** split into
focused skills for accurate triggering and clean separation of concerns.

---

## The Skill Family

| Skill | Package | Covers |
|---|---|---|
| **figma-lore** | `skill-figma.skill` | Figma mechanics, components, variants, slots, file structure, library management, audits, recipes |
| **figma-autolayout-lore** | `skill-figma-autolayout.skill` | Auto layout in depth, advanced patterns, component recipes |
| **figma-prototyping-lore** | `skill-figma-prototyping.skill` | Prototyping interaction model, Smart Animate, transitions, easing and springs, variables and conditionals, Figma Motion timeline, motion systems, build recipes |
| **design-lore** | `skill-design.skill` | Design systems, tokens, colour, typography, iOS/Android specs, Gestalt, UX laws, art history, research, strategy, interaction, prototyping, ops, UX writing |
| **design-system-lore** | `skill-design-system.skill` | Token architecture, colour systems, naming conventions, governance |
| **layout-lore** | `skill-layout.skill` | Grids, measure, whitespace, alignment, responsive strategy, section rhythm, page archetypes |
| **design-critique-lore** | `skill-critique.skill` | Heuristic evaluation, critique rubrics per dimension, critique practice and defending decisions |
| **ai-ux-lore** | `skill-ai-ux.skill` | Agentic experience design, trust calibration, AI persona and voice, evaluation, agent orchestration, prompt architecture |
| **design-lore-psychology** | `skill-psychology.skill` | Deep UX psychology, archetypes, theory-led audits, persuasion, phenomenology, semiotics |
| **ecommerce-lore** | `skill-ecommerce.skill` | Ecommerce UX, conversion benchmarks, CRO |
| **shopify-lore** | `skill-shopify.skill` | Shopify theme architecture, Horizon, design feasibility, dev handoff |
| **design-lore-industry** | `skill-industry.skill` | Crypto, Web3, DeFi, fintech, wallets, banking |
| **frontend-builder-lore** | `skill-builder-frontend.skill` | Frontend engineering builder lore |
| **fde-builder-lore** | `skill-builder-fde.skill` | Forward-deployed engineering builder lore |

Install all of them for complete coverage, or pick only the ones you need.

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

### Figma Prototyping (Modules 34–39)
- **Prototyping core** — the interaction model, flows and starting points, all 12 triggers, all 15 actions, overlays (positions, scrim, dismissal, swap vs open), scroll/overflow/fixed/sticky, preserve scroll position, device and presentation settings, hotspot craft, fidelity ladder, testing with prototypes, accessibility limits, handoff, QA checklist
- **Transitions & Smart Animate** — every transition type and what it means, Smart Animate matching rules and supported/unsupported properties, all eight easing presets, all spring presets with stiffness/damping/mass, duration craft, choreography and stagger, platform motion conventions, debugging
- **Advanced prototyping** — variables (all four types), Set variable, the complete expression syntax, conditionals, variable modes for theming and locale, interactive components and state behaviour, real text input, state modelling, and where the ceiling is
- **Figma Motion** — the native timeline, keyframes and auto-keyframing, animation styles, animated components, motion variables, export formats, Dev Mode handoff, the `figma.motion` Plugin API, Figma Sites interactions, motion review
- **Motion systems** — duration and easing tokens, reduced-motion policy, performance (what is cheap and what janks), CSS / motion.dev code mapping, motion spec templates, motion personality by domain
- **Recipes** — bottom sheets, toasts, Shopify PDP variant pickers, cart drawers, filter panels, multi-step forms with validation, wallet connect and signing flows, AI latency and failure states, live theme toggles, skeleton loading, and state inventories

### Layout (Module 43)
- Layout first principles, grid systems and their parameters per breakpoint, measure and vertical rhythm, whitespace as micro/macro/active, alignment and optical correction, responsive strategy (seven reflow behaviours), above-the-fold decisions, section rhythm for long pages
- **Page archetypes** with full anatomy and pitfalls — landing pages, product detail pages, collection and search results, dashboards and data views, forms and multi-step flows, application shells and navigation
- Layout anti-patterns and how to specify a layout that survives implementation

### Design Critique (Modules 40–42)
- **Heuristic evaluation** — each of Nielsen's 10 in depth with failure modes, checking methods and domain specifics; severity ratings; the full protocol; finding and report formats; Shneiderman, Gerhardt-Powals, Tognazzini, WCAG-as-heuristics and HEART; dedicated heuristic sets for AI, ecommerce/Shopify, crypto/fintech and accessibility; running an evaluation on a Figma file
- **Critique rubrics** — the standard pass, then observation / problem / fix rubrics rated pass / minor / major for composition, visual hierarchy, typography, colour, spacing, information density, affordance, copy, brand consistency, responsive behaviour, state completeness, task efficiency, data display and motion
- **Critique practice** — facilitation, feedback language, design rationale, red-teaming your own assumptions, pre-mortems, defending decisions without being defensive, framing design in product and metric terms, reviewing AI-generated work, review cadence, self-critique techniques

### AI UX (Modules 44–48)
- **AI interaction design** — what changes when the system is probabilistic, mixed-initiative flow and control handoffs, capability discoverability, latency and streaming as designed states, correction loops and editability, generative UI, context and memory visibility, frustration repair
- **Trust and alignment** — trust calibration and its five failure modes, the stakes × confidence language matrix, transparency and citation patterns, guardrail and refusal design, consent and agency, harm anticipation, escalation, bias in AI interfaces
- **Behaviour and evaluation** — persona architecture, tone calibration, error personality, behavioural consistency, failure taxonomies, output quality rubrics, AI metrics that mean something
- **Agent orchestration** — agent roles, task decomposition, handoff protocols, human-in-the-loop checkpoints, state and observability, failure recovery, agentic anti-patterns
- **Prompt architecture** — the prompt as a design surface, system prompt structure, constraint specification, examples and few-shot, context engineering, reasoning structure, prompt versioning

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
Skill-stack/
│
├── README.md                       ← you are here
├── INDEX.tsv                       ← every entry, greppable (see below)
├── lore.py                         ← index / get / search / validate
├── repackage-skills.py             ← PostToolUse hook: reindexes + rebuilds .skill
│
├── skill-figma/                    → figma-lore
│   └── lore/  00, 01, 03, 08, 09, 10
├── skill-figma-autolayout/         → figma-autolayout-lore
│   └── lore/  01, 01b, 01c
├── skill-figma-prototyping/        → figma-prototyping-lore
│   └── lore/  34 prototyping-core, 35 transitions-motion,
│              36 advanced-prototyping, 37 figma-motion,
│              38 motion-system-handoff, 39 prototype-recipes
├── skill-design/                   → design-lore
│   └── lore/  02, 04–07, 11–21
├── skill-design-system/            → design-system-lore
├── skill-layout/                   → layout-lore
│   └── lore/  43 layout-systems
├── skill-critique/                 → design-critique-lore
│   └── lore/  40 heuristic-evaluation, 41 critique-rubrics,
│              42 critique-practice
├── skill-ai-ux/                    → ai-ux-lore
│   └── lore/  44 ai-interaction-design, 45 ai-trust-alignment,
│              46 ai-behaviour-evaluation, 47 ai-agent-orchestration,
│              48 ai-prompt-architecture
├── skill-psychology/               → design-lore-psychology
├── skill-ecommerce/                → ecommerce-lore
├── skill-shopify/                  → shopify-lore
├── skill-industry/                 → design-lore-industry
├── skill-builder-frontend/         → frontend-builder-lore
└── skill-builder-fde/              → fde-builder-lore
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
| Figma prototyping mechanics, triggers, actions, overlays | `skill-figma-prototyping/lore/34-figma-prototyping-core.jsonl` |
| Smart Animate, transitions, easing, springs | `skill-figma-prototyping/lore/35-figma-transitions-motion.jsonl` |
| Prototype variables, conditionals, expressions | `skill-figma-prototyping/lore/36-figma-advanced-prototyping.jsonl` |
| Figma Motion timeline, keyframes, motion API | `skill-figma-prototyping/lore/37-figma-motion.jsonl` |
| Motion tokens, reduced motion, motion handoff | `skill-figma-prototyping/lore/38-motion-system-handoff.jsonl` |
| Step-by-step prototype recipes | `skill-figma-prototyping/lore/39-prototype-recipes.jsonl` |
| Heuristic evaluation, severity, protocol | `skill-critique/lore/40-heuristic-evaluation.jsonl` |
| Critique rubrics per dimension | `skill-critique/lore/41-critique-rubrics.jsonl` |
| Critique facilitation, rationale, defending decisions | `skill-critique/lore/42-critique-practice.jsonl` |
| Grids, measure, whitespace, page archetypes | `skill-layout/lore/43-layout-systems.jsonl` |
| AI interaction design, latency, correction loops | `skill-ai-ux/lore/44-ai-interaction-design.jsonl` |
| AI trust, transparency, refusal, harm | `skill-ai-ux/lore/45-ai-trust-alignment.jsonl` |
| AI persona, voice, failure taxonomy, metrics | `skill-ai-ux/lore/46-ai-behaviour-evaluation.jsonl` |
| Agent roles, handoffs, human-in-the-loop | `skill-ai-ux/lore/47-ai-agent-orchestration.jsonl` |
| Prompt architecture as design | `skill-ai-ux/lore/48-ai-prompt-architecture.jsonl` |
| Deep UX psychology, archetypes | `skill-psychology/lore/22-deep-ux-psychology.jsonl` |
| Shopify, ecommerce, conversion | `skill-industry/lore/23-ecommerce-ux.jsonl` |
| Crypto, fintech, wallets, DeFi | `skill-industry/lore/24-crypto-fintech-ux.jsonl` |

---

## Lore Entry Format

Every entry in every module uses the same schema — one JSON object per line:

```json
{
  "id": "gp-001",
  "topic": "gestalt-overview",
  "title": "Gestalt Psychology — The Foundation of Visual Perception",
  "content": "Full explanation with rules, values, and design guidance.",
  "tags": ["gestalt", "perception", "visual-design"],
  "source": "optional citation",
  "meta": { "optional": "hard numbers — specs, dp/pt values, ratios" }
}
```

`id`, `topic`, `title`, `content` and `tags` are required. `source`, `example`
and `meta` are optional. `meta` is where the hard numbers live (iOS safe-area
insets, Material dp values, WCAG ratios, type scales) and is searchable.

---

## Finding Things — INDEX.tsv and lore.py

The corpus is ~1,000 entries / ~285k tokens across 59 files. Reading a whole
module to find one fact costs 6–16k tokens, so every entry is indexed.

- **`INDEX.tsv`** (repo root) — one tab-separated line per entry across all
  skills: `id · prefix · skill · file · title · topic · tags`. Grep it, then
  read only the entries it names.
- **`skill-*/INDEX.tsv`** — the same thing scoped to one skill, shipped inside
  each `.skill` package so an installed skill is greppable too.

Both are regenerated automatically by the packaging hook. To do it by hand:

```bash
python3 lore.py index
```

`lore.py` also fetches and searches without reading whole files:

```bash
python3 lore.py get fp-012 ms-004          # print full entries by id
python3 lore.py search "reduced motion"    # one line per match
python3 lore.py search "44x44" -f meta     # search the hard numbers
python3 lore.py search "spring" -s figma-prototyping
python3 lore.py show "focus state" -n 3    # full content of matches
python3 lore.py validate                   # schema, id/prefix collisions, stale ranges
```

`validate` is the guardrail worth running before any commit. It checks that
every entry has the required fields, that no two unrelated modules share an id
or an overlapping id range, that each `SKILL.md` module index matches what is
actually on disk, and that the indexes are not stale. Modules deliberately
mirrored between skills are reported as such rather than flagged.


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
- [Owl-Listener/ai-design-skills](https://github.com/Owl-Listener/ai-design-skills) — the agentic-experience-design framing and source material for the AI UX modules 44–48 (MIT license)
- [phuryn/pm-skills](https://github.com/phuryn/pm-skills) — the strategy red-team method, pre-mortem structure, and prioritisation framework references in module 42 (MIT license)
- [Infrasity-Labs/dev-gtm-claude-skills](https://github.com/Infrasity-Labs/dev-gtm-claude-skills) — critique-dimension structure and motion-system token approach (MIT license)
- Figma Help Center and Figma Developer Docs — prototyping triggers and actions, Smart Animate, easing and spring presets, expressions, variable modes, Figma Motion, and the `figma.motion` Plugin API
- Ben Shneiderman — Eight Golden Rules; Gerhardt-Powals (1996) — cognitive engineering principles; Bruce Tognazzini — First Principles
- Gary Klein (2007) — pre-mortem / prospective hindsight
- Lee & See (2004) — appropriate reliance and calibrated trust
- Dan Olsen — Opportunity Score (*The Lean Product Playbook*)

---

*Maintained by [@AnderMagri](https://github.com/AnderMagri)*
