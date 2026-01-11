// design-tokens/typography.ts

export const typography = {
  fontFamily: {
    base: "'Inter', system-ui, sans-serif",
    mono: "'JetBrains Mono', monospace",
  },

  fontWeight: {
    regular: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
  },

  fontSize: {
    heading: {
      h1: {
        clamp: "clamp(2.5rem, 5vw + 1rem, 4.5rem)",
        lineHeight: "1.1",
        letterSpacing: "-0.02em",
      },
      h2: {
        clamp: "clamp(2rem, 4vw + 1rem, 3.5rem)",
        lineHeight: "1.15",
        letterSpacing: "-0.02em",
      },
      h3: {
        clamp: "clamp(1.5rem, 3vw + 0.5rem, 2.5rem)",
        lineHeight: "1.2",
      },
    },

    body: {
      lg: {
        size: "1rem",
        lineHeight: "1.6",
      },
      md: {
        size: "0.875rem",
        lineHeight: "1.6",
      },
      sm: {
        size: "0.75rem",
        lineHeight: "1.5",
      },
    },
  },

  maxWidth: {
    reading: "65ch",
    wide: "80ch",
  },
} as const;
