# Component: Navigation

> NERV command bar — fixed, dense, authoritative.

## Variants

| Variant | Position | Background | Use Case |
|---------|----------|-----------|---------|
| `fixed-top` | fixed top-0 | `surface` with backdrop-blur | Primary navigation |
| `sidebar` | fixed left-0 | `surface-raised` | Dashboard, admin panels |
| `command-bar` | fixed bottom-0 | `surface-glass` | Mobile, command palette |

## Structure — Fixed Top

```
┌──────────────────────────────────────────────────────────┐
│  [Logo]    Nav Items                    [Actions] [User] │  ← h-14, border-b
└──────────────────────────────────────────────────────────┘
```

## Nav Item States

| State | Text | Indicator | Notes |
|-------|------|-----------|-------|
| Default | `on-surface-muted` | none | — |
| Hover | `on-surface` | — | bg-surface-hover |
| Active | `primary` | 2px bottom border `primary` | Current page |
| Disabled | `on-surface-disabled` | none | — |

## Tailwind Usage

```html
<nav class="fixed top-0 inset-x-0 z-50
            h-14 bg-surface/80 backdrop-blur-xl
            border-b border-border
            flex items-center px-6">
  <!-- Logo -->
  <a href="/" class="font-display text-lg font-bold uppercase tracking-wider text-on-surface">
    NERV
  </a>

  <!-- Nav Items -->
  <div class="ml-8 flex items-center gap-1">
    <a href="/dashboard"
       class="px-3 py-1.5 text-sm font-medium text-primary
              border-b-2 border-primary rounded-none">
      Dashboard
    </a>
    <a href="/pilots"
       class="px-3 py-1.5 text-sm font-medium text-on-surface-muted
              hover:text-on-surface hover:bg-surface-hover
              rounded-md transition-colors duration-200">
      Pilots
    </a>
    <a href="/units"
       class="px-3 py-1.5 text-sm font-medium text-on-surface-muted
              hover:text-on-surface hover:bg-surface-hover
              rounded-md transition-colors duration-200">
      EVA Units
    </a>
  </div>

  <!-- Actions -->
  <div class="ml-auto flex items-center gap-3">
    <span class="inline-flex items-center gap-1.5
                 bg-[oklch(15%_0.06_155)] text-success
                 px-2 py-0.5 rounded-full
                 text-[0.6875rem] uppercase tracking-wider font-semibold font-mono">
      <span class="h-1.5 w-1.5 rounded-full bg-success animate-pulse"></span>
      MAGI: ONLINE
    </span>
    <button class="h-8 w-8 rounded-full bg-surface-raised border border-border
                   flex items-center justify-center
                   hover:border-border-strong transition-colors duration-200">
      <!-- Avatar/Icon -->
    </button>
  </div>
</nav>
```
