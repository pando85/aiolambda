import pytest
import subprocess
import shutil

from aiolambda_cli.templates import render_all


@pytest.fixture
def input_vars():
    return {
        'project_name': 'test1',
        'database': 'postgres',
        'is_mq': True,
        'is_ci': True
    }


def test_render(input_vars):
    render_all(input_vars)
    subprocess.run('make test', cwd=input_vars["project_name"], shell=True, check=True)
    shutil.rmtree(input_vars['project_name'])
