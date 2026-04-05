# Component: Card

> Elevated panels on the command deck — information containers with depth.

## Variants

| Variant | Background | Border | Shadow | Use Case |
|---------|-----------|--------|--------|---------|
| `default` | `surface-raised` | `border` | `shadow-md` | Standard content container |
| `glass` | `surface-glass` | `border-strong` | `shadow-md` + backdrop-blur | AT Field overlay, featured content |
| `interactive` | `surface-raised` | `border` | `shadow-md` → `shadow-lg` on hover | Clickable cards, links |
| `inset` | `surface-input` | `border` | `inset-sm` | Sunken panels, input groups |
| `status` | status surface variant | status border | `shadow-md` | Alert cards, notifications |
| `hero` | `surface-raised` | `border-strong` | `shadow-xl` + glow | Featured/highlighted content |

## States (Interactive variant)

| State | Transform | Notes |
|-------|----------|-------|
| Default | shadow-md | Base elevation |
| Hover | shadow-lg, border-strong, translateY(-2px) | Lifts off the deck |
| Focus | ring-focus | Keyboard navigation |
| Active | shadow-sm, translateY(0) | Pressed down |

## Structure

```
┌──────────────────────────────────┐
│  Card Header (optional)          │  ← space-4 padding, border-b
│  Title + subtitle + actions      │
├──────────────────────────────────┤
│                                  │
│  Card Body                       │  ← space-5 padding
│  Main content area               │
│                                  │
├──────────────────────────────────┤
│  Card Footer (optional)          │  ← space-4 padding, border-t
│  Actions, metadata               │
└──────────────────────────────────┘
```

## Tailwind Usage

```html
<!-- Default Card -->
<div class="bg-surface-raised border border-border rounded-lg shadow-md p-5">
  <h3 class="font-display text-xl font-bold uppercase tracking-wide text-on-surface">
    EVA Unit-01
  </h3>
  <p class="mt-2 text-on-surface-muted text-base">
    Synchronization rate: 94.2%
  </p>
</div>

<!-- Glass Card (AT Field) -->
<div class="bg-[oklch(14%_0.03_300/0.6)] backdrop-blur-xl
            border border-border-strong rounded-lg shadow-md p-5">
  <h3 class="font-display text-xl font-bold uppercase tracking-wide text-on-surface">
    AT Field Status
  </h3>
  <p class="mt-2 text-secondary font-mono text-sm tabular-nums">
    Output: 142.7%
  </p>
</div>

<!-- Interactive Card -->
<div class="bg-surface-raised border border-border rounded-lg shadow-md p-5
            hover:shadow-lg hover:border-border-strong hover:-translate-y-0.5
            active:shadow-sm active:translate-y-0
            transition-all duration-200 cursor-pointer">
  <!-- content -->
</div>
```

## Framer Motion

```tsx
<motion.div
  className="bg-surface-raised border border-border rounded-lg shadow-md p-5"
  whileHover={{ y: -4, boxShadow: "0 8px 32px oklch(5% 0.04 300 / 0.5)" }}
  whileTap={{ y: 0, boxShadow: "0 1px 3px oklch(5% 0.02 285 / 0.5)" }}
  transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
>
  {/* content */}
</motion.div>
```
