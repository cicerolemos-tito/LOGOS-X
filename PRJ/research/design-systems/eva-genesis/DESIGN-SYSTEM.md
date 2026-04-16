---
name: eva-genesis
description: >-
  Canon-accurate Evangelion design system — 6 EVA unit themes, NERV HQ interfaces,
  MAGI voting, AT Field effects, Pattern Blue alerts, 15 components, 80+ OKLCH tokens.
  Updates and docs at myclaude.sh/p/eva-genesis
---

# EVA GENESIS PRO

> Canon-accurate Evangelion design system with 6 switchable unit themes, NERV HQ interface patterns, and 80+ OKLCH tokens forged from the real anime palette.

**Version:** 2.0.0
**Target Platforms:** Web
**Base Unit:** 4px
**Color Space:** OKLCH
**Author:** @darwim

---

## Design Philosophy

EVA GENESIS encodes the visual language of tactical command interfaces and biomechanical aesthetics. Every surface feels like a NERV terminal — dark, layered, urgent. Color is not decorative — it signals status, danger, and hierarchy. Typography is condensed and militant. Spacing is dense but never cramped. Shadows are deep and directional, like entry plug lighting.

This is not a "dark theme." This is a design system built around the tension between cold tactical precision and organic, almost biological warmth — the duality at the heart of Evangelion.

