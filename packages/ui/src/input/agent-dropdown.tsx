"use client";

export interface Agent {
  id: string;
  name: string;
  description?: string;
}

interface AgentDropdownProps {
  selectedAgent?: string;
  onAgentChange?: (agentId: string | undefined) => void;
  agents?: Agent[];
  className?: string;
}

export const AgentDropdown = (_props: AgentDropdownProps) => {
  return <p>AgentDropdown</p>;
};

