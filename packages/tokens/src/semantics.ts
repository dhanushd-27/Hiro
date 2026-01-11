// design-tokens/semantic.ts
import { primitives } from "./primitives.js";

export const semantic = {
  light: {
    bg: {
      primary: primitives.color.base.lightBg,
      surface: primitives.color.base.lightSurface,
    },

    text: {
      primary: primitives.color.text.light,
      secondary: `rgb(8 14 41 / ${primitives.opacity.textSecondaryLight})`,
      muted: `rgb(8 14 41 / ${primitives.opacity.textMutedLight})`,
      inverse: primitives.color.text.dark,
    },

    border: {
      subtle: `rgb(8 14 41 / ${primitives.opacity.borderLight})`,
      focus: `rgb(55 84 237 / ${primitives.opacity.focusLight})`,
    },

    brand: {
      primary: primitives.color.blue[500],
    },
  },

  dark: {
    bg: {
      primary: primitives.color.base.darkBg,
      surface: primitives.color.base.darkSurface,
    },

    text: {
      primary: primitives.color.text.dark,
      secondary: `rgb(247 253 255 / ${primitives.opacity.textSecondaryDark})`,
      muted: `rgb(247 253 255 / ${primitives.opacity.textMutedDark})`,
      inverse: primitives.color.text.light,
    },

    border: {
      subtle: `rgb(247 253 255 / ${primitives.opacity.borderDark})`,
      focus: `rgb(55 84 237 / ${primitives.opacity.focusDark})`,
    },

    brand: {
      primary: primitives.color.blue[500],
    },
  },
} as const;