**Core values:**
1. **Canon Fidelity** — Colors sourced from the actual anime: Unit-01 purple (#765898) + green (#52d053), Unit-02 red (#d3290f), NERV orange (#FF9900), MAGI circuit patterns
2. **Narrative Friction** — Interfaces pulse, glitch, and overlap like real NERV HQ screens — designed for drama, not corporate calm
3. **Multi-Unit Theming** — Switch between 6 EVA unit palettes via a single CSS class. Same structure, different soul
4. **NERV HQ Interface System** — Orange text for primary info, green for grid/structure, cyan for data readouts — the canonical NERV display hierarchy

---

## Token Architecture

Three-layer system for maximum control:

**Layer 1 — Primitive Tokens:** Raw OKLCH values organized by hue family.
Example: `eva-purple-500: oklch(45% 0.28 300)`

**Layer 2 — Semantic Tokens:** Named by role, referencing primitives.
Example: `primary: $eva-purple-500`

**Layer 3 — Component Tokens:** Contextual overrides for specific components.
Example: `button-primary-bg: $primary`

Always use semantic tokens (Layer 2) in application code. Component tokens (Layer 3) exist in component specs only. Never reference primitives directly in UI code.

**Naming convention:** `kebab-case` for all tokens. Prefix `eva-` for primitives only.

---

## Color System

**Mode support:** Dark mode only — this system does not have a light mode. The darkness is the identity.

See `tokens/colors.yaml` for full token definitions.

### Palette Overview

**Brand — Unit-01 Default (switchable via themes):**
- `primary` — EVA Purple `oklch(42% 0.30 296)` — Canon Unit-01 body color. Used for: CTAs, active states, primary interactive elements
- `secondary` — Neon Green `oklch(72% 0.30 145)` — Canon Unit-01 accent stripes + eye glow. Used for: secondary actions, data visualization, sync indicators
- `accent` — NERV Orange `oklch(78% 0.22 65)` — Canon NERV HQ primary text color. Used for: highlights, labels, HUD readouts

**NERV Interface Colors (always available, theme-independent):**
- `nerv-text` — Orange `oklch(78% 0.22 65)` — Primary interface text (canon HQ screens)
- `nerv-grid` — Green `oklch(78% 0.30 142)` — Grid lines, structural elements
- `nerv-data` — Cyan `oklch(76% 0.16 200)` — Data readouts, timestamps, metrics

**Special Phenomena:**
- `at-field` — Orange `oklch(75% 0.20 60)` — AT Field barrier glow
- `berserk` — Red `oklch(55% 0.30 20)` — Berserk mode indicator
- `lcl` — Amber `oklch(72% 0.18 75)` — LCL fluid color
- `angel-core` — Red `oklch(50% 0.28 22)` — Angel core
- `pattern-blue` — Blue `oklch(62% 0.18 240)` — Angel detection signal

**Surface colors — Command Deck Layers:**
- `surface` — Deep void `oklch(8% 0.02 290)` — Main background, near-black with rich purple undertone
- `surface-raised` — Panel `oklch(12% 0.02 290)` — Cards, sidebars, elevated containers
- `surface-overlay` — Terminal `oklch(16% 0.03 290)` — Modals, drawers, command overlays
- `surface-input` — Plug depth `oklch(10% 0.02 290)` — Form inputs, sunken elements
- `surface-glass` — AT Field `oklch(14% 0.04 295 / 0.6)` — Glassmorphism overlays with purple tint

**Content colors — Readout Hierarchy:**
- `on-surface` — Primary text `oklch(92% 0.01 285)` — Cool white with faint purple cast
- `on-surface-muted` — Secondary `oklch(58% 0.02 285)` — Dimmed readout text
- `on-surface-disabled` — Ghost `oklch(32% 0.01 285)` — Inactive, decommissioned
- `border` — Grid line `oklch(20% 0.02 285)` — Subtle structural dividers
- `border-strong` — Cage frame `oklch(30% 0.03 300)` — Prominent borders with purple tint
- `border-focus` — Sync pulse `oklch(65% 0.28 300)` — Focus rings, bright EVA purple

**Status colors — MAGI System:**
- `success` — Sync OK `oklch(68% 0.18 155)` — Green, synchronization confirmed
- `warning` — Caution `oklch(78% 0.18 85)` — Amber, elevated threat level
- `error` — Angel Alert `oklch(58% 0.25 25)` — Red, critical — pattern blue detected
- `info` — MAGI Blue `oklch(62% 0.15 240)` — Analysis, computation, data

**Special — AT Field FX:**
- `glow-primary` — `oklch(52% 0.32 295)` — Intense purple glow for hover/active states
- `glow-secondary` — `oklch(78% 0.30 145)` — Neon green glow for terminal/data elements
- `glow-danger` — `oklch(58% 0.25 25)` — Red alert glow
- `glow-sync` — `oklch(72% 0.26 145)` — Green sync confirmation glow

---

## Typography Scale

See `tokens/typography.yaml` for full token definitions.

**Font stacks:**
- `font-display`: `'Orbitron', 'Rajdhani', 'system-ui', sans-serif` — Tactical headers, HUD elements
- `font-sans`: `'Geist Sans', 'Inter', 'system-ui', sans-serif` — Body text, UI elements
- `font-mono`: `'Geist Mono', 'JetBrains Mono', 'Consolas', monospace` — Data readouts, code, IDs, timestamps

**Scale — Dense tactical readout:**

| Step | Size | Line Height | Tracking | Use Case |
|------|------|-------------|----------|---------|
| `text-xs` | 0.6875rem (11px) | 1rem | 0.06em | Micro labels, status badges, timestamps |
| `text-sm` | 0.8125rem (13px) | 1.125rem | 0.03em | Secondary content, captions |
| `text-base` | 0.9375rem (15px) | 1.5rem | 0.01em | Body text — slightly dense |
| `text-lg` | 1.0625rem (17px) | 1.625rem | 0 | Large body, card titles |
| `text-xl` | 1.25rem (20px) | 1.75rem | -0.01em | Subheadings |
| `text-2xl` | 1.5rem (24px) | 1.875rem | -0.02em | Section headings |
| `text-3xl` | 2rem (32px) | 2.25rem | -0.03em | Page titles |
| `text-4xl` | 2.75rem (44px) | 3rem | -0.04em | Hero headings |
| `text-5xl` | 3.75rem (60px) | 1 | -0.05em | Display — NERV command headers |
| `text-6xl` | 5rem (80px) | 1 | -0.06em | Impact — full-bleed statements |

**Weights:** normal (400), medium (500), semibold (600), bold (700), black (900)

**Uppercase utility:** Headers at `text-3xl` and above use `uppercase` + `tracking-wider` by convention (not enforced — designer's choice).

---

## Spacing Scale

See `tokens/spacing.yaml` for full token definitions.

Base unit: 4px — Dense by default, like a NERV command terminal.

| Name | Value | Pixels | Use Case |
|------|-------|--------|---------|
| `space-0.5` | 0.125rem | 2px | Hairline gaps, icon-label |
| `space-1` | 0.25rem | 4px | Tight internal padding |
| `space-1.5` | 0.375rem | 6px | Badge padding |
| `space-2` | 0.5rem | 8px | Standard internal padding |
| `space-3` | 0.75rem | 12px | Form fields, compact cards |
| `space-4` | 1rem | 16px | Standard padding |
| `space-5` | 1.25rem | 20px | Card padding |
| `space-6` | 1.5rem | 24px | Section internal padding |
| `space-8` | 2rem | 32px | Between card groups |
| `space-10` | 2.5rem | 40px | Component separation |
| `space-12` | 3rem | 48px | Section gaps |
| `space-16` | 4rem | 64px | Major section breaks |
| `space-20` | 5rem | 80px | Hero padding |
| `space-24` | 6rem | 96px | Full section breathing room |
| `space-32` | 8rem | 128px | Page-level dramatic spacing |

---

## Shadow / Elevation System

See `tokens/shadows.yaml` for full token definitions.

Shadows in EVA GENESIS are heavy, directional, and tinted purple. They feel like depth in an entry plug — not subtle Material Design elevation.

| Level | Name | Value | Use Case |
|-------|------|-------|---------|
| 0 | `shadow-none` | `none` | Flat elements |
| 1 | `shadow-sm` | `0 1px 3px oklch(5% 0.02 285 / 0.5)` | Subtle lift — buttons at rest |
| 2 | `shadow-md` | `0 4px 12px oklch(5% 0.03 300 / 0.4), 0 1px 3px oklch(5% 0.02 285 / 0.3)` | Cards, panels |
| 3 | `shadow-lg` | `0 8px 32px oklch(5% 0.04 300 / 0.5), 0 2px 8px oklch(5% 0.02 285 / 0.3)` | Dropdowns, popovers |
| 4 | `shadow-xl` | `0 16px 48px oklch(5% 0.05 300 / 0.6), 0 4px 16px oklch(5% 0.03 285 / 0.4)` | Modals, command overlays |
| 5 | `shadow-glow` | `0 0 20px oklch(45% 0.28 300 / 0.4), 0 0 60px oklch(45% 0.28 300 / 0.15)` | AT Field glow — active/focus states |
| 6 | `shadow-glow-danger` | `0 0 20px oklch(58% 0.25 25 / 0.4), 0 0 60px oklch(58% 0.25 25 / 0.15)` | Angel alert glow |

---

## Motion System

See `tokens/motion.yaml` for full token definitions.

Motion in EVA GENESIS is **dramatic but purposeful** — entry plug startup sequences, not cartoon bounces.

**Philosophy:** `cinematic` — every animation should feel like it has weight and consequence.

**Easing curves:**
- `ease-nerv` — `cubic-bezier(0.16, 1, 0.3, 1)` — Primary easing, smooth deceleration (like MAGI processing)
- `ease-alert` — `cubic-bezier(0.68, -0.55, 0.27, 1.55)` — Overshoot for attention-grabbing elements
- `ease-deploy` — `cubic-bezier(0.25, 0.46, 0.45, 0.94)` — Measured deployment, entry plug insertion
- `ease-spring` — `cubic-bezier(0.34, 1.56, 0.64, 1)` — Energetic spring for micro-interactions

**Durations:**
- `duration-instant` — 100ms — Micro-feedback (button press)
- `duration-fast` — 200ms — Hover states, toggles
- `duration-normal` — 350ms — Panel transitions, card reveals
- `duration-slow` — 600ms — Page transitions, hero animations
- `duration-dramatic` — 1000ms — Full sequence reveals, AT Field materialization
- `duration-cinematic` — 1500ms — Staggered hero entrance, boot sequence

**Signature animations:**
- **AT Field Shimmer** — Subtle border-glow pulse on focus/active elements
- **Entry Plug Slide** — Elements slide in from below with scale(0.95→1) + opacity(0→1)
- **MAGI Boot** — Staggered letter-by-letter reveal for headings
- **Sync Pulse** — Rhythmic glow on status indicators
- **Pattern Blue** — Red alert flash for error states

---

## Export Instructions

### Available Exports

| Format | File | Use For |
|--------|------|---------|
| Tailwind CSS v4 | `exports/tailwind-preset.js` | Tailwind-based projects (primary) |
| CSS Variables | `exports/css-variables.css` | Vanilla CSS / non-Tailwind |
| DTCG JSON | `exports/dtcg.json` | Design tool integration (Figma Tokens, Style Dictionary) |

### Tailwind Installation

1. Copy `exports/tailwind-preset.js` to your project
2. In your CSS entry file:
   ```css
   @import "tailwindcss";
   @import './exports/css-variables.css';
   ```
3. In `tailwind.config.ts`:
   ```ts
   import evaPreset from './eva-genesis/exports/tailwind-preset'
   export default { presets: [evaPreset] }
   ```

### CSS Variables Installation

```css
@import './eva-genesis/exports/css-variables.css';
```

All tokens available as `var(--eva-*)` custom properties.

---

## How to Instruct Claude Code

Add this to your project's CLAUDE.md:

```markdown
## Design System: EVA GENESIS
All UI must use EVA GENESIS tokens from the design system.
- Colors: use semantic tokens from colors.yaml (NEVER raw hex/oklch — always token names)
- Typography: use text-* scale, font-display for headers, font-sans for body, font-mono for data
- Spacing: use space-* scale, base unit 4px
- Shadows: use shadow-* levels, shadow-glow for active states
- Motion: use Framer Motion with ease-nerv curve, entry-plug-slide for reveals
- Export target: Tailwind v4 preset
- Dark mode only — no light mode toggle needed
- Uppercase + tracking-wider for hero/display text (convention, not rule)
- AT Field glow (shadow-glow) on focus rings and active interactive elements
```

---

## Anti-Patterns


1. **Using light backgrounds** — This system has no light mode. A white background breaks every contrast ratio and visual hierarchy decision
2. **Raw color values in code** — Never write `oklch(45% 0.28 300)` in components. Use `primary`. The whole point of tokens is indirection
3. **Subtle shadows** — EVA GENESIS shadows are deliberately heavy and purple-tinted. Don't reduce opacity to make them "softer"
4. **Rounded corners > 12px** — This is a tactical, angular system. Max border-radius is 12px for large containers; default is 6px
5. **Decorative gradients** — Gradients are reserved for glow effects and AT Field FX. No rainbow gradients, no multi-color backgrounds
6. **Sans-serif for data** — Numbers, timestamps, IDs, code MUST use `font-mono`. This is non-negotiable
7. **Bounce/elastic animations** — The motion system is cinematic, not playful. No spring physics on page transitions
8. **Low-contrast text** — `on-surface-muted` is the MINIMUM contrast level for readable text. Never go below it
9. **Generic button styles** — Every button uses the shadow-glow on hover. No flat, unshadowed buttons
10. **Ignoring the glow system** — AT Field glow is the signature visual. Focus rings, active states, and hover all use it

---

## Quality Criteria


Before shipping UI built with EVA GENESIS, verify:
- [ ] No raw color values — all colors reference semantic tokens
- [ ] `font-display` used for headings, `font-sans` for body, `font-mono` for data
- [ ] Shadow-glow applied to interactive focus states
- [ ] All status colors use the correct semantic (success/warning/error/info)
- [ ] Spacing uses scale values only — no arbitrary pixel values
- [ ] Motion uses defined easing curves — no `ease-in-out` defaults
- [ ] Text contrast meets WCAG AA (4.5:1 for body, 3:1 for large text)
- [ ] Dark surfaces only — no white or near-white backgrounds
<!-- Published on MyClaude (myclaude.sh) | Quality: MCS-2 (100%) | Engine: Studio v2 -->
