# Component: Toast / Notification

> MAGI system alerts — compact, auto-dismiss, positioned bottom-right.

## Variants

| Variant | Icon BG | Border Left | Use Case |
|---------|---------|-------------|---------|
| `default` | `primary-muted` | `primary` | General notification |
| `success` | `success-surface` | `success` | Operation confirmed |
| `warning` | `warning-surface` | `warning` | Caution advisory |
| `error` | `error-surface` | `error` | Critical failure |
| `info` | `info-surface` | `info` | System information |

## Structure

```
┌─────────────────────────────────────────┐
│ ▌ [Icon]  Title                    [×]  │  ← border-left-4
│ ▌         Description text              │
│ ▌         [Action]  [Dismiss]           │  ← optional
└─────────────────────────────────────────┘
```

## Animation

- **Enter:** slide from right + fade (x: 100→0, opacity: 0→1, 350ms, ease-nerv)
- **Exit:** slide right + fade (x: 0→100, opacity: 1→0, 200ms)
- **Auto-dismiss:** 5000ms default, pause on hover

## Tailwind Usage

```html
<!-- Success Toast -->
<div class="flex items-start gap-3 w-80
            bg-surface-raised border border-border border-l-4 border-l-success
            rounded-lg shadow-lg p-4">
  <div class="flex-shrink-0 h-8 w-8 rounded-md bg-[oklch(15%_0.06_155)]
              flex items-center justify-center">
    <!-- Check icon in text-success -->
  </div>
  <div class="flex-1 min-w-0">
    <p class="text-sm font-semibold text-on-surface">Sync Complete</p>
    <p class="mt-0.5 text-xs text-on-surface-muted">Unit-01 synchronization at 94.2%</p>
  </div>
  <button class="text-on-surface-disabled hover:text-on-surface transition-colors">
    <!-- Close icon -->
  </button>
</div>

<!-- Error Toast -->
<div class="flex items-start gap-3 w-80
            bg-surface-raised border border-border border-l-4 border-l-error
            rounded-lg shadow-lg p-4">
  <div class="flex-shrink-0 h-8 w-8 rounded-md bg-error-surface
              flex items-center justify-center">
    <!-- Alert icon in text-error -->
  </div>
  <div class="flex-1 min-w-0">
    <p class="text-sm font-semibold text-on-surface">Pattern Blue Detected</p>
    <p class="mt-0.5 text-xs text-on-surface-muted">Angel approaching — all pilots report to cages</p>
  </div>
</div>
```
