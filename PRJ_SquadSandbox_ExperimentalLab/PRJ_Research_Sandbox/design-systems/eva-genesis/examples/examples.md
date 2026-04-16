# EVA GENESIS — Implementation Examples

## Example 1: NERV Dashboard Card Grid

```html
<section class="bg-surface py-16 px-6">
  <div class="max-w-7xl mx-auto">
    <!-- Section Header -->
    <span class="text-[0.6875rem] uppercase tracking-widest font-semibold text-accent">
      Monitoring
    </span>
    <h2 class="mt-3 font-display text-3xl font-bold uppercase tracking-wide text-on-surface">
      EVA Status Overview
    </h2>

    <!-- Card Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10">
      <!-- Card: Unit-01 -->
      <div class="bg-surface-raised border border-border rounded-lg shadow-md p-5
                  hover:shadow-lg hover:border-border-strong hover:-translate-y-0.5
                  transition-all duration-200">
        <div class="flex items-center justify-between">
          <h3 class="font-display text-lg font-bold uppercase tracking-wide text-on-surface">
            EVA-01
          </h3>
          <span class="inline-flex items-center gap-1.5
                       bg-[oklch(15%_0.06_155)] text-success
                       px-2 py-0.5 rounded-full
                       text-[0.6875rem] uppercase tracking-wider font-semibold">
            <span class="h-1.5 w-1.5 rounded-full bg-success animate-pulse"></span>
            ACTIVE
          </span>
        </div>
        <div class="mt-4 space-y-2">
          <div class="flex justify-between text-sm">
            <span class="text-on-surface-muted">Sync Rate</span>
            <span class="font-mono tabular-nums text-on-surface">94.2%</span>
          </div>
          <div class="flex justify-between text-sm">
            <span class="text-on-surface-muted">Pilot</span>
            <span class="text-on-surface">Ikari, S.</span>
          </div>
          <div class="flex justify-between text-sm">
            <span class="text-on-surface-muted">AT Field</span>
            <span class="font-mono tabular-nums text-primary">142.7%</span>
          </div>
        </div>
      </div>
      <!-- More cards follow same pattern -->
    </div>
  </div>
</section>
```

---

## Example 2: Command Login Form

```html
<div class="min-h-screen bg-surface flex items-center justify-center px-4">
  <div class="w-full max-w-sm">
    <!-- Logo -->
    <div class="text-center mb-10">
      <h1 class="font-display text-4xl font-black uppercase tracking-wider text-on-surface">
        NERV
      </h1>
      <p class="mt-2 text-sm text-on-surface-muted">Authorized personnel only</p>
    </div>

    <!-- Form -->
    <div class="bg-surface-raised border border-border rounded-xl shadow-xl p-6 space-y-5">
      <div class="space-y-1.5">
        <label class="text-[0.6875rem] uppercase tracking-widest font-semibold text-on-surface-muted">
          Designation
        </label>
        <input type="text" placeholder="IKARI-S"
               class="w-full bg-surface-input border border-border rounded-md
                      px-3.5 py-2.5 text-[0.9375rem] text-on-surface
                      placeholder:text-on-surface-disabled
                      shadow-[inset_0_1px_2px_oklch(5%_0.02_285/0.4)]
                      hover:border-border-strong
                      focus:border-border-focus focus:ring-2 focus:ring-eva-purple-400/80
                      focus:ring-offset-2 focus:ring-offset-void-950 focus:shadow-none
                      transition-all duration-200" />
      </div>

      <div class="space-y-1.5">
        <label class="text-[0.6875rem] uppercase tracking-widest font-semibold text-on-surface-muted">
          Access Code
        </label>
        <input type="password" placeholder="••••••••"
               class="w-full bg-surface-input border border-border rounded-md
                      px-3.5 py-2.5 text-[0.9375rem] text-on-surface font-mono
                      placeholder:text-on-surface-disabled
                      shadow-[inset_0_1px_2px_oklch(5%_0.02_285/0.4)]
                      hover:border-border-strong
                      focus:border-border-focus focus:ring-2 focus:ring-eva-purple-400/80
                      focus:ring-offset-2 focus:ring-offset-void-950 focus:shadow-none
                      transition-all duration-200" />
      </div>

      <button class="w-full bg-primary text-primary-foreground py-2.5 text-[0.9375rem]
                     font-medium rounded-md shadow-sm
                     hover:shadow-[0_0_20px_oklch(45%_0.28_300/0.4)] hover:brightness-105
                     active:scale-[0.97]
                     transition-all duration-200">
        Authenticate
      </button>

      <p class="text-center text-xs text-on-surface-disabled">
        MAGI System v3.0 — Casper | Balthasar | Melchior
      </p>
    </div>
  </div>
</div>
```

---

## Example 3: Framer Motion Hero with Stagger

```tsx
import { motion } from 'framer-motion';

const container = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.12, delayChildren: 0.3 } }
};

const item = {
  hidden: { opacity: 0, y: 24, scale: 0.96 },
  visible: {
    opacity: 1, y: 0, scale: 1,
    transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] }
  }
};

export function NervHero() {
  return (
    <section className="relative min-h-screen bg-surface flex items-center justify-center overflow-hidden">
      {/* AT Field radial glow */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_50%_40%,oklch(25%_0.15_300/0.3),transparent_70%)]" />

      <motion.div
        className="relative z-10 text-center max-w-4xl px-6"
        variants={container}
        initial="hidden"
        animate="visible"
      >
        <motion.span
          variants={item}
          className="inline-flex items-center gap-1.5 bg-primary-muted text-primary
                     px-3 py-1 rounded-full text-[0.6875rem] uppercase tracking-widest font-semibold"
        >
          <span className="h-1.5 w-1.5 rounded-full bg-primary animate-pulse" />
          EVANGELION
        </motion.span>

        <motion.h1
          variants={item}
          className="mt-8 font-display text-6xl font-black uppercase tracking-wider text-on-surface"
        >
          THE FATE OF
          <br />
          <span className="text-primary">DESTRUCTION</span>
          <br />
          IS THE JOY OF REBIRTH
        </motion.h1>

        <motion.p
          variants={item}
          className="mt-6 text-xl text-on-surface-muted max-w-2xl mx-auto"
        >
          EVA GENESIS design system — built for interfaces that demand
          attention and refuse to be ignored.
        </motion.p>

        <motion.div variants={item} className="mt-10 flex justify-center gap-4">
          <motion.button
            whileHover={{ scale: 1.02, boxShadow: '0 0 20px oklch(45% 0.28 300 / 0.4)' }}
            whileTap={{ scale: 0.97 }}
            className="bg-primary text-primary-foreground px-8 py-3 rounded-md font-medium shadow-sm"
          >
            Get Started
          </motion.button>
          <button className="text-on-surface-muted px-8 py-3 rounded-md border border-border
                            hover:bg-surface-hover hover:text-on-surface transition-all duration-200">
            View Tokens
          </button>
        </motion.div>
      </motion.div>
    </section>
  );
}
```
