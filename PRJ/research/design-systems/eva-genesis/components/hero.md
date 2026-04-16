# Component: Hero Section

> The entry plug activation sequence — maximum visual impact.

## Variants

| Variant | Layout | Visual Treatment |
|---------|--------|------------------|
| `centered` | Text center, stacked | Radial gradient glow behind heading |
| `split` | Text left, visual right | Asymmetric, image/3D on right half |
| `full-bleed` | Full viewport, text overlay | Background visual fills screen |
| `command` | Dense, data-rich | NERV terminal boot screen aesthetic |

## Structure — Centered (Default)

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│                   [Status Badge]                         │
│                                                          │
│            HERO HEADING TEXT                              │  ← font-display, text-5xl/6xl
│            IN UPPERCASE                                  │     uppercase, tracking-wider
│                                                          │
│       Subheading in regular weight,                      │  ← font-sans, text-lg/xl
│       on-surface-muted, max-w-2xl                        │     on-surface-muted
│                                                          │
│         [Primary CTA]  [Secondary CTA]                   │  ← button-lg
│                                                          │
│                                                          │  ← py-24 to py-32
└──────────────────────────────────────────────────────────┘
```

## Background Effects

- **Radial glow:** `radial-gradient(ellipse at 50% 40%, oklch(25% 0.15 300 / 0.3), transparent 70%)`
- **Grid overlay:** Subtle CSS grid pattern at 5% opacity for terminal feel
- **Noise texture:** Optional film grain at 2-3% opacity via SVG filter

## Tailwind Usage

```html
<section class="relative min-h-[80vh] flex flex-col items-center justify-center
                px-6 py-24 overflow-hidden">
  <!-- Background glow -->
  <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_50%_40%,oklch(25%_0.15_300/0.3),transparent_70%)]
              pointer-events-none" />

  <!-- Content -->
  <div class="relative z-10 flex flex-col items-center text-center max-w-4xl">
    <!-- Status badge -->
    <span class="inline-flex items-center gap-1.5
                 bg-primary-muted text-primary
                 px-3 py-1 rounded-full mb-8
                 text-[0.6875rem] uppercase tracking-widest font-semibold">
      <span class="h-1.5 w-1.5 rounded-full bg-primary animate-pulse"></span>
      SYSTEM ACTIVE
    </span>

    <!-- Heading -->
    <h1 class="font-display text-5xl md:text-6xl font-black uppercase tracking-wider
               text-on-surface leading-none">
      GOD'S IN HIS HEAVEN.
      <br />
      <span class="text-primary">ALL'S RIGHT WITH THE WORLD.</span>
    </h1>

    <!-- Subheading -->
    <p class="mt-6 text-lg md:text-xl text-on-surface-muted max-w-2xl leading-relaxed">
      A dark brutalist design system forged from NERV command aesthetics
      and biomechanical precision.
    </p>

    <!-- CTAs -->
    <div class="mt-10 flex items-center gap-4">
      <button class="bg-primary text-primary-foreground px-8 py-3 text-base
                     font-medium rounded-md shadow-sm
                     hover:shadow-[0_0_20px_oklch(45%_0.28_300/0.4)]
                     hover:brightness-105
                     active:scale-[0.97]
                     transition-all duration-200">
        Initialize
      </button>
      <button class="bg-transparent text-on-surface-muted px-8 py-3 text-base
                     font-medium rounded-md border border-border
                     hover:bg-surface-hover hover:text-on-surface hover:border-border-strong
                     transition-all duration-200">
        Read Docs
      </button>
    </div>
  </div>
</section>
```

## Framer Motion

```tsx
const heroVariants = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.12, delayChildren: 0.3 } }
};

const itemVariants = {
  hidden: { opacity: 0, y: 24, scale: 0.96 },
  visible: { opacity: 1, y: 0, scale: 1, transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] } }
};

<motion.div variants={heroVariants} initial="hidden" animate="visible">
  <motion.span variants={itemVariants}>{/* badge */}</motion.span>
  <motion.h1 variants={itemVariants}>{/* heading */}</motion.h1>
  <motion.p variants={itemVariants}>{/* subheading */}</motion.p>
  <motion.div variants={itemVariants}>{/* CTAs */}</motion.div>
</motion.div>
```
