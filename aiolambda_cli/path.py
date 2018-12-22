from pathlib import Path
from toolz import curry

from aiolambda.functools import compose

MARKER_PROJECT_NAME = '__PROJECT_NAME__'


@curry
def dest_from_template(template_base: Path, dest_dir: Path, template_path: Path) -> Path:
    @curry
    def remove(remove: str, base: str) -> str:
        return base.replace(remove, '')

    @curry
    def replace(replace_src: str, replace_dest: str, base: str) -> str:
        return base.replace(replace_src, replace_dest)

    @curry
    def add_path(base: Path, tail: Path):
        return base / tail

    return compose(
        remove(str(template_base) + '/'),
        remove('.j2'),
        replace(MARKER_PROJECT_NAME, str(dest_dir.name)),
        Path,
        add_path(dest_dir)
    )(str(template_path))
