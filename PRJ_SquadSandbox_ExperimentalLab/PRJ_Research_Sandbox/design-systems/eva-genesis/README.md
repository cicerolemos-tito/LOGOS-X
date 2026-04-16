# EVA GENESIS PRO

> Canon-accurate Evangelion design system — 6 switchable unit themes, NERV HQ interfaces, MAGI voting, AT Field effects, 15 components, 80+ OKLCH tokens.

## What It Does

EVA GENESIS PRO is a comprehensive design system forged from the actual Neon Genesis Evangelion anime palette. Every color is canon-sourced. Every component is NERV HQ-accurate. Includes:

- **80+ OKLCH color tokens** — 3-layer architecture with canon colors for Unit-01, Unit-02, Unit-00, Unit-03, Mark.06, plus NERV interface colors and special phenomena (AT Field, Berserk, LCL, Pattern Blue)
- **6 switchable themes** — Unit-01 (purple+green), Unit-02 (red+orange), Unit-00 (blue+gold), Unit-03 (black+crimson), Mark.06 (deep blue+yellow), NERV Terminal (orange+green)
- **15 component specs** — Button, Card, Input, Badge, Navigation, Modal, Table, Hero, Toast, Section, MAGI Vote, Sync Meter, Pattern Blue Alert, HUD Data, AT Field Overlay
- **5 token files** — Colors, typography (3 font stacks), spacing, shadows, motion (cinematic Framer Motion + AT Field + berserk + LCL animations)
- **4 export formats** — Tailwind v4 preset, CSS custom properties, DTCG JSON, Theme variants CSS
- **NERV interface system** — Orange text, green grid, cyan data — the canonical display hierarchy

## Installation

```bash
myclaude install eva-genesis
```

After installation, the design system is available at `myclaude-products/eva-genesis/`.

**Also compatible with:** Any [Agent Skills](https://agentskills.io)-compliant platform (Cursor, Codex, Gemini CLI, Copilot, and 30+ more).

## Usage

### With Tailwind v4

```ts
// tailwind.config.ts
import evaPreset from './eva-genesis/exports/tailwind-preset'
export default { presets: [evaPreset] }
```

### With CSS Variables

```css
@import './eva-genesis/exports/css-variables.css';
```

### With Claude Code

Add to your project's CLAUDE.md:

```markdown
## Design System: EVA GENESIS
Read tokens from eva-genesis/tokens/ before building any UI.
Colors: semantic tokens only (primary, surface, on-surface — never raw oklch).
Fonts: font-display for headers, font-sans for body, font-mono for data.
Motion: Framer Motion with ease-nerv curve.
Dark mode only — no light mode.
```

### Examples

See `examples/examples.md` for full implementation examples:
- NERV Dashboard card grid
- Command login form
- Framer Motion hero with stagger animation

## Token Architecture

```
Primitive → Semantic → Component
(raw values)  (role-based)  (context-specific)

void-950 → surface → card-background
eva-purple-500 → primary → button-primary-bg
```

Always reference **semantic tokens** in code. Never use primitives directly.

## Requirements

- Claude Code >= 1.0.0
- Tailwind CSS v4 (for preset export)
- Framer Motion (for motion tokens — recommended)
- Fonts: Orbitron (display), Geist Sans (body), Geist Mono (data)

---

**Version:** 2.0.0 | **License:** Proprietary | **Author:** @darwim

[![MCS 2](https://myclaude.sh/badge/mcs/2.svg)](https://myclaude.sh/quality) [![Available on MyClaude](https://myclaude.sh/badge/available.svg)](https://myclaude.sh/p/eva-genesis)

<sub>Quality-validated by [MyClaude Studio Engine](https://myclaude.sh/studio) | [Browse marketplace](https://myclaude.sh/explore)</sub>
