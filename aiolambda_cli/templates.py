import jinja2

from functools import partial
from pathlib import Path
from typing import List

from aiolambda_cli.file import save_to_file
from aiolambda_cli.path import dest_from_template

TEMPLATE_BASE_PATH = Path(__file__).parent / Path('templates')


def render_from_file(path: Path, vars_dict: dict) -> str:
    env = jinja2.Environment(
        autoescape=False,
        trim_blocks=False,
        loader=jinja2.FileSystemLoader(str(path.parent)),
    )

    template = env.get_template(str(path.name))
    return template.render(**vars_dict)


def render_all(vars_dict: dict) -> List[str]:
    template_base_path = Path(TEMPLATE_BASE_PATH)
    dest_dir = Path(vars_dict['project_name'])
    dest_from_path = partial(dest_from_template, template_base_path, dest_dir)

    all_tree = list(template_base_path.glob('**/*'))
    all_directories = filter(lambda x: x.is_dir(), all_tree)
    directories = [
        dest_from_path(directory_path)
        for directory_path in all_directories]

    dest_dir.mkdir()
    list(map(lambda x: x.mkdir(), directories))  # type: ignore

    def filter_templates(template_path: Path) -> bool:
        if template_path.is_file():
            if not vars_dict['is_ci'] and 'travis' in str(template_path):
                return False
            if not vars_dict['is_mq'] and 'mq' in str(template_path):
                return False
            return True
        return False
    all_templates = filter(filter_templates, all_tree)

    def generate_template(template_path: Path) -> str:
        return save_to_file(
            render_from_file(template_path, vars_dict),
            dest_from_path(template_path))

    templates = [generate_template(template_path) for template_path in all_templates]
    return templates
