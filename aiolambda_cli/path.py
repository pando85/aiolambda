from functools import partial
from pathlib import Path

from aiolambda.functools import compose


def dest_from_template(template_base: Path, dest_dir: Path, template_path: Path) -> Path:
    def remove(remove: str, base: str) -> str:
        return base.replace(remove + '/', '')

    def add_path(base: Path, tail: Path):
        return base / tail

    remove_base = partial(remove, str(template_base))
    remove_j2 = partial(remove, '.j2')
    add_dest_dir = partial(add_path, dest_dir)

    return compose(
        remove_base,
        remove_j2,
        Path,
        add_dest_dir
    )(str(template_path))
