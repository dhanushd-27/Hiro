import Image from "next/image";
import { Github } from "lucide-react";
import { hiroLogo } from "@repo/assets";
import { ThemeToggler } from "../theme-toggler";
import styles from "./header.module.css";

export function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.left}>
        <Image alt="Hiro" height={32} priority src={hiroLogo} width={32} />
      </div>
      <div className={styles.right}>
        <ThemeToggler />
        <a
          href="https://github.com/dhanushd-27/Hiro"
          target="_blank"
          rel="noopener noreferrer"
          className="icon-button"
          aria-label="View on GitHub"
        >
          <Github size={20} />
        </a>
      </div>
    </header>
  );
}
