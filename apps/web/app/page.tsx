import Link from "next/link";

export default function Home() {
  return (
    <main className="flex min-h-screen items-center justify-center">
      <p className="text-xl font-semibold">Home</p>
      <Link href="/chat">Chat</Link>
    </main>
  );
}
