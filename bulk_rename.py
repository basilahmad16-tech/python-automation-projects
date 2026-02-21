from __future__ import annotations

from pathlib import Path


def bulk_rename(directory: str, prefix: str, start: int = 1) -> None:
    base = Path(directory)
    if not base.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    files = sorted([p for p in base.iterdir() if p.is_file()])
    if not files:
        print("No files found.")
        return

    counter = start
    for file in files:
        new_name = f"{prefix}_{counter:03d}{file.suffix}"
        target = file.with_name(new_name)
        file.rename(target)
        counter += 1

    print(f"Renamed {len(files)} files.")


if __name__ == "__main__":
    folder = input("Folder path: ").strip()
    prefix = input("Prefix (e.g., invoice): ").strip()
    start_str = input("Start number (default 1): ").strip()
    start_num = int(start_str) if start_str else 1
    bulk_rename(folder, prefix, start_num)