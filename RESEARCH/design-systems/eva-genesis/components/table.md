# Component: Table

> MAGI data readout — dense, mono-spaced numbers, scanline aesthetic.

## Structure

```
┌────────────────────────────────────────────────────────┐
│  TH     TH        TH         TH           TH          │  ← text-xs, uppercase,
│─────────────────────────────────────────────────────── │     tracking-widest, on-surface-muted
│  TD     TD        TD         TD           TD          │  ← text-sm, on-surface
│  TD     TD        TD         TD           TD          │
│  TD     TD        TD         TD           TD          │
│────────────────────────────────────────────────────────│
│  Pagination / Summary                                  │
└────────────────────────────────────────────────────────┘
```

## Row States

| State | Background | Border | Notes |
|-------|-----------|--------|-------|
| Default (even) | `surface` | border-b `border` | Base |
| Default (odd) | `surface-input` | border-b `border` | Subtle zebra stripe |
| Hover | `surface-hover` | border-b `border` | Row highlight |
| Selected | `primary-muted` | border-b `border-focus` | Active selection |
| Danger | `error-surface` | border-b `error` | Alert row |

## Rules

- Numeric columns: `font-mono` + `tabular-nums` + right-aligned
- Status columns: Use Badge component
- Header row: sticky top, `surface-raised` bg, border-b `border-strong`
- Dense variant: py-1.5 instead of py-2.5

## Tailwind Usage

```html
<div class="border border-border rounded-lg overflow-hidden">
  <table class="w-full">
    <thead>
      <tr class="bg-surface-raised border-b border-border-strong">
        <th class="px-4 py-3 text-left text-[0.6875rem] uppercase tracking-widest
                   font-semibold text-on-surface-muted">
          Unit
        </th>
        <th class="px-4 py-3 text-left text-[0.6875rem] uppercase tracking-widest
                   font-semibold text-on-surface-muted">
          Pilot
        </th>
        <th class="px-4 py-3 text-right text-[0.6875rem] uppercase tracking-widest
                   font-semibold text-on-surface-muted">
          Sync Rate
        </th>
        <th class="px-4 py-3 text-left text-[0.6875rem] uppercase tracking-widest
                   font-semibold text-on-surface-muted">
          Status
        </th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b border-border hover:bg-surface-hover transition-colors">
        <td class="px-4 py-2.5 text-sm text-on-surface font-medium">EVA-01</td>
        <td class="px-4 py-2.5 text-sm text-on-surface-muted">Ikari, S.</td>
        <td class="px-4 py-2.5 text-sm text-on-surface font-mono tabular-nums text-right">94.2%</td>
        <td class="px-4 py-2.5">
          <span class="inline-flex items-center gap-1.5 bg-[oklch(15%_0.06_155)] text-success
                       px-2 py-0.5 rounded-full text-[0.6875rem] uppercase tracking-wider font-semibold">
            <span class="h-1.5 w-1.5 rounded-full bg-success animate-pulse"></span>
            ACTIVE
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```
