import { Header } from "../components";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex flex-1 flex-col items-center justify-center">
        {/* Main content goes here */}
      </main>
    </div>
  );
}
