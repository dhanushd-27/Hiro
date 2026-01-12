import { Header } from "../components";
import { ChatInput } from "@repo/ui/input";

export default function Home() {
  return (
    <div className="page-container">
      <Header />
      <main className="main-content">
        <div className="hero-section">
          <h1 className="hero-title">Ready when you are.</h1>
        </div>
        <div className="chat-input-section">
          <ChatInput placeholder="Ask anything" />
        </div>
      </main>
    </div>
  );
}
