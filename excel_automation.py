from __future__ import annotations

from pathlib import Path
import pandas as pd


def clean_excel(input_file: str, output_file: str) -> None:
    input_path = Path(input_file)

    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_file}")

    df = pd.read_excel(input_path)

    # Remove empty rows
    df = df.dropna(how="all")

    # Strip spaces from string columns
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    output_path = Path(output_file)
    df.to_excel(output_path, index=False)

    print(f"Cleaned Excel saved to: {output_path}")


if __name__ == "__main__":
    inp = input("Enter Excel file path: ").strip()
    out = input("Enter output file name: ").strip()
    clean_excel(inp, out)