"use client";

import { useState } from "react";
import { AgentDropdown } from "./agent-dropdown";

interface ChatInputProps {
  onSend?: (message: string, agentId?: string) => void;
  placeholder?: string;
  className?: string;
  disabled?: boolean;
}

export const ChatInput = ({
  onSend,
  placeholder = "Type your message...",
  className = "",
  disabled = false,
}: ChatInputProps) => {
  const [message, setMessage] = useState("");
  const [selectedAgent, setSelectedAgent] = useState<string | undefined>();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim()) {
      onSend?.(message, selectedAgent);
      setMessage("");
    }
  };

  return (
    <form onSubmit={handleSubmit} className={`chat-input flex items-center gap-2 ${className}`}>
      <AgentDropdown
        selectedAgent={selectedAgent}
        onAgentChange={setSelectedAgent}
      />
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder={placeholder}
        disabled={disabled}
        className="flex-1 px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
      />
      <button
        type="submit"
        className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
        disabled={!message.trim() || disabled}
      >
        Send
      </button>
    </form>
  );
};

