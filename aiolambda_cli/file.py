from pathlib import Path


def ensure_blank_line(file_content: str) -> str:
    if file_content.split('\n')[-1:] == ['']:
        return file_content
    return f'{file_content}\n'


def save_to_file(content: str, path: Path) -> str:
    with open(str(path), 'w') as file:
        file.write(ensure_blank_line(content))
    return content
