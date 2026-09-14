/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // SmartCity360 Official Municipal Palette (Royal Purple & Midnight Violet Theme)
        city: {
          purple: '#7C3AED',              // Vibrant Royal Purple - Primary Brand
          'purple-dark': '#5B21B6',       // Deep Violet for hover & active states
          'purple-light': '#C084FC',      // Electric Lilac for soft highlights
          'purple-night': '#120524',      // Deep Obsidian Purple for dark panels & sidebars
          'purple-card': '#1C0838',       // Dark purple card surface
          'purple-border': '#3D156A',     // Subtle purple border
          lavender: '#E9D5FF',            // Soft Lavender for tags & badges
          lilac: '#D8B4FE',               // Light Lilac for text accents
          
          // Re-mapped aliases so all existing components seamlessly adopt the Purple theme
          terracotta: '#7C3AED',          // Maps to Primary Purple
          'terracotta-dark': '#5B21B6',   // Maps to Purple Dark
          'terracotta-light': '#C084FC',  // Maps to Lilac
          amber: '#C084FC',               // Maps to Lilac / Bright Violet
          'amber-light': '#E9D5FF',       // Maps to Soft Lavender
          ochre: '#9333EA',               // Rich Violet
          forest: '#1A0730',              // Midnight Purple (Replaced dark forest)
          green: '#7C3AED',               // Purple brand interactive
          leaf: '#A855F7',                // Purple 500 operational accent
          sand: '#E9D5FF',                // Soft lavender neutral
          ivory: '#FAF7FD',               // Light lavender-white clean page background
          charcoal: '#120524',            // Midnight Purple base (headers, sidebars, dark cards)
          concrete: '#C4B5FD',            // Lavender concrete for borders & dividers
          sage: '#F3E8FF',                // Soft lavender surface & badge background
          danger: '#EF4444',              // Critical Emergency Red
          success: '#10B981',             // Operational Success Green
        },
        surface: {
          light: '#FFFFFF',
          card: '#FFFFFF',
          muted: '#F5EFFC',
          border: '#E4DAF2',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
      },
      boxShadow: {
        'civic': '0 1px 3px 0 rgba(124, 58, 237, 0.08), 0 1px 2px -1px rgba(124, 58, 237, 0.08)',
        'civic-md': '0 4px 6px -1px rgba(124, 58, 237, 0.12), 0 2px 4px -2px rgba(124, 58, 237, 0.08)',
        'civic-lg': '0 10px 15px -3px rgba(124, 58, 237, 0.16), 0 4px 6px -4px rgba(124, 58, 237, 0.1)',
      },
      borderRadius: {
        'civic': '10px',
      }
    },
  },
  plugins: [],
}

