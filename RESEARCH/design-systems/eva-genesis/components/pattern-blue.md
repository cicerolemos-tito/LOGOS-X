# Component: Pattern Blue Alert

> Angel detection alert — the most urgent notification in the system.

## Alert Levels

| Level | Label | Colors | Animation |
|-------|-------|--------|-----------|
| `standby` | ALL CLEAR | `success` bg | none |
| `monitoring` | MONITORING | `info` bg | slow pulse |
| `pattern-orange` | PATTERN ORANGE | `warning` bg | medium pulse |
| `pattern-blue` | PATTERN BLUE | `error` bg | rapid pulse + flash |

## Structure — Full Alert

```
┌──────────────────────────────────────────────────────┐
│  ██  !! PATTERN BLUE DETECTED !!  ██                 │
│                                                      │
│  Classification: ANGEL                               │
│  Designation:    6th Angel — RAMIEL                   │
│  Distance:       12.4 km                             │
│  Threat Level:   ABSOLUTE                            │
│                                                      │
│  [DEPLOY EVA]              [INITIATE LOCKDOWN]       │
└──────────────────────────────────────────────────────┘
```

## Tailwind Usage

```html
<!-- Pattern Blue — Full Alert -->
<div class="relative overflow-hidden bg-error-surface border-2 border-error rounded-xl p-6
            shadow-[0_0_30px_oklch(55%_0.25_25/0.4),0_0_80px_oklch(55%_0.25_25/0.15)]
            animate-[pattern-blue_1.5s_ease-in-out_infinite]">
  <!-- Scan lines overlay -->
  <div class="absolute inset-0 opacity-5 pointer-events-none"
       style="background: repeating-linear-gradient(0deg, transparent, transparent 2px, oklch(90% 0 0 / 0.1) 2px, oklch(90% 0 0 / 0.1) 4px)"></div>

  <!-- Header -->
  <div class="relative flex items-center justify-center gap-3">
    <span class="h-3 w-3 bg-error rounded-sm animate-pulse"></span>
    <span class="font-display text-lg font-black uppercase tracking-[0.15em] text-error">
      Pattern Blue Detected
    </span>
    <span class="h-3 w-3 bg-error rounded-sm animate-pulse"></span>
  </div>

  <!-- Data -->
  <div class="relative mt-5 grid grid-cols-2 gap-x-6 gap-y-2">
    <div class="flex justify-between text-sm">
      <span class="text-on-surface-muted">Classification</span>
      <span class="font-mono font-bold text-error uppercase">ANGEL</span>
    </div>
    <div class="flex justify-between text-sm">
      <span class="text-on-surface-muted">Designation</span>
      <span class="font-mono font-bold text-on-surface">RAMIEL</span>
    </div>
    <div class="flex justify-between text-sm">
      <span class="text-on-surface-muted">Distance</span>
      <span class="font-mono tabular-nums text-nerv-orange">12.4 km</span>
    </div>
    <div class="flex justify-between text-sm">
      <span class="text-on-surface-muted">Threat Level</span>
      <span class="font-mono font-bold text-error uppercase tracking-wider">ABSOLUTE</span>
    </div>
  </div>

  <!-- Actions -->
  <div class="relative mt-6 flex gap-3">
    <button class="flex-1 bg-error text-on-surface py-2.5 text-sm font-bold rounded-md uppercase tracking-wider
                   shadow-[0_0_20px_oklch(55%_0.25_25/0.4)]
                   hover:brightness-110 active:scale-[0.97] transition-all duration-200">
      Deploy EVA
    </button>
    <button class="flex-1 bg-transparent text-error py-2.5 text-sm font-bold rounded-md uppercase tracking-wider
                   border border-error hover:bg-error-surface transition-all duration-200">
      Initiate Lockdown
    </button>
  </div>
</div>

<!-- Pattern Blue — Compact Banner -->
<div class="flex items-center gap-3 bg-error-surface border border-error rounded-lg px-4 py-3
            shadow-[0_0_15px_oklch(55%_0.25_25/0.3)]">
  <span class="h-2.5 w-2.5 bg-error rounded-sm animate-pulse flex-shrink-0"></span>
  <span class="font-display text-xs font-bold uppercase tracking-[0.12em] text-error">
    Pattern Blue
  </span>
  <span class="font-mono text-xs text-on-surface-muted ml-auto tabular-nums">
    12.4 km — APPROACHING
  </span>
</div>
```
