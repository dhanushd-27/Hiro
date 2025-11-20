"use client";

export interface Thread {
  id: string;
  title: string;
  lastMessage?: string;
  timestamp?: Date;
  unreadCount?: number;
}

interface ThreadListProps {
  threads: Thread[];
  selectedThreadId?: string;
  onThreadSelect?: (threadId: string) => void;
  className?: string;
}

export const ThreadList = (_props: ThreadListProps) => {
  return <p>ThreadList</p>;
};

