"use client";

interface ChatInputProps {
  onSend?: (message: string, agentId?: string) => void;
  placeholder?: string;
  className?: string;
  disabled?: boolean;
}

export const ChatInput = (_props: ChatInputProps) => {
  return <p>ChatInput</p>;
};

