import { raw } from "./primitives.js";
import { resolveSemantic, type Theme } from "./semantics.js";

/**
 * Component Tokens
 * - component-specific design decisions
 * - reference semantic tokens (never raw values directly)
 */
export const components = {
  button: {
    borderRadius: "radius.lg",
    paddingY: "12px",
    paddingX: "24px",
    fontSize: "1rem",
    fontWeight: 500,
    iconSpacing: "4px",

    dimensions: {
      height: "48px",
      strokeWidth: "1.5px",
    },

    contained: {
      layout: {
        default: { height: "48px", width: "auto", paddingX: "30px", paddingY: "12px" },
        withIcon: {
          height: "48px",
          width: "auto",
          paddingX: "24px",
          paddingY: "12px",
          iconGap: "4px",
        },
        iconOnly: { height: "48px", width: "48px", paddingX: "0px", paddingY: "0px" },
      },
      states: {
        enabled: { background: "brand.primary", color: "text.inverse", border: "none" },
        hover: { background: "brand.hover", color: "text.inverse", border: "none" },
        pressed: { background: "brand.pressed", color: "text.inverse", border: "none" },
        processing: { background: "ink.solid", color: "text.inverse", border: "none", cursor: "progress" },
        disabled: {
          background: "border.default",
          color: "text.muted",
          border: "none",
          cursor: "not-allowed",
        },
      },
    },

    outline: {
      layout: {
        default: { height: "48px", width: "auto", paddingX: "24px", paddingY: "12px" },
        withIcon: {
          height: "48px",
          width: "auto",
          paddingX: "24px",
          paddingY: "12px",
          iconGap: "4px",
        },
        iconOnly: { height: "48px", width: "48px", paddingX: "0px", paddingY: "0px" },
      },
      states: {
        enabled: { background: "transparent", color: "brand.primary", border: "1.5px solid brand.primary" },
        hover: { background: "brand.softBg", color: "brand.primary", border: "1.5px solid brand.primary" },
        pressed: { background: "brand.pressBg", color: "brand.primary", border: "1.5px solid brand.primary" },
        processing: {
          background: "transparent",
          color: "text.inverse",
          border: "1.5px solid brand.primary",
          cursor: "progress",
        },
        disabled: {
          background: "transparent",
          color: "text.muted",
          border: "1.5px solid border.default",
          cursor: "not-allowed",
        },
      },
    },

    text: {
      layout: {
        default: { height: "48px", width: "auto", paddingX: "16px", paddingY: "12px" },
        withIcon: {
          height: "48px",
          width: "auto",
          paddingX: "16px",
          paddingY: "12px",
          iconGap: "4px",
        },
        iconOnly: { height: "48px", width: "48px", paddingX: "0px", paddingY: "0px" },
      },
      states: {
        enabled: { background: "transparent", color: "brand.primary", border: "none" },
        hover: { background: "brand.softBg", color: "brand.primary", border: "none" },
        pressed: { background: "brand.pressBg", color: "brand.primary", border: "none" },
        processing: { background: "ink.solid", color: "text.inverse", border: "none", cursor: "progress" },
        disabled: { background: "transparent", color: "text.muted", border: "none", cursor: "not-allowed" },
      },
    },
  },
} as const;

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

const RAW_PREFIXES = ["color.", "spacing.", "radius.", "shadow.", "logo."] as const;

/**
 * Resolve component references → concrete values for a theme.
 * - references like "brand.primary" come from semantic tokens
 * - references like "radius.lg" or "color.brand.100" come from raw tokens
 */
export function resolveComponents(theme: Theme) {
  const s = resolveSemantic(theme) as unknown as Record<string, unknown>;
  return deepResolve(components, (ref) => {
    if (ref.includes("solid ")) {
      // Handle "1.5px solid brand.primary" style values.
      const parts = ref.split(" ");
      const last = parts[parts.length - 1] ?? "";
      const isRaw = RAW_PREFIXES.some((p) => last.startsWith(p));
      const resolved = isRaw ? resolvePath(raw, last) : resolvePath(s, last);
      return typeof resolved === "string" ? parts.slice(0, -1).concat(resolved).join(" ") : ref;
    }

    const isRaw = RAW_PREFIXES.some((p) => ref.startsWith(p));
    const resolved = isRaw ? resolvePath(raw, ref) : resolvePath(s, ref);
    return resolved ?? ref;
  });
}
