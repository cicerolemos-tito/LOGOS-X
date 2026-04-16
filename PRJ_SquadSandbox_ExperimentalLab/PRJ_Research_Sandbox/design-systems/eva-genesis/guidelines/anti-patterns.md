# EVA GENESIS — Anti-Patterns

Common mistakes when implementing this design system. Each anti-pattern includes what to do instead.

---

## 1. The Generic Dark Theme

**Wrong:** Using Tailwind's default `gray-900` / `gray-800` backgrounds.
**Why it fails:** Default grays have no personality. EVA GENESIS uses purple-tinted voids.
**Fix:** Use `surface` / `surface-raised` / `surface-overlay` which reference the void-* scale with purple undertones.

## 2. The Missing Glow

**Wrong:** Interactive elements with plain borders and no glow effects.
**Why it fails:** The AT Field glow is the signature of this design system. Without it, buttons and cards look like any dark theme.
**Fix:** Apply `shadow-glow` on hover for primary elements. Use `ring-focus` for keyboard focus states.

## 3. The Light Mode Escape

**Wrong:** Adding a light mode toggle or using white backgrounds anywhere.
**Why it fails:** Every color, shadow, and contrast ratio is calibrated for dark surfaces. Light mode breaks all of it.
**Fix:** There is no light mode. The darkness IS the design decision. If you need light, use a different DS.

## 4. The Rounded Corner Inflation

**Wrong:** `rounded-2xl`, `rounded-3xl`, or large border radius values.
**Why it fails:** EVA GENESIS is angular and tactical. Excessive rounding makes it feel soft and consumer-app-like.
**Fix:** Max radius is `radius-xl` (12px) for large containers. Default is `radius-md` (6px). Use `radius-full` only for pills/avatars.

## 5. The Decorative Gradient

**Wrong:** Multi-color gradients as backgrounds or card fills.
**Why it fails:** Gradients in EVA GENESIS are reserved for glow effects (radial-gradient for hero backgrounds, box-shadow for AT Field).
**Fix:** Use solid surface tokens for backgrounds. Gradients only appear as subtle radial glows behind hero text or as glow shadows.

## 6. The Data Sans-Serif

**Wrong:** Displaying numbers, timestamps, or IDs in the sans-serif font.
**Why it fails:** Mono-spaced fonts ensure data columns align. Sans-serif numbers look amateur in a command interface.
**Fix:** Always use `font-mono` + `tabular-nums` for any numeric or data content.

## 7. The Slow Ease

**Wrong:** Using `transition-all duration-500 ease-in-out` on everything.
**Why it fails:** Default CSS easing feels sluggish. EVA GENESIS uses specific curves that feel decisive.
**Fix:** Use `ease-nerv` (cubic-bezier(0.16, 1, 0.3, 1)) and `duration-fast` (200ms) for micro-interactions. Reserve `duration-slow`+ for page-level animations.

## 8. The Flat Button

**Wrong:** Buttons without any shadow or glow on any state.
**Why it fails:** Buttons need to feel like control panel switches — they have depth and react to touch.
**Fix:** Default buttons get `shadow-sm`. Hover gets the glow variant. Active gets `scale(0.97)`.

## 9. The Missing Status Semantics

**Wrong:** Using `primary` color for success indicators, or `text-green-500` for status.
**Why it fails:** Status colors have their own semantic tokens with matching surfaces and foregrounds.
**Fix:** Use `success` / `success-surface` / `success-foreground` for positive states. Same pattern for warning, error, info.

## 10. The Animation Overload

**Wrong:** Every element has a complex entrance animation, parallax, and glow.
**Why it fails:** When everything is dramatic, nothing is dramatic. Cinematic motion requires restraint.
**Fix:** Reserve dramatic animations (>600ms) for hero sections and page transitions. Use `duration-fast` for UI feedback. Stagger children, don't animate everything simultaneously.
