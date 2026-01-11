// design-tokens/primitives.ts

export const primitives = {
  color: {
    blue: {
      500: "#3754ED", // Brand / Primary
    },

    base: {
      lightBg: "#EEF3F7",
      lightSurface: "#F7FDFF",
      darkBg: "#080E29",
      darkSurface: "#131B62",
    },

    text: {
      light: "#080E29",
      dark: "#F7FDFF",
    },
  },

  opacity: {
    textSecondaryLight: 0.7,
    textMutedLight: 0.5,
    borderLight: 0.1,
    focusLight: 0.25,

    textSecondaryDark: 0.75,
    textMutedDark: 0.55,
    borderDark: 0.125,
    focusDark: 0.4,
  },

  spacing: {
    xs: 4,
    sm: 8,
    md: 16,
    lg: 24,
    xl: 32,
  },

  radius: {
    sm: "4px",
    md: "8px",
    lg: "16px",
    pill: "999px",
  },

  typography: {
    fontFamily: {
      base: "'Inter', system-ui, sans-serif",
    },
    fontWeight: {
      regular: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
    },
  },

  motion: {
    duration: {
      fast: "150ms",
      normal: "250ms",
      slow: "400ms",
    },
    easing: {
      standard: "cubic-bezier(0.4, 0, 0.2, 1)",
    },
  },
} as const;
