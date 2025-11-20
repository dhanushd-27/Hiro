"use client";

interface SidebarFooterProps {
  className?: string;
  userProfile?: {
    name?: string;
    email?: string;
    avatar?: string;
  };
}

export const SidebarFooter = (_props: SidebarFooterProps) => {
  return <p>SidebarFooter</p>;
};

