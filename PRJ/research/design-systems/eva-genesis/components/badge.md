# Component: Badge

> Status indicators — compact, high-contrast, always mono-spaced when showing data.

## Variants

| Variant | Background | Text | Border | Use Case |
|---------|-----------|------|--------|---------|
| `default` | `primary-muted` | `primary` | none | General labels, tags |
| `secondary` | `oklch(15% 0.06 195)` | `secondary` | none | Secondary info |
| `accent` | `oklch(15% 0.07 85)` | `accent` | none | Highlights, new items |
| `success` | `success-surface` | `success` | none | Active, online, synced |
| `warning` | `warning-surface` | `warning` | none | Caution, pending |
| `error` | `error-surface` | `error` | none | Critical, offline |
| `info` | `info-surface` | `info` | none | Informational |
| `outline` | `transparent` | `on-surface-muted` | `border` | Subtle, metadata |

## Sizing

| Size | Padding | Font | Height |
|------|---------|------|--------|
| `sm` | 2px 6px | text-xs (11px) | 20px |
| `md` | 4px 10px | text-xs (11px) | 24px |
| `lg` | 6px 12px | text-sm (13px) | 28px |

## Rules

- Badge text is ALWAYS `uppercase` + `tracking-wider` + `font-semibold`
- Numeric data inside badges uses `font-mono` + `tabular-nums`
- Max content: 20 characters. Longer text → use a different component
- Status badges with pulse animation → add `sync-pulse` motion

## Tailwind Usage

```html
<!-- Status: Active (with pulse) -->
<span class="inline-flex items-center gap-1.5
             bg-[oklch(15%_0.06_155)] text-success
             px-2.5 py-1 rounded-full
             text-[0.6875rem] uppercase tracking-wider font-semibold">
  <span class="h-1.5 w-1.5 rounded-full bg-success animate-pulse"></span>
  SYNCED
</span>

<!-- Status: Critical -->
<span class="inline-flex items-center gap-1.5
             bg-error-surface text-error
             px-2.5 py-1 rounded-full
             text-[0.6875rem] uppercase tracking-wider font-semibold">
  <span class="h-1.5 w-1.5 rounded-full bg-error"></span>
  PATTERN BLUE
</span>

<!-- Data Badge (mono) -->
<span class="inline-flex items-center
             bg-primary-muted text-primary
             px-2.5 py-1 rounded-full
             font-mono text-[0.6875rem] tabular-nums font-semibold">
  94.2%
</span>
```
