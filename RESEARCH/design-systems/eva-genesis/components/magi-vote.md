# Component: MAGI Voting Display

> The three MAGI supercomputers vote on critical decisions. Casper, Balthasar, Melchior.

## Structure

```
┌───────────────────────────────────────────────────┐
│              MAGI DECISION SYSTEM                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │ MELCHIOR │  │ BALTHASAR│  │  CASPER   │       │
│  │          │  │          │  │          │       │
│  │ APPROVE  │  │  DENY    │  │ APPROVE  │       │
│  │  ●       │  │    ●     │  │  ●       │       │
│  └──────────┘  └──────────┘  └──────────┘       │
│                                                   │
│  RESULT: 2/3 APPROVED                             │
└───────────────────────────────────────────────────┘
```

## Vote States

| State | Background | Border | Glow | Icon Color |
|-------|-----------|--------|------|------------|
| Approve | `success-surface` | `success` | `glow-sync` | `success` |
| Deny | `error-surface` | `error` | `glow-danger` | `error` |
| Pending | `warning-surface` | `warning` | `glow-nerv` | `warning` |
| Processing | `surface-raised` | `border` | pulse animation | `on-surface-muted` |

## Tailwind Usage

```html
<div class="bg-surface-raised border border-border rounded-xl p-6 shadow-lg">
  <h3 class="font-display text-xs uppercase tracking-[0.2em] font-semibold text-nerv-data text-center mb-6">
    MAGI Decision System
  </h3>

  <div class="grid grid-cols-3 gap-4">
    <!-- Melchior: Approve -->
    <div class="bg-success-surface border border-success rounded-lg p-4 text-center
                shadow-[0_0_20px_oklch(72%_0.26_145/0.3)]">
      <span class="font-display text-[0.6875rem] uppercase tracking-[0.15em] font-bold text-on-surface-muted">
        Melchior
      </span>
      <div class="mt-3 h-3 w-3 rounded-full bg-success mx-auto animate-pulse"></div>
      <span class="mt-2 block font-mono text-xs font-bold text-success uppercase tracking-wider">
        Approve
      </span>
    </div>

    <!-- Balthasar: Deny -->
    <div class="bg-error-surface border border-error rounded-lg p-4 text-center
                shadow-[0_0_20px_oklch(55%_0.25_25/0.3)]">
      <span class="font-display text-[0.6875rem] uppercase tracking-[0.15em] font-bold text-on-surface-muted">
        Balthasar
      </span>
      <div class="mt-3 h-3 w-3 rounded-full bg-error mx-auto"></div>
      <span class="mt-2 block font-mono text-xs font-bold text-error uppercase tracking-wider">
        Deny
      </span>
    </div>

    <!-- Casper: Approve -->
    <div class="bg-success-surface border border-success rounded-lg p-4 text-center
                shadow-[0_0_20px_oklch(72%_0.26_145/0.3)]">
      <span class="font-display text-[0.6875rem] uppercase tracking-[0.15em] font-bold text-on-surface-muted">
        Casper
      </span>
      <div class="mt-3 h-3 w-3 rounded-full bg-success mx-auto animate-pulse"></div>
      <span class="mt-2 block font-mono text-xs font-bold text-success uppercase tracking-wider">
        Approve
      </span>
    </div>
  </div>

  <!-- Result -->
  <div class="mt-6 text-center border-t border-border pt-4">
    <span class="font-mono text-sm font-bold text-success tabular-nums">
      RESULT: 2/3 APPROVED
    </span>
  </div>
</div>
```
