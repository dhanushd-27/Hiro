"use client";

import { ReactNode } from "react";

interface SidebarProps {
  isOpen?: boolean;
  onToggle?: () => void;
  branchName?: string;
  threads?: any[];
  selectedThreadId?: string;
  onThreadSelect?: (threadId: string) => void;
  onNewChat?: () => void;
  className?: string;
  children?: ReactNode;
  userProfile?: {
    name?: string;
    email?: string;
    avatar?: string;
  };
}

export const Sidebar = (_props: SidebarProps) => {
  return <p>Sidebar</p>;
};

