"use client";

import type { Thread } from "../chat-threads";

interface ThreadsListProps {
  threads: Thread[];
  selectedThreadId?: string;
  onThreadSelect?: (threadId: string) => void;
  className?: string;
}

export const ThreadsList = (_props: ThreadsListProps) => {
  return <p>ThreadsList</p>;
};

