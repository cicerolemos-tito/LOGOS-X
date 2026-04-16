# Component: AT Field Overlay

> The Absolute Terror Field — octagonal energy barriers that shimmer orange.
> Used as decorative overlays, loading states, and protection indicators.

## Variants

| Variant | Use Case | Visual |
|---------|---------|--------|
| `shield` | Active protection indicator | Pulsing octagonal border |
| `overlay` | Full-screen loading/transition | Expanding octagonal pattern |
| `badge` | Small inline AT indicator | Compact hexagonal icon with glow |

## CSS Pattern — Octagonal Clip

```css
/* AT Field octagonal shape */
.at-field-shape {
  clip-path: polygon(30% 0%, 70% 0%, 100% 30%, 100% 70%, 70% 100%, 30% 100%, 0% 70%, 0% 30%);
}
```

## Tailwind Usage

```html
<!-- AT Field Shield — wraps any content -->
<div class="relative p-[3px] rounded-xl
            bg-gradient-to-br from-at-field/60 via-transparent to-at-field/60
            shadow-[0_0_20px_oklch(75%_0.20_60/0.3),0_0_60px_oklch(75%_0.20_60/0.1)]
            animate-[at-field-shimmer_3s_ease-in-out_infinite]">
  <div class="bg-surface-raised rounded-[10px] p-5">
    <!-- Protected content here -->
    <div class="flex items-center gap-2 mb-3">
      <span class="h-2 w-2 rounded-full bg-at-field animate-pulse"></span>
      <span class="font-display text-[0.6875rem] uppercase tracking-[0.15em] font-bold text-at-field">
        AT Field Active
      </span>
    </div>
    <p class="text-sm text-on-surface-muted">
      Content protected by Absolute Terror Field barrier.
    </p>
  </div>
</div>

<!-- AT Field Loading State -->
<div class="flex flex-col items-center justify-center py-16">
  <!-- Octagonal ring -->
  <div class="relative h-20 w-20">
    <div class="absolute inset-0 border-2 border-at-field/40 rounded-lg rotate-45
                animate-[spin_4s_linear_infinite]"></div>
    <div class="absolute inset-2 border-2 border-at-field/60 rounded-lg rotate-[22.5deg]
                animate-[spin_3s_linear_infinite_reverse]"></div>
    <div class="absolute inset-4 border-2 border-at-field rounded-md rotate-45
                animate-[spin_2s_linear_infinite]
                shadow-[0_0_12px_oklch(75%_0.20_60/0.5)]"></div>
  </div>
  <span class="mt-6 font-display text-xs uppercase tracking-[0.2em] text-at-field font-bold">
    AT Field Deploying
  </span>
  <span class="mt-1 font-mono text-[0.6875rem] text-on-surface-muted tabular-nums">
    Output: 87.3%
  </span>
</div>

<!-- Compact AT Field Badge -->
<span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md
             bg-[oklch(15%_0.08_60)] border border-at-field/30
             shadow-[0_0_10px_oklch(75%_0.20_60/0.2)]">
  <span class="h-1.5 w-1.5 rounded-full bg-at-field animate-pulse"></span>
  <span class="font-mono text-[0.6875rem] text-at-field font-bold tabular-nums">
    AT FIELD: 142.7%
  </span>
</span>
```

## Framer Motion

```tsx
// AT Field shimmer on container
<motion.div
  animate={{
    boxShadow: [
      "0 0 20px oklch(75% 0.20 60 / 0.2)",
      "0 0 40px oklch(75% 0.20 60 / 0.4)",
      "0 0 20px oklch(75% 0.20 60 / 0.2)",
    ],
  }}
  transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
  className="p-[2px] rounded-xl bg-gradient-to-br from-at-field/40 to-at-field/40"
>
  <div className="bg-surface-raised rounded-[10px] p-5">
    {/* content */}
  </div>
</motion.div>
```
