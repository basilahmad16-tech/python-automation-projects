from pathlib import Path


def organize_files_by_extension(directory: str) -> None:
    base_path: Path = Path(directory)

    if not base_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    for file in base_path.iterdir():
        if file.is_file():
            extension: str = file.suffix.lower().replace(".", "")
            if not extension:
                extension = "no_extension"

            target_folder: Path = base_path / extension
            target_folder.mkdir(exist_ok=True)

            new_path: Path = target_folder / file.name
            file.rename(new_path)


if __name__ == "__main__":
    folder_path: str = input("Enter folder path to organize: ").strip()
    organize_files_by_extension(folder_path)
    print("Files organized successfully.")