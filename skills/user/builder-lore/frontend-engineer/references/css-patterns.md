# CSS Patterns Reference
# Layout recipes, responsive patterns, animation, and dark mode.
## CSS Reset (paste at top of global CSS)
```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { -webkit-font-smoothing: antialiased; }
img, video { display: block; max-width: 100%; }
```
## Responsive Breakpoints (mobile-first)
```css
/* Base = mobile */
.container { padding: var(--space-md); }
/* Tablet */
@media (min-width: 768px) {
  .container { padding: var(--space-xl); }
}
/* Desktop */
@media (min-width: 1280px) {
  .container { max-width: 1200px; margin: 0 auto; }
}
```
## Page Layout with CSS Grid
```css
.page {
  display: grid;
  grid-template-rows: auto 1fr auto; /* header, main, footer */
  min-height: 100vh;
}
.sidebar-layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: var(--space-lg);
}
```
## Transitions
```css
/* Fade in */
.element {
  opacity: 0;
  transition: opacity 200ms ease;
}
.element.visible { opacity: 1; }
/* Slide up */
.card {
  transform: translateY(8px);
  opacity: 0;
  transition: transform 200ms ease, opacity 200ms ease;
}
.card.visible { transform: translateY(0); opacity: 1; }
```
## Dark Mode with CSS Variables
```css
:root {
  --color-bg: #ffffff;
  --color-text: #111827;
}
[data-theme='dark'] {
  --color-bg: #111827;
  --color-text: #f9fafb;
}
```
```tsx
// Toggle in React
document.documentElement.setAttribute('data-theme', 'dark');
```
## Z-index Scale
```css
:root {
  --z-base: 0;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-overlay: 300;
  --z-modal: 400;
  --z-toast: 500;
}
```
