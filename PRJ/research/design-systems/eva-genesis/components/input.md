# Component: Input

> Sunken entry fields — data flows into the system through recessed channels.

## Variants

| Variant | Background | Border | Notes |
|---------|-----------|--------|-------|
| `default` | `surface-input` | `border` | Standard text input |
| `ghost` | `transparent` | `border` (bottom only) | Minimal — search bars, inline edit |
| `filled` | `surface-raised` | none | Dense forms, dark fields |

## States

| State | Border | Shadow | Ring | Notes |
|-------|--------|--------|------|-------|
| Default | `border` | `inset-sm` | none | Recessed appearance |
| Hover | `border-strong` | `inset-sm` | none | Subtle acknowledgment |
| Focus | `border-focus` | none | `ring-focus` | AT Field glow activates |
| Error | `error` | none | `ring-error` | Pattern Blue alert |
| Disabled | `border` | `inset-sm` | none | opacity 0.4 |
| Read-only | `surface-raised` | none | none | Non-interactive data display |

## Sizing

| Size | Padding | Font | Height |
|------|---------|------|--------|
| `sm` | 8px 10px | text-sm | 32px |
| `md` | 10px 14px | text-base | 40px |
| `lg` | 12px 16px | text-lg | 48px |

## Structure

```
┌─ Label ─────────────────────────────┐  ← text-xs, uppercase, tracking-widest
│                                      │     font-semibold, on-surface-muted
│  [icon]  Input value here            │  ← surface-input bg, inset shadow
│                                      │
└──────────────────────────────────────┘
  Helper text or error message            ← text-xs, on-surface-muted or error
```

## Tailwind Usage

```html
<!-- Default Input with Label -->
<div class="space-y-1.5">
  <label class="text-[0.6875rem] uppercase tracking-widest font-semibold text-on-surface-muted">
    Pilot Name
  </label>
  <input
    type="text"
    placeholder="Enter designation..."
    class="w-full bg-surface-input border border-border rounded-md
           px-3.5 py-2.5 text-[0.9375rem] text-on-surface
           placeholder:text-on-surface-disabled
           shadow-[inset_0_1px_2px_oklch(5%_0.02_285/0.4)]
           hover:border-border-strong
           focus:border-border-focus focus:ring-2 focus:ring-eva-purple-400/80
           focus:ring-offset-2 focus:ring-offset-void-950
           focus:shadow-none
           disabled:opacity-40 disabled:cursor-not-allowed
           transition-all duration-200"
  />
  <p class="text-[0.6875rem] text-on-surface-muted">Designation code (e.g., IKARI-S)</p>
</div>

<!-- Error State -->
<div class="space-y-1.5">
  <label class="text-[0.6875rem] uppercase tracking-widest font-semibold text-error">
    Sync Rate
  </label>
  <input
    type="text"
    value="ERROR"
    class="w-full bg-surface-input border border-error rounded-md
           px-3.5 py-2.5 text-[0.9375rem] text-on-surface
           ring-2 ring-angel-red-500/80 ring-offset-2 ring-offset-void-950
           transition-all duration-200"
  />
  <p class="text-[0.6875rem] text-error">Synchronization failed — Pattern Blue detected</p>
</div>
```
