"use client";

import { useState, useRef, useCallback, useEffect, type KeyboardEvent, type ChangeEvent } from "react";

interface ChatInputProps {
  onSend?: (message: string) => void;
  placeholder?: string;
  className?: string;
  disabled?: boolean;
  maxRows?: number;
}

// Plus icon for attachments
const PlusIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 5V19M5 12H19" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

// Send icon (arrow up)
const SendIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M7 11L12 6L17 11M12 18V7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

export const ChatInput = ({
  onSend,
  placeholder = "Ask anything",
  className = "",
  disabled = false,
  maxRows = 6,
}: ChatInputProps) => {
  const [message, setMessage] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const adjustHeight = useCallback(() => {
    const textarea = textareaRef.current;
    if (!textarea) return;

    textarea.style.height = "auto";
    const lineHeight = parseInt(getComputedStyle(textarea).lineHeight) || 24;
    const maxHeight = lineHeight * maxRows;
    const newHeight = Math.min(textarea.scrollHeight, maxHeight);
    textarea.style.height = `${newHeight}px`;
    
    // Show scrollbar only when content exceeds max height
    textarea.style.overflowY = textarea.scrollHeight > maxHeight ? "auto" : "hidden";
  }, [maxRows]);

  useEffect(() => {
    adjustHeight();
  }, [message, adjustHeight]);

  const handleSend = useCallback(() => {
    const trimmed = message.trim();
    if (!trimmed || disabled) return;

    onSend?.(trimmed);
    setMessage("");

    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
      textareaRef.current.style.overflowY = "hidden";
    }
  }, [message, disabled, onSend]);

  const handleKeyDown = useCallback(
    (e: KeyboardEvent<HTMLTextAreaElement>) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        handleSend();
      }
    },
    [handleSend]
  );

  const handleChange = useCallback((e: ChangeEvent<HTMLTextAreaElement>) => {
    setMessage(e.target.value);
  }, []);

  const canSend = message.trim().length > 0 && !disabled;

  return (
    <div className={`chat-input-container ${className}`}>
      <div className={`chat-input-wrapper ${disabled ? "chat-input-disabled" : ""}`}>
        {/* Attach button */}
        <button
          type="button"
          className="chat-input-icon-button chat-input-attach"
          aria-label="Attach file"
          disabled={disabled}
        >
          <PlusIcon />
        </button>

        {/* Textarea */}
        <textarea
          ref={textareaRef}
          value={message}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          disabled={disabled}
          rows={1}
          className="chat-input-textarea"
          aria-label="Message input"
        />

        {/* Send button */}
        <button
          type="button"
          onClick={handleSend}
          disabled={!canSend}
          className={`chat-input-send-button ${canSend ? "chat-input-send-active" : ""}`}
          aria-label="Send message"
        >
          <SendIcon />
        </button>
      </div>
    </div>
  );
};

