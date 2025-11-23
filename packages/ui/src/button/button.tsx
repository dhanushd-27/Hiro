"use client";

import { CSSProperties, useState } from "react";

interface ButtonProps {
  name: string;
  variant?: "primary" | "secondary";
  action: () => void;
}

export const Button = ({
  name,
  variant = "primary",
  action,
}: ButtonProps) => {
  const [isHovered, setIsHovered] = useState(false);
  const [isActive, setIsActive] = useState(false);
  const [isFocused, setIsFocused] = useState(false);

  const baseStyles: CSSProperties = {
    padding: "10px 24px",
    borderRadius: "8px",
    fontWeight: 500,
    fontSize: "16px",
    lineHeight: "20px",
    fontFamily: "inherit",
    cursor: "pointer",
    border: "none",
    transition: "all 0.2s ease",
    outline: "none",
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    gap: "8px",
  };

  const getVariantStyles = (): CSSProperties => {
    if (variant === "primary") {
      if (isActive) {
        return {
          backgroundColor: "#0f0f0f",
          color: "#f5f5f5",
          boxShadow: "0 1px 2px rgba(0, 0, 0, 0.1)",
          transform: "scale(0.98)",
        };
      }
      if (isHovered) {
        return {
          backgroundColor: "#2a2a2a",
          color: "#f5f5f5",
          boxShadow: "0 2px 4px rgba(0, 0, 0, 0.15)",
        };
      }
      return {
        backgroundColor: "#1a1a1a", // Soft black, easier on eyes than pure black
        color: "#f5f5f5", // Soft white, easier on eyes than pure white
        boxShadow: "0 1px 2px rgba(0, 0, 0, 0.1)",
      };
    } else {
      if (isActive) {
        return {
          backgroundColor: "#dcdcdc",
          color: "#1a1a1a",
          border: "1px solid #d4d4d4",
          boxShadow: "0 1px 2px rgba(0, 0, 0, 0.05)",
          transform: "scale(0.98)",
        };
      }
      if (isHovered) {
        return {
          backgroundColor: "#e8e8e8",
          color: "#1a1a1a",
          border: "1px solid #d4d4d4",
          boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
        };
      }
      return {
        backgroundColor: "#f5f5f5", // Soft white background
        color: "#1a1a1a", // Soft black text
        border: "1px solid #e5e5e5",
        boxShadow: "0 1px 2px rgba(0, 0, 0, 0.05)",
      };
    }
  };

  const focusStyle: CSSProperties = isFocused
    ? {
        boxShadow: `0 0 0 3px ${
          variant === "primary" ? "rgba(26, 26, 26, 0.2)" : "rgba(26, 26, 26, 0.1)"
        }`,
      }
    : {};

  const combinedStyle: CSSProperties = {
    ...baseStyles,
    ...getVariantStyles(),
    ...focusStyle,
  };

  return (
    <button
      style={combinedStyle}
      onClick={action}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => {
        setIsHovered(false);
        setIsActive(false);
      }}
      onMouseDown={() => setIsActive(true)}
      onMouseUp={() => setIsActive(false)}
      onFocus={() => setIsFocused(true)}
      onBlur={() => setIsFocused(false)}
    >
      {name}
    </button>
  );
};

