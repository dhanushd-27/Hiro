"use client";

interface UserProfileProps {
  name?: string;
  email?: string;
  avatar?: string;
  onProfileClick?: () => void;
  className?: string;
}

export const UserProfile = (_props: UserProfileProps) => {
  return <p>UserProfile</p>;
};

