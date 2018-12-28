import itertools
import pytest
import subprocess
import shutil

from aiolambda import __version__
from aiolambda_cli.templates import render_all


def input_vars_list():
    all_posibilites = itertools.product([True, False], repeat=2)
    return [{
        'project_name': 'test1',
        'version': __version__,
        'database': 'postgresql',
        'test': True,
        'is_mq': _vars[0],
        'is_ci': _vars[1]
    } for _vars in all_posibilites]


@pytest.mark.parametrize('input_vars', input_vars_list())
def test_render(input_vars):
    render_all(input_vars)
    subprocess.run('make test', cwd=input_vars["project_name"], shell=True, check=True)
    shutil.rmtree(input_vars['project_name'])
