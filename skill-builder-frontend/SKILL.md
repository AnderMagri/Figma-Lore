---
name: frontend-engineer
description: >
  Learning companion and execution guide for a product designer becoming a frontend engineer.
  Assumes full design knowledge (systems, tokens, components, hierarchy, states) — never explains
  design concepts. Fills the gap between "I understand how it works" and "I can build it from scratch."
  Covers the engineering PROCESS: where to start, how to structure a project, what to do when stuck,
  and ready-to-use code patterns for common UI tasks. Use this skill whenever Ander is building
  a frontend project, writing React/HTML/CSS/TypeScript from scratch, structuring a component,
  or asking how to translate a design into working code. Also trigger for questions about project
  setup, file structure, build tools, Git workflow, or "how do I start building X".
---
# Frontend Engineer Skill
## For: Product designer with full design knowledge, building programming fluency
---
## Core Principle
You already know what good UI looks like and how it should behave. The gap is **process** —
how to start a blank file and end up with working code. This skill fills that gap.
Every response should:
1. Give the **process first** (what to do, in order)
2. Give the **pattern second** (the actual code to use)
3. Never explain design decisions — assume they're already made
---
## The Build Process (always follow this order)
### Starting a new project from scratch
```
1. Scaffold the project (Vite + React + TypeScript is the default)
2. Set up CSS variables / design tokens first
3. Build the layout shell (outermost container → sections → slots)
4. Add components one at a time, starting with the simplest
5. Wire up state only after the UI structure exists
6. Add interactions last (hover, focus, transitions)
```
Never start with data or logic. Always start with structure.
### Starting a new component from scratch
```
1. Write the HTML structure first — no styling yet
2. Add CSS classes (or Tailwind utilities) to make it look right
3. Make it accept props so it's reusable
4. Add state if it needs to change
5. Add event handlers last
```
---
## Project Setup
### Default stack (fastest to ship)
```bash
npm create vite@latest my-project -- --template react-ts
cd my-project
npm install
npm run dev
```
### File structure for a design-system-aware project
```
src/
├── tokens/
│   └── tokens.css          # All CSS variables (colors, spacing, type)
├── components/
│   ├── Button/
│   │   ├── Button.tsx
│   │   └── Button.module.css
│   └── ...
├── pages/ (or screens/)
├── hooks/                  # Reusable logic
├── utils/                  # Helper functions
└── App.tsx
```
### tokens.css pattern (map from Figma variables)
```css
:root {
  /* Primitives */
  --color-blue-500: #3B82F6;
  --color-gray-900: #111827;
  /* Semantics */
  --color-bg-primary: var(--color-gray-900);
  --color-action: var(--color-blue-500);
  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 40px;
  /* Typography */
  --font-body: 'Inter', sans-serif;
  --text-sm: 14px;
  --text-base: 16px;
  --text-lg: 20px;
  --text-xl: 24px;
}
```
---
## Core Patterns
### Pattern: React component (the template you always start with)
```tsx
interface ComponentNameProps {
  label: string;
  variant?: 'primary' | 'secondary';
  onClick?: () => void;
}
export function ComponentName({ label, variant = 'primary', onClick }: ComponentNameProps) {
  return (
    <button
      className={`btn btn--${variant}`}
      onClick={onClick}
    >
      {label}
    </button>
  );
}
```
### Pattern: State (for anything that changes)
```tsx
import { useState } from 'react';
const [isOpen, setIsOpen] = useState(false);
const toggle = () => setIsOpen(prev => !prev);
const [value, setValue] = useState('');
<input value={value} onChange={(e) => setValue(e.target.value)} />
const [selected, setSelected] = useState<string | null>(null);
```
### Pattern: List rendering
```tsx
const items = ['one', 'two', 'three'];
return (
  <ul>
    {items.map((item) => (
      <li key={item}>{item}</li>
    ))}
  </ul>
);
```
### Pattern: Conditional rendering
```tsx
{isOpen && <Modal />}
{isLoggedIn ? <Dashboard /> : <Login />}
<div className={`card ${isActive ? 'card--active' : ''}`}>
```
### Pattern: Fetch data from an API
```tsx
import { useState, useEffect } from 'react';
function MyComponent() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetch('https://api.example.com/data')
      .then(res => res.json())
      .then(json => {
        setData(json);
        setLoading(false);
      });
  }, []);
  if (loading) return <p>Loading...</p>;
  return <div>{JSON.stringify(data)}</div>;
}
```
### Pattern: CSS Layout
```css
.row { display: flex; align-items: center; gap: var(--space-md); }
.stack { display: flex; flex-direction: column; gap: var(--space-md); }
.row > :last-child { margin-left: auto; }
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--space-lg);
}
```
---
## When You're Stuck
- **"I don't know where to start"** → Write the HTML structure first. No CSS, no JS. Just the skeleton.
- **"My styles aren't applying"** → Check class name spelling, is the CSS file imported, open DevTools.
- **"My component isn't updating"** → Are you using useState? Don't mutate objects directly.
- **"I don't know what props to give a component"** → Think Figma properties. Each one that changes between instances is a prop.
- **"Prop or state?"** → Prop = comes from outside. State = lives inside.
---
## Git Workflow
```bash
git add .
git commit -m "describe what changed"
git push
```
Commit every time something works.
---
## Design-to-Code Translation
| Figma concept | Code equivalent |
|---|---|
| Auto Layout (row) | `display: flex; flex-direction: row` |
| Auto Layout (column) | `display: flex; flex-direction: column` |
| Fill container | `flex: 1` or `width: 100%` |
| Hug contents | default block/flex behavior |
| Component | React component function |
| Variant | prop (e.g. `variant="primary"`) |
| Boolean property | boolean prop (e.g. `isDisabled`) |
| Instance swap | children prop or slot pattern |
| Colour variable | CSS custom property |
| Text style | CSS class with font-size, line-height, font-weight |
---
## Reference Files
- `references/react-patterns.md` — forms, modals, context, custom hooks
- `references/css-patterns.md` — responsive, grid, animation, dark mode
- `references/typescript-for-designers.md` — only what you need for component work
