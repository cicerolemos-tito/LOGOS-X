/* EVA GENESIS — CSS Custom Properties v1.0.0
   Dark mode only. Palette: Deep EVA Purple + Neon Green + Entry Amber.
   Import at the root of your project.
   Usage: var(--eva-surface), var(--eva-primary), etc. */

:root {
  /* ── Surfaces (deep purple-tinted voids) ── */
  --eva-surface: oklch(8% 0.02 290);
  --eva-surface-raised: oklch(12% 0.02 290);
  --eva-surface-overlay: oklch(16% 0.03 290);
  --eva-surface-input: oklch(10% 0.02 290);
  --eva-surface-glass: oklch(14% 0.04 295 / 0.6);
  --eva-surface-hover: oklch(20% 0.03 290);

  /* ── Content ── */
  --eva-on-surface: oklch(92% 0.01 290);
  --eva-on-surface-muted: oklch(58% 0.02 290);
  --eva-on-surface-disabled: oklch(32% 0.01 290);

  /* ── Borders ── */
  --eva-border: oklch(20% 0.03 290);
  --eva-border-strong: oklch(30% 0.04 300);
  --eva-border-focus: oklch(52% 0.32 295);

  /* ── Brand: Primary (EVA Purple — deep, saturated) ── */
  --eva-primary: oklch(44% 0.33 295);
  --eva-primary-hover: oklch(52% 0.32 295);
  --eva-primary-active: oklch(38% 0.32 295);
  --eva-primary-foreground: oklch(92% 0.01 290);
  --eva-primary-muted: oklch(18% 0.18 295);

  /* ── Brand: Secondary (Neon Green — electric) ── */
  --eva-secondary: oklch(78% 0.30 145);
  --eva-secondary-hover: oklch(85% 0.28 145);
  --eva-secondary-active: oklch(65% 0.28 145);
  --eva-secondary-foreground: oklch(8% 0.02 290);

  /* ── Brand: Accent (Entry Amber) ── */
  --eva-accent: oklch(78% 0.18 85);
  --eva-accent-hover: oklch(85% 0.16 85);
  --eva-accent-active: oklch(65% 0.17 85);
  --eva-accent-foreground: oklch(8% 0.02 290);

  /* ── Status ── */
  --eva-success: oklch(72% 0.26 145);
  --eva-success-surface: oklch(15% 0.08 145);
  --eva-warning: oklch(78% 0.18 85);
  --eva-warning-surface: oklch(15% 0.07 85);
  --eva-error: oklch(58% 0.25 25);
  --eva-error-surface: oklch(15% 0.08 25);
  --eva-info: oklch(62% 0.15 240);
  --eva-info-surface: oklch(15% 0.06 240);

  /* ── Glow FX ── */
  --eva-glow-primary: 0 0 20px oklch(44% 0.33 295 / 0.4), 0 0 60px oklch(44% 0.33 295 / 0.15);
  --eva-glow-neon: 0 0 20px oklch(78% 0.30 145 / 0.4), 0 0 60px oklch(78% 0.30 145 / 0.15);
  --eva-glow-danger: 0 0 20px oklch(58% 0.25 25 / 0.4), 0 0 60px oklch(58% 0.25 25 / 0.15);
  --eva-glow-sync: 0 0 20px oklch(72% 0.26 145 / 0.4), 0 0 60px oklch(72% 0.26 145 / 0.15);

  /* ── Shadows (purple-tinted) ── */
  --eva-shadow-sm: 0 1px 3px oklch(5% 0.03 290 / 0.5);
  --eva-shadow-md: 0 4px 12px oklch(5% 0.04 295 / 0.4), 0 1px 3px oklch(5% 0.03 290 / 0.3);
  --eva-shadow-lg: 0 8px 32px oklch(5% 0.05 295 / 0.5), 0 2px 8px oklch(5% 0.03 290 / 0.3);
  --eva-shadow-xl: 0 16px 48px oklch(5% 0.06 295 / 0.6), 0 4px 16px oklch(5% 0.04 290 / 0.4);

  /* ── Typography ── */
  --eva-font-display: 'Orbitron', 'Rajdhani', system-ui, sans-serif;
  --eva-font-sans: 'Geist Sans', 'Inter', system-ui, -apple-system, sans-serif;
  --eva-font-mono: 'Geist Mono', 'JetBrains Mono', 'Fira Code', Consolas, monospace;

  /* ── Spacing (base: 4px) ── */
  --eva-space-1: 0.25rem;
  --eva-space-2: 0.5rem;
  --eva-space-3: 0.75rem;
  --eva-space-4: 1rem;
  --eva-space-5: 1.25rem;
  --eva-space-6: 1.5rem;
  --eva-space-8: 2rem;
  --eva-space-10: 2.5rem;
  --eva-space-12: 3rem;
  --eva-space-16: 4rem;
  --eva-space-20: 5rem;
  --eva-space-24: 6rem;

  /* ── Border Radius ── */
  --eva-radius-sm: 4px;
  --eva-radius-md: 6px;
  --eva-radius-lg: 10px;
  --eva-radius-xl: 12px;

  /* ── Motion ── */
  --eva-ease-nerv: cubic-bezier(0.16, 1, 0.3, 1);
  --eva-ease-alert: cubic-bezier(0.68, -0.55, 0.27, 1.55);
  --eva-ease-deploy: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --eva-duration-fast: 200ms;
  --eva-duration-normal: 350ms;
  --eva-duration-slow: 600ms;
  --eva-duration-dramatic: 1000ms;
}

@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.1s !important; transition-duration: 0.1s !important; }
}
