# Component: Button

> Every button in EVA GENESIS carries the AT Field glow signature on interaction.

## Variants

| Variant | Background | Text | Border | Glow on Hover |
|---------|-----------|------|--------|---------------|
| `primary` | `primary` | `primary-foreground` | none | `glow-primary` |
| `secondary` | `transparent` | `secondary` | `border-strong` | `glow-teal` |
| `accent` | `accent` | `accent-foreground` | none | `glow-accent` |
| `ghost` | `transparent` | `on-surface-muted` | none | `surface-hover` bg |
| `destructive` | `error` | `on-surface` | none | `glow-danger` |
| `outline` | `transparent` | `on-surface` | `border` | `surface-hover` bg + `border-strong` |

## States

| State | Transform | Notes |
|-------|----------|-------|
| Default | — | Base appearance |
| Hover | +shadow-glow variant, brightness +5% | AT Field shimmer begins |
| Focus | ring-focus (2px gap, 2px ring `border-focus`) | Visible keyboard focus |
| Active | scale(0.97), shadow-sm | Pressed — tactile feedback |
| Disabled | opacity 0.4, cursor not-allowed | No glow, no hover |
| Loading | spinner replaces text, opacity 0.7 | Pulse animation on background |

## Sizing

| Size | Padding | Font | Height | Border Radius |
|------|---------|------|--------|---------------|
| `xs` | 6px 10px | text-xs | 28px | radius-sm |
| `sm` | 8px 14px | text-sm | 32px | radius-md |
| `md` | 10px 18px | text-base | 40px | radius-md |
| `lg` | 12px 24px | text-lg | 48px | radius-md |
| `xl` | 16px 32px | text-xl | 56px | radius-lg |

## Tailwind Usage

```html
<!-- Primary -->
<button class="bg-primary text-primary-foreground px-[18px] py-2.5 text-[0.9375rem]
               font-medium rounded-md shadow-sm
               hover:shadow-[0_0_20px_oklch(45%_0.28_300/0.4)]
               hover:brightness-105
               active:scale-[0.97] active:shadow-sm
               focus-visible:ring-2 focus-visible:ring-eva-purple-400 focus-visible:ring-offset-2
               focus-visible:ring-offset-void-950
               disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:shadow-none
               transition-all duration-200">
  Deploy EVA
</button>

<!-- Ghost -->
<button class="bg-transparent text-on-surface-muted px-[18px] py-2.5 text-[0.9375rem]
               font-medium rounded-md
               hover:bg-surface-hover hover:text-on-surface
               active:scale-[0.97]
               transition-all duration-200">
  Cancel
</button>

<!-- Destructive -->
<button class="bg-error text-on-surface px-[18px] py-2.5 text-[0.9375rem]
               font-medium rounded-md shadow-sm
               hover:shadow-[0_0_20px_oklch(58%_0.25_25/0.4)]
               hover:brightness-110
               active:scale-[0.97]
               transition-all duration-200">
  Self Destruct
</button>
```

## Framer Motion

```tsx
<motion.button
  whileHover={{ scale: 1.02, boxShadow: "0 0 20px oklch(45% 0.28 300 / 0.4)" }}
  whileTap={{ scale: 0.97 }}
  transition={{ duration: 0.2, ease: [0.16, 1, 0.3, 1] }}
>
  Deploy EVA
</motion.button>
```
