export const typography = {
  fontFamily: {
    base: "'Figtree', Arial, sans-serif",
    brand: "'alro-bold', sans-serif",
  },

  fontWeight: {
    light: 300,
    regular: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
  },

  /**
   * Responsive font sizes (mobile/tablet/desktop + clamp)
   * Theme-invariant, so this can stay as a stable system contract.
   */
  fontSize: {
    h1: {
      mobile: "2.5rem",
      tablet: "3.5rem",
      desktop: "4.5rem",
      clamp: "clamp(2.5rem, 5vw + 1rem, 4.5rem)",
    },
    h2: {
      mobile: "2.25rem",
      tablet: "3.25rem",
      desktop: "4.25rem",
      clamp: "clamp(2.25rem, 4.5vw + 1rem, 4.25rem)",
    },
    h3: {
      mobile: "1.75rem",
      tablet: "2.25rem",
      desktop: "3rem",
      clamp: "clamp(1.75rem, 3vw + 0.5rem, 3rem)",
    },
    h4: {
      mobile: "1.5rem",
      tablet: "1.75rem",
      desktop: "2rem",
      clamp: "clamp(1.5rem, 2vw + 0.5rem, 2rem)",
    },
    subtitle: {
      mobile: "0.875rem",
      tablet: "0.9375rem",
      desktop: "1rem",
      clamp: "clamp(0.875rem, 0.5vw + 0.5rem, 1rem)",
    },
    paragraph: {
      mobile: "0.875rem",
      tablet: "0.875rem",
      desktop: "1rem",
      clamp: "clamp(0.875rem, 0.5vw + 0.75rem, 1rem)",
    },
    body: {
      mobile: "0.75rem",
      tablet: "0.8125rem",
      desktop: "0.875rem",
      clamp: "clamp(0.75rem, 0.3vw + 0.6rem, 0.875rem)",
    },
    small: {
      mobile: "0.6875rem",
      tablet: "0.6875rem",
      desktop: "0.75rem",
      clamp: "clamp(0.6875rem, 0.2vw + 0.6rem, 0.75rem)",
    },
  },

  lineHeight: {
    h1: { mobile: "1.2", tablet: "1.15", desktop: "1.1" },
    h2: { mobile: "1.25", tablet: "1.2", desktop: "1.15" },
    h3: { mobile: "1.3", tablet: "1.25", desktop: "1.2" },
    h4: { mobile: "1.35", tablet: "1.3", desktop: "1.25" },
    subtitle: { mobile: "1.5", tablet: "1.5", desktop: "1.5" },
    paragraph: { mobile: "1.6", tablet: "1.55", desktop: "1.5" },
    body: { mobile: "1.6", tablet: "1.55", desktop: "1.5" },
    small: { mobile: "1.5", tablet: "1.5", desktop: "1.5" },
  },

  letterSpacing: {
    h1: "-0.02em",
    h2: "-0.02em",
    h3: "-0.01em",
    h4: "normal",
    subtitle: "normal",
    paragraph: "normal",
    body: "normal",
    small: "0.01em",
  },

  maxLineWidth: {
    heading: "20ch",
    paragraph: "65ch",
    wide: "80ch",
  },
} as const;
