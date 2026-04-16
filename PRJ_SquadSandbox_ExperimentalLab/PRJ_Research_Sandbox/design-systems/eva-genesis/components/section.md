# Component: Section

> Page-level content blocks — consistent padding, optional dividers.

## Variants

| Variant | Background | Padding | Notes |
|---------|-----------|---------|-------|
| `default` | `surface` | py-16 md:py-24 | Standard section |
| `raised` | `surface-raised` | py-16 md:py-24 | Alternating sections |
| `hero` | `surface` | py-24 md:py-32 | Hero/feature sections |
| `compact` | `surface` | py-8 md:py-12 | Dense info blocks |
| `glass` | `surface-glass` | py-16 md:py-24 | AT Field overlay section |

## Structure

```
┌──────────────────────────────────────────────────────────┐
│                                                          │  ← py-16/24
│  ┌──── Container (max-w-7xl, mx-auto, px-6) ────────┐  │
│  │                                                    │  │
│  │  [Section Label]     ← text-xs, uppercase, accent  │  │
│  │  Section Heading     ← text-3xl/4xl, font-display  │  │
│  │  Description         ← text-lg, on-surface-muted   │  │
│  │                                                    │  │
│  │  [Content Grid / Cards / Feature List]             │  │
│  │                                                    │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Section Header Pattern

```html
<div class="max-w-2xl">
  <span class="text-[0.6875rem] uppercase tracking-widest font-semibold text-accent">
    EVA Units
  </span>
  <h2 class="mt-3 font-display text-3xl md:text-4xl font-bold uppercase tracking-wide text-on-surface">
    The Children
  </h2>
  <p class="mt-4 text-lg text-on-surface-muted leading-relaxed">
    Three pilots. Three Evangelion units. One mission.
  </p>
</div>
```

## Grid Patterns

```html
<!-- 3-column feature grid -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
  <!-- Cards here -->
</div>

<!-- 2-column split (text + visual) -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mt-12">
  <!-- Text block -->
  <!-- Visual block -->
</div>

<!-- Bento grid -->
<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-12">
  <div class="col-span-2 row-span-2"><!-- Large feature --></div>
  <div><!-- Small item --></div>
  <div><!-- Small item --></div>
  <div><!-- Small item --></div>
  <div><!-- Small item --></div>
</div>
```
