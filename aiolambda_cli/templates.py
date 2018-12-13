from functools import partial
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from aiolambda_cli.file import save_to_file
from aiolambda_cli.path import dest_from_template

TEMPLATE_BASE_PATH = Path(__file__).parent / Path('templates')


def render_from_file(path: Path, vars_dict):
    env = Environment(
        autoescape=False,
        trim_blocks=False,
        loader=FileSystemLoader(str(path.parent)),
    )

    template = env.get_template(str(path.name))
    return template.render(**vars_dict)


def render_all(vars_dict):
    template_base_path = Path(TEMPLATE_BASE_PATH)
    dest_dir = Path(vars_dict['project_name'])
    dest_from_path = partial(dest_from_template, template_base_path, dest_dir)

    all_tree = list(template_base_path.glob('**/*'))
    all_directories = filter(lambda x: x.is_dir(), all_tree)
    directories = [
        dest_from_path(directory_path)
        for directory_path in all_directories]

    dest_dir.mkdir()
    [directory.mkdir() for directory in directories]

    def generate_template(template_path):
        return save_to_file(
            render_from_file(template_path, vars_dict),
            dest_from_path(template_path))

    all_templates = filter(lambda x: x.is_file(), all_tree)
    templates = [generate_template(template_path) for template_path in all_templates]
    return templates
