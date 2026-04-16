# EVA GENESIS — Usage Guidelines

## Do

- **Always use semantic tokens** — `primary`, `surface`, `on-surface`, not `eva-purple-500` or `void-950`
- **Use `font-display` for headings** — Orbitron gives the tactical HUD feel. Sans is for body only
- **Use `font-mono` for all data** — Numbers, percentages, timestamps, IDs, code. Non-negotiable
- **Apply AT Field glow on focus** — `shadow-glow` or `ring-focus` on every interactive element
- **Use uppercase + tracking-wider** for display text (text-3xl and above, section labels, badges)
- **Use the status color system** — success/warning/error/info have matching surface + foreground tokens
- **Keep spacing dense** — This is a command terminal, not a marketing site. Use space-2 to space-4 for internal padding
- **Use Framer Motion** — The motion tokens are designed for Framer Motion variants, not CSS animations
- **Apply `tabular-nums`** to any numeric data display for alignment
- **Use `backdrop-blur-xl`** with `surface-glass` for AT Field overlay effects

## Don't

- **Don't use light backgrounds** — Ever. Not white, not near-white, not light gray
- **Don't use default Tailwind grays** — Use the `void-*` scale which has purple undertones
- **Don't skip the glow** — Plain borders without glow look like a different design system
- **Don't use border-radius > 12px** — Exception: `radius-full` for pills and avatars only
- **Don't use casual/playful animations** — No bounce, no jiggle, no confetti. This is NERV, not a toy
- **Don't use `ease-in-out`** — Use `ease-nerv` (the custom cubic-bezier) for all transitions
- **Don't mix font stacks** — Display for headers, sans for body, mono for data. No exceptions
- **Don't create new color tokens ad-hoc** — If a token doesn't exist, you don't need it
- **Don't use opacity < 0.4 for disabled states** — Below that, elements become invisible on dark backgrounds
- **Don't forget reduced motion** — All animations must degrade to simple opacity fades
