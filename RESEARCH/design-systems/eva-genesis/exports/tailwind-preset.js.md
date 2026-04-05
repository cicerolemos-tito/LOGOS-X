// EVA GENESIS — Tailwind v4 Preset v1.0.0
// Palette: Deep EVA Purple + Neon Green + Entry Amber
// Usage: import evaPreset from './eva-genesis/exports/tailwind-preset'
//        export default { presets: [evaPreset] }

/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
      colors: {
        // ── Surfaces (purple-tinted voids) ──
        surface: {
          DEFAULT: 'oklch(8% 0.02 290)',
          raised: 'oklch(12% 0.02 290)',
          overlay: 'oklch(16% 0.03 290)',
          input: 'oklch(10% 0.02 290)',
          glass: 'oklch(14% 0.04 295 / 0.6)',
          hover: 'oklch(20% 0.03 290)',
        },
        'on-surface': {
          DEFAULT: 'oklch(92% 0.01 290)',
          muted: 'oklch(58% 0.02 290)',
          disabled: 'oklch(32% 0.01 290)',
        },
        border: {
          DEFAULT: 'oklch(20% 0.03 290)',
          strong: 'oklch(30% 0.04 300)',
          focus: 'oklch(52% 0.32 295)',
        },

        // ── Brand: Primary (EVA Purple — deeper, more saturated) ──
        primary: {
          DEFAULT: 'oklch(44% 0.33 295)',
          hover: 'oklch(52% 0.32 295)',
          active: 'oklch(38% 0.32 295)',
          foreground: 'oklch(92% 0.01 290)',
          muted: 'oklch(18% 0.18 295)',
        },

        // ── Brand: Secondary (Neon Green — electric) ──
        secondary: {
          DEFAULT: 'oklch(78% 0.30 145)',
          hover: 'oklch(85% 0.28 145)',
          active: 'oklch(65% 0.28 145)',
          foreground: 'oklch(8% 0.02 290)',
        },

        // ── Brand: Accent (Entry Amber) ──
        accent: {
          DEFAULT: 'oklch(78% 0.18 85)',
          hover: 'oklch(85% 0.16 85)',
          active: 'oklch(65% 0.17 85)',
          foreground: 'oklch(8% 0.02 290)',
        },

        // ── Status ──
        success: {
          DEFAULT: 'oklch(72% 0.26 145)',
          surface: 'oklch(15% 0.08 145)',
          foreground: 'oklch(82% 0.22 145)',
        },
        warning: {
          DEFAULT: 'oklch(78% 0.18 85)',
          surface: 'oklch(15% 0.07 85)',
          foreground: 'oklch(85% 0.16 85)',
        },
        error: {
          DEFAULT: 'oklch(58% 0.25 25)',
          surface: 'oklch(15% 0.08 25)',
          foreground: 'oklch(68% 0.22 25)',
        },
        info: {
          DEFAULT: 'oklch(62% 0.15 240)',
          surface: 'oklch(15% 0.06 240)',
          foreground: 'oklch(72% 0.13 240)',
        },

        // ── Primitives ──
        'void': {
          950: 'oklch(8% 0.02 290)',
          900: 'oklch(10% 0.02 290)',
          850: 'oklch(12% 0.02 290)',
          800: 'oklch(16% 0.03 290)',
          750: 'oklch(20% 0.03 290)',
          700: 'oklch(24% 0.03 295)',
          600: 'oklch(30% 0.04 300)',
          500: 'oklch(38% 0.03 290)',
          400: 'oklch(48% 0.03 290)',
          300: 'oklch(58% 0.02 290)',
          200: 'oklch(72% 0.02 290)',
          100: 'oklch(85% 0.01 290)',
          50: 'oklch(92% 0.01 290)',
        },
        'eva-purple': {
          900: 'oklch(18% 0.18 295)',
          800: 'oklch(25% 0.24 295)',
          700: 'oklch(32% 0.28 295)',
          600: 'oklch(38% 0.32 295)',
          500: 'oklch(44% 0.33 295)',
          400: 'oklch(52% 0.32 295)',
          300: 'oklch(62% 0.28 295)',
          200: 'oklch(72% 0.20 295)',
          100: 'oklch(82% 0.12 295)',
        },
        'neon-green': {
          900: 'oklch(30% 0.12 145)',
          800: 'oklch(40% 0.18 145)',
          700: 'oklch(55% 0.24 145)',
          600: 'oklch(65% 0.28 145)',
          500: 'oklch(78% 0.30 145)',
          400: 'oklch(85% 0.28 145)',
          300: 'oklch(90% 0.22 145)',
        },
        'entry-amber': {
          700: 'oklch(55% 0.15 85)',
          600: 'oklch(65% 0.17 85)',
          500: 'oklch(78% 0.18 85)',
          400: 'oklch(85% 0.16 85)',
          300: 'oklch(90% 0.12 85)',
        },
        'angel-red': {
          600: 'oklch(45% 0.22 25)',
          500: 'oklch(58% 0.25 25)',
          400: 'oklch(68% 0.22 25)',
        },
        'sync-green': {
          600: 'oklch(55% 0.20 145)',
          500: 'oklch(72% 0.26 145)',
          400: 'oklch(82% 0.22 145)',
        },
        'magi-blue': {
          600: 'oklch(48% 0.13 240)',
          500: 'oklch(62% 0.15 240)',
          400: 'oklch(72% 0.13 240)',
        },
      },

      fontFamily: {
        display: ["'Orbitron'", "'Rajdhani'", "'system-ui'", 'sans-serif'],
        sans: ["'Geist Sans'", "'Inter'", "'system-ui'", "'-apple-system'", 'sans-serif'],
        mono: ["'Geist Mono'", "'JetBrains Mono'", "'Fira Code'", "'Consolas'", 'monospace'],
      },

      fontSize: {
        xs:   ['0.6875rem',  { lineHeight: '1rem',     letterSpacing: '0.06em'  }],
        sm:   ['0.8125rem',  { lineHeight: '1.125rem', letterSpacing: '0.03em'  }],
        base: ['0.9375rem',  { lineHeight: '1.5rem',   letterSpacing: '0.01em'  }],
        lg:   ['1.0625rem',  { lineHeight: '1.625rem', letterSpacing: '0'       }],
        xl:   ['1.25rem',    { lineHeight: '1.75rem',  letterSpacing: '-0.01em' }],
        '2xl': ['1.5rem',    { lineHeight: '1.875rem', letterSpacing: '-0.02em' }],
        '3xl': ['2rem',      { lineHeight: '2.25rem',  letterSpacing: '-0.03em' }],
        '4xl': ['2.75rem',   { lineHeight: '3rem',     letterSpacing: '-0.04em' }],
        '5xl': ['3.75rem',   { lineHeight: '1',        letterSpacing: '-0.05em' }],
        '6xl': ['5rem',      { lineHeight: '1',        letterSpacing: '-0.06em' }],
      },

      spacing: {
        '0.5': '0.125rem',
        '1': '0.25rem',
        '1.5': '0.375rem',
        '2': '0.5rem',
        '3': '0.75rem',
        '4': '1rem',
        '5': '1.25rem',
        '6': '1.5rem',
        '8': '2rem',
        '10': '2.5rem',
        '12': '3rem',
        '16': '4rem',
        '20': '5rem',
        '24': '6rem',
        '32': '8rem',
      },

      borderRadius: {
        sm: '4px',
        DEFAULT: '6px',
        md: '6px',
        lg: '10px',
        xl: '12px',
      },

      boxShadow: {
        sm: '0 1px 3px oklch(5% 0.03 290 / 0.5)',
        md: '0 4px 12px oklch(5% 0.04 295 / 0.4), 0 1px 3px oklch(5% 0.03 290 / 0.3)',
        lg: '0 8px 32px oklch(5% 0.05 295 / 0.5), 0 2px 8px oklch(5% 0.03 290 / 0.3)',
        xl: '0 16px 48px oklch(5% 0.06 295 / 0.6), 0 4px 16px oklch(5% 0.04 290 / 0.4)',
        '2xl': '0 24px 64px oklch(5% 0.07 295 / 0.7), 0 8px 24px oklch(5% 0.05 290 / 0.4)',
        'glow': '0 0 20px oklch(44% 0.33 295 / 0.4), 0 0 60px oklch(44% 0.33 295 / 0.15)',
        'glow-intense': '0 0 30px oklch(52% 0.35 295 / 0.5), 0 0 80px oklch(44% 0.33 295 / 0.25)',
        'glow-danger': '0 0 20px oklch(58% 0.25 25 / 0.4), 0 0 60px oklch(58% 0.25 25 / 0.15)',
        'glow-neon': '0 0 20px oklch(78% 0.30 145 / 0.4), 0 0 60px oklch(78% 0.30 145 / 0.15)',
        'glow-neon-intense': '0 0 30px oklch(85% 0.30 145 / 0.5), 0 0 80px oklch(78% 0.30 145 / 0.25)',
        'glow-sync': '0 0 20px oklch(72% 0.26 145 / 0.4), 0 0 60px oklch(72% 0.26 145 / 0.15)',
        'glow-accent': '0 0 20px oklch(78% 0.18 85 / 0.4), 0 0 60px oklch(78% 0.18 85 / 0.15)',
        'inset-sm': 'inset 0 1px 2px oklch(5% 0.03 290 / 0.4)',
        'inset-md': 'inset 0 2px 6px oklch(5% 0.04 295 / 0.4)',
        'ring-focus': '0 0 0 2px oklch(8% 0.02 290), 0 0 0 4px oklch(52% 0.32 295 / 0.8)',
        'ring-error': '0 0 0 2px oklch(8% 0.02 290), 0 0 0 4px oklch(58% 0.25 25 / 0.8)',
      },

      transitionTimingFunction: {
        'nerv': 'cubic-bezier(0.16, 1, 0.3, 1)',
        'alert': 'cubic-bezier(0.68, -0.55, 0.27, 1.55)',
        'deploy': 'cubic-bezier(0.25, 0.46, 0.45, 0.94)',
        'spring': 'cubic-bezier(0.34, 1.56, 0.64, 1)',
      },

      transitionDuration: {
        'instant': '100ms',
        'fast': '200ms',
        'normal': '350ms',
        'slow': '600ms',
        'dramatic': '1000ms',
        'cinematic': '1500ms',
      },

      keyframes: {
        'at-field-pulse': {
          '0%, 100%': { boxShadow: '0 0 20px oklch(44% 0.33 295 / 0.3)' },
          '50%': { boxShadow: '0 0 30px oklch(52% 0.35 295 / 0.5)' },
        },
        'neon-pulse': {
          '0%, 100%': { boxShadow: '0 0 20px oklch(78% 0.30 145 / 0.3)' },
          '50%': { boxShadow: '0 0 35px oklch(85% 0.30 145 / 0.5)' },
        },
        'sync-pulse': {
          '0%, 100%': { opacity: '1', transform: 'scale(1)' },
          '50%': { opacity: '0.5', transform: 'scale(1.05)' },
        },
        'pattern-blue': {
          '0%, 100%': { backgroundColor: 'oklch(15% 0.08 25)' },
          '50%': { backgroundColor: 'oklch(20% 0.12 25)' },
        },
      },

      animation: {
        'at-field': 'at-field-pulse 2s ease-in-out infinite',
        'neon-pulse': 'neon-pulse 2s ease-in-out infinite',
        'sync-pulse': 'sync-pulse 2s ease-in-out infinite',
        'pattern-blue': 'pattern-blue 1.5s ease-in-out 2',
      },
    },
  },
};
