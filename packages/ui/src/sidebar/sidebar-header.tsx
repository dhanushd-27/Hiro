"use client";

interface SidebarHeaderProps {
  branchName?: string;
  onToggle?: () => void;
  className?: string;
}

export const SidebarHeader = (_props: SidebarHeaderProps) => {
  return <p>SidebarHeader</p>;
};

