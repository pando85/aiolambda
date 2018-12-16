from functools import partial
from pathlib import Path

from aiolambda.functools import compose

MARKER_PROJECT_NAME = '__PROJECT_NAME__'


def dest_from_template(template_base: Path, dest_dir: Path, template_path: Path) -> Path:
    def remove(remove: str, base: str) -> str:
        return base.replace(remove, '')

    def replace(replace_src: str, replace_dest: str, base: str) -> str:
        return base.replace(replace_src, replace_dest)

    def add_path(base: Path, tail: Path):
        return base / tail

    remove_base = partial(remove, str(template_base) + '/')
    remove_j2 = partial(remove, '.j2')
    replace_name = partial(replace, MARKER_PROJECT_NAME, str(dest_dir.name))

    add_dest_dir = partial(add_path, dest_dir)

    return compose(
        remove_base,
        remove_j2,
        replace_name,
        Path,
        add_dest_dir
    )(str(template_path))
