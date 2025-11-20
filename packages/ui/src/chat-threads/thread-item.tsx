"use client";

import type { Thread } from "./thread-list";

interface ThreadItemProps {
  thread: Thread;
  isSelected?: boolean;
  onClick?: () => void;
  className?: string;
}

export const ThreadItem = (_props: ThreadItemProps) => {
  return <p>ThreadItem</p>;
};

