# Component: Modal / Dialog

> Command overlay — demands attention, AT Field backdrop.

## Variants

| Variant | Width | Use Case |
|---------|-------|---------|
| `default` | max-w-lg (512px) | Confirmation, forms |
| `wide` | max-w-2xl (672px) | Complex forms, data display |
| `full` | max-w-4xl (896px) | Data tables, detailed views |
| `sheet` | full height, right-aligned | Side panels, detail drawers |

## Structure

```
┌─ BACKDROP (surface-glass + blur) ───────────────────────┐
│                                                          │
│   ┌─ MODAL ───────────────────────────────────────┐     │
│   │  Header: Title + Close                         │     │
│   │  ─────────────────────────────────────────────│     │
│   │  Body: Content                                 │     │
│   │  ─────────────────────────────────────────────│     │
│   │  Footer: Actions                               │     │
│   └───────────────────────────────────────────────┘     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Animation

- **Backdrop:** Fade in 200ms
- **Modal:** Entry-plug-slide (y: 24 → 0, scale: 0.96 → 1, opacity: 0 → 1, 350ms, ease-nerv)
- **Exit:** Reverse at 200ms (faster out than in)
- **Sheet:** Slide from right, 350ms, ease-nerv

## Tailwind Usage

```html
<!-- Backdrop -->
<div class="fixed inset-0 z-50
            bg-[oklch(5%_0.02_285/0.8)] backdrop-blur-sm
            flex items-center justify-center p-4">

  <!-- Modal -->
  <div class="w-full max-w-lg bg-surface-overlay border border-border-strong
              rounded-xl shadow-xl overflow-hidden">

    <!-- Header -->
    <div class="flex items-center justify-between px-6 py-4 border-b border-border">
      <h2 class="font-display text-lg font-bold uppercase tracking-wide text-on-surface">
        Confirm Deployment
      </h2>
      <button class="text-on-surface-muted hover:text-on-surface
                     transition-colors duration-200">
        <!-- Close icon -->
      </button>
    </div>

    <!-- Body -->
    <div class="px-6 py-5 text-on-surface-muted text-base">
      <p>Deploy EVA Unit-01 to sector 7? This action cannot be reversed.</p>
    </div>

    <!-- Footer -->
    <div class="flex items-center justify-end gap-3 px-6 py-4 border-t border-border">
      <button class="bg-transparent text-on-surface-muted px-4 py-2 text-sm
                     font-medium rounded-md hover:bg-surface-hover
                     transition-colors duration-200">
        Abort
      </button>
      <button class="bg-primary text-primary-foreground px-4 py-2 text-sm
                     font-medium rounded-md shadow-sm
                     hover:shadow-[0_0_20px_oklch(45%_0.28_300/0.4)]
                     transition-all duration-200">
        Deploy
      </button>
    </div>
  </div>
</div>
```
