/**
 * Raw Tokens (aka Primitive Tokens)
 * - context-free values (no theme logic, no component meaning)
 * - safe to share across platforms
 */
export const raw = {
  logo: {
    src: "waku.png",
  },

  color: {
    /**
     * Brand scale (Blue Ribbon)
     * Keep this as a scale so semantic roles can pick levels (600/500/etc).
     */
    brand: {
      50: "#F0F3FE",
      100: "#DCE3FD",
      200: "#C2CEFB",
      300: "#97AFF9",
      400: "#6787F3",
      500: "#3754ED",
      600: "#2D3EE3",
      700: "#252CD0",
      800: "#2426A9",
      900: "#232685",
      950: "#1A1A51",
    },

    neutral: {
      50: "#F9F9F9",
      100: "#E5E5E5",
      200: "#D0D0D0",
      300: "#BCBCBC",
      400: "#A7A7A7",
      500: "#868686",
      600: "#646464",
      700: "#4C4C4C",
      800: "#333333",
      900: "#000000",
    },

    base: {
      /**
       * App surfaces / backgrounds provided by design.
       * These are not part of the neutral scale, so we keep them separate.
       */
      lightBg: "#F7FDFF",
      lightPanel: "#EEF3F7",
      darkBg: "#080E29",
      darkPanel: "#131B62",
      border: "#2F2F2F",
      disabledText: "#3C3C3C",
    },

    common: {
      white: "#FFFFFF",
      black: "#000000",
    },

    /**
     * Alpha “colors” as CSS strings (still raw + context-free).
     * This keeps semantic tokens as references (no computed strings needed).
     */
    alpha: {
      white: {
        87: "rgb(255 255 255 / 0.87)",
        65: "rgb(255 255 255 / 0.65)",
        30: "rgb(255 255 255 / 0.3)",
      },
      black: {
        87: "rgb(0 0 0 / 0.87)",
        65: "rgb(0 0 0 / 0.65)",
        38: "rgb(0 0 0 / 0.38)",
      },
    },

    /**
     * Extra brand-adjacent values that aren't part of the scale,
     * but are used for gradients / pressed states.
     */
    brandAccent: {
      // Kept for backwards-compat; for this palette, prefer `color.brand.*`
      light: "#F7FDFF",
      mid: "#3754ED",
      dark: "#131B62",
    },

    gradient: {
      start: "#F7FDFF",
      via1: "#3754ED",
      via2: "#131B62",
      end: "#080E29",
    },

    status: {
      success: "#51CC56",
      warning: "#FEB63D",
      info: "#5B93FF",
      error: "#FF5555",
    },

    notification: {
      successBackground: "#DFF6E2",
      warningBackground: "#FFF6DD",
      infoBackground: "#E7F0FF",
      errorBackground: "#FFE7E7",
      successText: "#218838",
      warningText: "#B26A00",
      infoText: "#0353B6",
      errorText: "#C1272D",
    },
  },

  shadow: {
    xs: "0 1px 2px 0 rgba(16, 24, 40, 0.05)",
    sm: "0px 2px 4px 0px rgba(11, 10, 55, 0.15)",
    md: "0px 4px 10px 0px rgba(18, 16, 99, 0.09)",
    lg: "0px 8px 20px 0px rgba(18, 16, 99, 0.06)",
  },

  spacing: {
    xxs: 4,
    xs: 8,
    sm: 12,
    md: 16,
    lg: 24,
    xl: 32,
    xxl: 40,
  },

  radius: {
    none: "0px",
    sm: "4px",
    md: "8px",
    lg: "16px",
    pill: "999px",
  },
} as const;

// Backwards-friendly alias (many codebases expect `primitives`)
export const primitives = raw;
