# Component: Synchronization Meter

> Pilot-EVA sync rate display — the most iconic data readout in NERV HQ.

## Variants

| Variant | Range | Color | Glow | Notes |
|---------|-------|-------|------|-------|
| `critical` | 0-30% | `error` | `glow-danger` | Connection unstable |
| `low` | 31-50% | `warning` | `glow-nerv` | Below operational |
| `normal` | 51-80% | `nerv-data` | none | Standard operation |
| `high` | 81-99% | `secondary` | `glow-secondary` | Peak performance |
| `berserk` | 100%+ | `berserk` | `glow-danger` pulsing | Loss of control |

## Structure

```
┌─────────────────────────────────────────────────┐
│  SYNC RATE          PILOT: IKARI, S.            │
│  ████████████████████░░░░░░░░  94.2%            │
│  ─────────────────────────────────────          │
│  NEURAL: STABLE    AT FIELD: 142.7%             │
└─────────────────────────────────────────────────┘
```

## Tailwind Usage

```html
<!-- Sync Meter — High -->
<div class="bg-surface-raised border border-border rounded-lg p-4 shadow-md">
  <div class="flex items-center justify-between mb-2">
    <span class="font-display text-[0.6875rem] uppercase tracking-[0.15em] font-bold text-on-surface-muted">
      Sync Rate
    </span>
    <span class="font-mono text-sm font-bold text-secondary tabular-nums">
      94.2%
    </span>
  </div>

  <!-- Progress Bar -->
  <div class="relative h-2 bg-void-800 rounded-full overflow-hidden">
    <div class="absolute inset-y-0 left-0 bg-secondary rounded-full transition-all duration-500"
         style="width: 94.2%;">
      <div class="absolute inset-0 bg-gradient-to-r from-secondary/80 to-secondary
                  shadow-[0_0_12px_oklch(72%_0.30_145/0.5)]"></div>
    </div>
  </div>

  <!-- Sub-data -->
  <div class="flex items-center justify-between mt-3 text-[0.6875rem]">
    <span class="text-on-surface-muted">
      Neural: <span class="font-mono text-nerv-data">STABLE</span>
    </span>
    <span class="text-on-surface-muted">
      AT Field: <span class="font-mono text-nerv-orange tabular-nums">142.7%</span>
    </span>
  </div>
</div>

<!-- Sync Meter — Berserk -->
<div class="bg-error-surface border border-error rounded-lg p-4 shadow-md
            shadow-[0_0_20px_oklch(55%_0.30_20/0.4)] animate-[pattern-blue_1.5s_ease-in-out_infinite]">
  <div class="flex items-center justify-between mb-2">
    <span class="font-display text-[0.6875rem] uppercase tracking-[0.15em] font-bold text-error">
      !! BERSERK MODE !!
    </span>
    <span class="font-mono text-sm font-bold text-error tabular-nums animate-pulse">
      ∞%
    </span>
  </div>
  <div class="h-2 bg-error rounded-full shadow-[0_0_12px_oklch(55%_0.30_20/0.6)]"></div>
  <div class="mt-3 text-[0.6875rem] text-error font-mono uppercase tracking-wider text-center">
    PILOT CONTROL LOST — INITIATING EMERGENCY SHUTDOWN
  </div>
</div>
```
