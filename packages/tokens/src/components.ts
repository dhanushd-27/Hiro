// design-tokens/components.ts
import { semantic } from "./semantics.js";
import { primitives } from "./primitives.js";

export const components = {
  button: {
    base: {
      height: "48px",
      radius: primitives.radius.lg,
      fontWeight: primitives.typography.fontWeight.medium,
      paddingX: primitives.spacing.lg,
    },

    variants: {
      primary: {
        enabled: {
          bg: semantic.light.brand.primary,
          text: semantic.light.text.inverse,
        },
        hover: {
          bg: semantic.light.brand.primary,
        },
        disabled: {
          bg: semantic.light.border.subtle,
          text: semantic.light.text.muted,
        },
      },
    },
  },

  card: {
    base: {
      radius: primitives.radius.lg,
      padding: primitives.spacing.lg,
      bg: semantic.light.bg.surface,
      border: semantic.light.border.subtle,
    },
  },

  input: {
    base: {
      height: "44px",
      radius: primitives.radius.md,
      bg: semantic.light.bg.surface,
      text: semantic.light.text.primary,
      border: semantic.light.border.subtle,
      focusBorder: semantic.light.border.focus,
    },
  },
} as const;
