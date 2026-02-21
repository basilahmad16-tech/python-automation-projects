from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path


def backup_folder(source_dir: str, backup_root: str) -> None:
    src = Path(source_dir)
    if not src.exists():
        raise FileNotFoundError(f"Source folder not found: {source_dir}")

    root = Path(backup_root)
    root.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = root / f"{src.name}_backup_{timestamp}"

    shutil.copytree(src, dest)
    print(f"Backup created: {dest}")


if __name__ == "__main__":
    src = input("Source folder path: ").strip()
    dest_root = input("Backup root folder path: ").strip()
    backup_folder(src, dest_root)