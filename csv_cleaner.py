from __future__ import annotations

import csv
from pathlib import Path


def clean_csv(input_path: str, output_path: str) -> None:
    src = Path(input_path)
    if not src.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    rows_written = 0
    with src.open("r", newline="", encoding="utf-8") as f_in, Path(output_path).open(
        "w", newline="", encoding="utf-8"
    ) as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        for row in reader:
            cleaned = [cell.strip() for cell in row]
            if any(cleaned):  # skip fully empty rows
                writer.writerow(cleaned)
                rows_written += 1

    print(f"Cleaned CSV saved. Rows written: {rows_written}")


if __name__ == "__main__":
    inp = input("Input CSV path: ").strip()
    out = input("Output CSV path: ").strip()
    clean_csv(inp, out)