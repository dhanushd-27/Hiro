import { raw } from "./primitives.js";
import { resolveComponents } from "./components.js";
import { resolveSemantic, type Theme } from "./semantics.js";
import { typography } from "./typography.js";
import { breakpoints } from "./breakpoints.js";

export { raw, primitives } from "./primitives.js";
export { semantic, resolveSemantic } from "./semantics.js";
export { components, resolveComponents } from "./components.js";
export { typography } from "./typography.js";
export { breakpoints } from "./breakpoints.js";

export type { Theme } from "./semantics.js";

/**
 * Convenience: resolved tokens for a theme (what UI should consume).
 */
export function createTokens(theme: "light" | "dark") {
  return {
    raw,
    semantic: resolveSemantic(theme),
    components: resolveComponents(theme),
    typography,
    breakpoints,
  } as const;
}

