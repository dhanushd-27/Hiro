"use client";

import { ReactNode } from "react";
import { SidebarHeader } from "./sidebar-header";
import { ThreadsList } from "./threads-list";
import { NewChatButton } from "./new-chat-button";
import { SidebarFooter } from "./sidebar-footer";

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

export const Sidebar = ({
  isOpen = true,
  onToggle,
  branchName = "main",
  threads = [],
  selectedThreadId,
  onThreadSelect,
  onNewChat,
  className = "",
  children,
  userProfile,
}: SidebarProps) => {
  if (!isOpen) {
    return (
      <button
        onClick={onToggle}
        className="fixed left-0 top-0 z-50 p-2 bg-gray-100 hover:bg-gray-200 rounded-r-lg"
      >
        <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
        </svg>
      </button>
    );
  }

  return (
    <aside
      className={`sidebar flex flex-col h-full bg-white border-r border-gray-200 ${className}`}
    >
      <SidebarHeader branchName={branchName} onToggle={onToggle} />
      
      <div className="flex-1 overflow-y-auto p-4">
        <NewChatButton onClick={onNewChat} />
        <div className="mt-4">
          <ThreadsList
            threads={threads}
            selectedThreadId={selectedThreadId}
            onThreadSelect={onThreadSelect}
          />
        </div>
        {children}
      </div>

      <SidebarFooter userProfile={userProfile} />
    </aside>
  );
};

