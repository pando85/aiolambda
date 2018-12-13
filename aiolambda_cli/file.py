from pathlib import Path


def save_to_file(content: str, path: Path) -> str:
    with open(str(path), 'w') as file:
        file.write(content)
    return content
