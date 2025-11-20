"use client";

import { UserProfile } from "../profile";

interface SidebarFooterProps {
  className?: string;
  userProfile?: {
    name?: string;
    email?: string;
    avatar?: string;
  };
}

export const SidebarFooter = ({ className = "", userProfile }: SidebarFooterProps) => {
  return (
    <div className={`sidebar-footer border-t border-gray-200 p-4 ${className}`}>
      <UserProfile
        name={userProfile?.name}
        email={userProfile?.email}
        avatar={userProfile?.avatar}
      />
    </div>
  );
};

