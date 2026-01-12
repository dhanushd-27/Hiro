import { raw } from "./primitives.js";

/**
 * Semantic Tokens (meaning / intent)
 * These are stable roles that map → raw tokens.
 *
 * IMPORTANT:
 * - Values are references (strings) to raw tokens (ex: "color.neutral.50")
 * - Theme-aware (light/dark)
 */
export const semantic = {
  light: {
    bg: {
      primary: "color.base.lightBg",
      surface: "color.base.lightPanel",
    },

    surface: {
      default: "color.white",
      subtle: "color.neutral.50",
      disabled: "color.neutral.100",
    },

    text: {
      primary: "color.alpha.black.87",
      secondary: "color.alpha.black.65",
      disabled: "color.alpha.black.38",
      // “Muted” is a role we use across the system; map it to secondary for now.
      muted: "color.alpha.black.65",
      inverse: "color.alpha.white.87",
    },

    ink: {
      // A stable “solid ink” used for things like processing/overlay states.
      solid: "color.neutral.900",
    },

    border: {
      default: "color.base.border",
      neutral: "color.neutral.300",
      disabled: "color.neutral.200",
    },

    brand: {
      primary: "color.brand.500",
      hover: "color.brand.400",
      pressed: "color.brand.600",
      softBg: "color.brand.50",
      pressBg: "color.brand.100",
    },

    status: {
      success: "color.status.success",
      warning: "color.status.warning",
      info: "color.status.info",
      error: "color.status.error",
    },

    notification: {
      successBackground: "color.notification.successBackground",
      warningBackground: "color.notification.warningBackground",
      infoBackground: "color.notification.infoBackground",
      errorBackground: "color.notification.errorBackground",
      successText: "color.notification.successText",
      warningText: "color.notification.warningText",
      infoText: "color.notification.infoText",
      errorText: "color.notification.errorText",
    },
  },

  dark: {
    bg: {
      primary: "color.base.darkBg",
      surface: "color.base.darkPanel",
    },

    surface: {
      default: "color.neutral.800",
      subtle: "color.neutral.700",
      disabled: "color.neutral.600",
    },

    text: {
      primary: "color.alpha.white.87",
      secondary: "color.alpha.white.65",
      disabled: "color.alpha.white.30",
      muted: "color.alpha.white.65",
      inverse: "color.alpha.black.87",
    },

    ink: {
      solid: "color.neutral.900",
    },

    border: {
      default: "color.base.border",
      neutral: "color.neutral.500",
      disabled: "color.neutral.600",
    },

    brand: {
      primary: "color.brand.500",
      hover: "color.brand.400",
      pressed: "color.brand.600",
      softBg: "color.brand.50",
      pressBg: "color.brand.100",
    },

    status: {
      success: "color.status.success",
      warning: "color.status.warning",
      info: "color.status.info",
      error: "color.status.error",
    },

    notification: {
      successBackground: "color.notification.successBackground",
      warningBackground: "color.notification.warningBackground",
      infoBackground: "color.notification.infoBackground",
      errorBackground: "color.notification.errorBackground",
      successText: "color.notification.successText",
      warningText: "color.notification.warningText",
      infoText: "color.notification.infoText",
      errorText: "color.notification.errorText",
    },
  },
} as const;

export type Theme = keyof typeof semantic;

function resolvePath(obj: unknown, path: string): unknown {
  return path.split(".").reduce<unknown>((acc, key) => {
    if (acc == null) return undefined;
    if (typeof acc !== "object") return undefined;
    return (acc as Record<string, unknown>)[key];
  }, obj);
}

function deepResolve<T>(value: T, resolveString: (v: string) => unknown): unknown {
  if (typeof value === "string") return resolveString(value);
  if (Array.isArray(value)) return value.map((v) => deepResolve(v, resolveString));
  if (value && typeof value === "object") {
    const out: Record<string, unknown> = {};
    for (const [k, v] of Object.entries(value)) out[k] = deepResolve(v, resolveString);
    return out;
  }
  return value;
}

/**
 * Resolve semantic references → concrete values for a theme.
 * This is what UI components should actually consume at runtime.
 */
export function resolveSemantic(theme: Theme) {
  const refs = semantic[theme];
  return deepResolve(refs, (ref) => resolvePath(raw, ref)) as unknown as {
    [K in keyof typeof refs]: unknown;
  };
}
