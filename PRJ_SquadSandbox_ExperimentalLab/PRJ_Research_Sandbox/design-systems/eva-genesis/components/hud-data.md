# Component: HUD Data Display

> NERV HQ readout panels — orange text on dark, cyan data, green grid lines.

## Variants

| Variant | Text Color | Accent | Use Case |
|---------|-----------|--------|---------|
| `nerv` | `nerv-text` (orange) | `nerv-grid` (green) | Primary readout |
| `data` | `nerv-data` (cyan) | `nerv-grid` (green) | Data analysis |
| `alert` | `error` | `berserk` | Emergency readout |

## Structure — Data Panel

```
┌─────────────────────────────────────┐
│  ┌─ HEADER ────────────────────┐   │
│  │  LABEL          TIMESTAMP   │   │
│  └─────────────────────────────┘   │
│                                     │
│  KEY ............... VALUE          │
│  KEY ............... VALUE          │
│  KEY ............... VALUE          │
│                                     │
│  ▓▓▓▓▓▓▓░░░░░ 67% ── BAR GRAPH   │
└─────────────────────────────────────┘
```

## Tailwind Usage

```html
<!-- NERV Data Panel -->
<div class="bg-surface-raised border border-border rounded-lg overflow-hidden shadow-md">
  <!-- Header -->
  <div class="flex items-center justify-between px-4 py-2.5 bg-void-800 border-b border-border">
    <span class="font-display text-[0.6875rem] uppercase tracking-[0.15em] font-bold text-nerv-orange">
      EVA Unit Status
    </span>
    <span class="font-mono text-[0.6875rem] text-nerv-cyan tabular-nums">
      14:32:07.042
    </span>
  </div>

  <!-- Data Rows -->
  <div class="p-4 space-y-2.5">
    <div class="flex items-center justify-between text-sm">
      <span class="text-nerv-orange font-mono text-xs uppercase tracking-wider">Unit</span>
      <span class="font-mono text-on-surface tabular-nums">EVA-01</span>
    </div>
    <div class="flex items-center justify-between text-sm">
      <span class="text-nerv-orange font-mono text-xs uppercase tracking-wider">Pilot</span>
      <span class="font-mono text-nerv-cyan">IKARI, SHINJI</span>
    </div>
    <div class="flex items-center justify-between text-sm">
      <span class="text-nerv-orange font-mono text-xs uppercase tracking-wider">Sync</span>
      <span class="font-mono text-secondary font-bold tabular-nums">94.2%</span>
    </div>
    <div class="flex items-center justify-between text-sm">
      <span class="text-nerv-orange font-mono text-xs uppercase tracking-wider">AT Field</span>
      <span class="font-mono text-at-field font-bold tabular-nums">142.7%</span>
    </div>

    <!-- Separator — green grid line -->
    <div class="border-t border-nerv-green/20 my-2"></div>

    <!-- Bar Graph -->
    <div>
      <div class="flex items-center justify-between mb-1">
        <span class="text-nerv-orange font-mono text-xs uppercase tracking-wider">Power</span>
        <span class="font-mono text-xs text-nerv-cyan tabular-nums">04:32:00</span>
      </div>
      <div class="h-1.5 bg-void-800 rounded-full overflow-hidden">
        <div class="h-full bg-nerv-green rounded-full shadow-[0_0_8px_oklch(78%_0.30_142/0.5)]"
             style="width: 67%"></div>
      </div>
    </div>
  </div>
</div>

<!-- Compact HUD Readout Row -->
<div class="flex items-center gap-6 bg-void-800/60 border border-border rounded-md px-4 py-2.5">
  <span class="font-display text-[0.625rem] uppercase tracking-[0.2em] text-nerv-orange font-bold">
    SYS
  </span>
  <span class="font-mono text-xs text-nerv-cyan tabular-nums">CPU: 78.4%</span>
  <span class="font-mono text-xs text-nerv-green tabular-nums">MEM: 4.2 GB</span>
  <span class="font-mono text-xs text-nerv-orange tabular-nums">NET: 1.2 Gbps</span>
  <span class="font-mono text-xs text-on-surface-muted ml-auto tabular-nums">14:32:07</span>
</div>
```
