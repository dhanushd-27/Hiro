"use client";

import { useState, useEffect, useRef } from "react";
import { Sidebar } from "./sidebar";
import { ChatInput } from "./input";
import type { Thread } from "./chat-threads";

export interface Message {
  id: string;
  content: string;
  role: "user" | "assistant";
  timestamp: Date;
  agentId?: string;
}

export interface ChatPageProps {
  initialThreads?: Thread[];
  initialMessages?: Record<string, Message[]>;
  branchName?: string;
  onSendMessage?: (message: string, threadId: string, agentId?: string) => Promise<Message | void>;
  onNewThread?: (threadId: string) => void;
  onThreadSelect?: (threadId: string) => void;
  userProfile?: {
    name?: string;
    email?: string;
    avatar?: string;
  };
  className?: string;
}

export const ChatPage = ({
  initialThreads = [],
  initialMessages = {},
  branchName = "main",
  onSendMessage,
  onNewThread,
  onThreadSelect,
  userProfile,
  className = "",
}: ChatPageProps) => {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [selectedThreadId, setSelectedThreadId] = useState<string | undefined>(
    initialThreads[0]?.id
  );
  const [messages, setMessages] = useState<Record<string, Message[]>>(initialMessages);
  const [threads, setThreads] = useState<Thread[]>(initialThreads);
  const [isLoading, setIsLoading] = useState(false);

  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [selectedThreadId, messages]);

  const handleSendMessage = async (message: string, agentId?: string) => {
    if (!selectedThreadId) return;

    const newMessage: Message = {
      id: `${selectedThreadId}-${Date.now()}`,
      content: message,
      role: "user",
      timestamp: new Date(),
      agentId,
    };

    // Add user message immediately
    setMessages((prev) => ({
      ...prev,
      [selectedThreadId]: [...(prev[selectedThreadId] || []), newMessage],
    }));

    // Update thread with last message
    setThreads((prev) =>
      prev.map((thread) =>
        thread.id === selectedThreadId
          ? {
              ...thread,
              lastMessage: message,
              timestamp: new Date(),
              unreadCount: 0,
            }
          : thread
      )
    );

    // Call the onSendMessage callback if provided
    if (onSendMessage) {
      setIsLoading(true);
      try {
        const response = await onSendMessage(message, selectedThreadId, agentId);
        if (response) {
          setMessages((prev) => ({
            ...prev,
            [selectedThreadId]: [...(prev[selectedThreadId] || []), response],
          }));

          setThreads((prev) =>
            prev.map((thread) =>
              thread.id === selectedThreadId
                ? {
                    ...thread,
                    lastMessage: response.content,
                    timestamp: new Date(),
                  }
                : thread
            )
          );
        }
      } catch (error) {
        console.error("Error sending message:", error);
        // Optionally add an error message
        const errorMessage: Message = {
          id: `${selectedThreadId}-error-${Date.now()}`,
          content: "Sorry, there was an error sending your message. Please try again.",
          role: "assistant",
          timestamp: new Date(),
        };
        setMessages((prev) => ({
          ...prev,
          [selectedThreadId]: [...(prev[selectedThreadId] || []), errorMessage],
        }));
      } finally {
        setIsLoading(false);
      }
    }
  };

  const handleNewChat = () => {
    const newThreadId = Date.now().toString();
    const newThread: Thread = {
      id: newThreadId,
      title: "New Chat",
      timestamp: new Date(),
    };
    setThreads([newThread, ...threads]);
    setSelectedThreadId(newThreadId);
    setMessages((prev) => ({ ...prev, [newThreadId]: [] }));
    onNewThread?.(newThreadId);
  };

  const handleThreadSelect = (threadId: string) => {
    setSelectedThreadId(threadId);
    onThreadSelect?.(threadId);
  };

  const selectedThread = threads.find((t) => t.id === selectedThreadId);
  const threadMessages = selectedThreadId ? messages[selectedThreadId] || [] : [];

  return (
    <div className={`flex h-screen overflow-hidden bg-gray-50 ${className}`}>
      {/* Sidebar */}
      <Sidebar
        isOpen={sidebarOpen}
        onToggle={() => setSidebarOpen(!sidebarOpen)}
        branchName={branchName}
        threads={threads}
        selectedThreadId={selectedThreadId}
        onThreadSelect={handleThreadSelect}
        onNewChat={handleNewChat}
        className="w-80 flex-shrink-0"
        userProfile={userProfile}
      />

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col overflow-hidden bg-white">
        {/* Chat Header */}
        {selectedThread && (
          <div className="border-b border-gray-200 px-6 py-4 bg-white">
            <h1 className="text-xl font-semibold text-gray-900">
              {selectedThread.title}
            </h1>
            {selectedThread.lastMessage && (
              <p className="text-sm text-gray-500 mt-1 line-clamp-1">
                {selectedThread.lastMessage}
              </p>
            )}
          </div>
        )}

        {/* Messages Area */}
        <div className="flex-1 overflow-y-auto px-6 py-4">
          {selectedThreadId ? (
            <div className="max-w-4xl mx-auto space-y-4">
              {threadMessages.length === 0 ? (
                <div className="text-center text-gray-500 py-12">
                  <p className="text-lg font-medium mb-2">Start a conversation</p>
                  <p className="text-sm">Select an agent and type your message below</p>
                </div>
              ) : (
                <>
                  {threadMessages.map((message) => (
                    <MessageBubble key={message.id} message={message} />
                  ))}
                  {isLoading && (
                    <div className="flex justify-start">
                      <div className="bg-gray-100 text-gray-900 rounded-lg px-4 py-2">
                        <div className="flex items-center gap-2">
                          <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" />
                          <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:0.2s]" />
                          <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:0.4s]" />
                        </div>
                      </div>
                    </div>
                  )}
                  <div ref={messagesEndRef} />
                </>
              )}
            </div>
          ) : (
            <div className="flex items-center justify-center h-full">
              <div className="text-center text-gray-500">
                <p className="text-lg font-medium mb-2">No thread selected</p>
                <p className="text-sm">
                  Select a thread from the sidebar or create a new chat
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Input Box */}
        {selectedThreadId && (
          <div className="border-t border-gray-200 px-6 py-4 bg-white">
            <div className="max-w-4xl mx-auto">
              <ChatInput
                onSend={handleSendMessage}
                placeholder="Type your message..."
                disabled={isLoading}
              />
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

interface MessageBubbleProps {
  message: Message;
}

const MessageBubble = ({ message }: MessageBubbleProps) => {
  return (
    <div
      className={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}
    >
      <div
        className={`max-w-[80%] rounded-lg px-4 py-2 ${
          message.role === "user"
            ? "bg-blue-500 text-white"
            : "bg-gray-100 text-gray-900"
        }`}
      >
        <p className="text-sm whitespace-pre-wrap">{message.content}</p>
        <p
          className={`text-xs mt-1 ${
            message.role === "user" ? "text-blue-100" : "text-gray-500"
          }`}
        >
          {message.timestamp.toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          })}
        </p>
      </div>
    </div>
  );
};

