import pytest
import subprocess

from . import check_bake, inside_bake


@pytest.mark.local
def test_basic_config(cookies):
    bake = cookies.bake(extra_context={'project_slug': 'test_project'})
    check_bake(bake)


@pytest.mark.local
def test_with_remote(cookies):
    bake = cookies.bake(extra_context={'remote_url': 'https://github.com/dokempf/test-gha-python-package.git'})
    check_bake(bake)
    assert bake.project_path.name == 'test-gha-python-package'
    with inside_bake(bake):
        assert len(subprocess.check_output("git remote -vv".split())) > 0
