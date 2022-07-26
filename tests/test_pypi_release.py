import github
import os
import re
import pytest
import requests
import subprocess
import time
from packaging import version


@pytest.mark.pypi
@pytest.mark.timeout(1800)
def test_pypi_deploy():
    # Find out the current version of the PyPI package
    def upstream_version(url):
        response = requests.get(url)
        if response.status_code == 200:
            return version.parse(response.json()['info']['version'])
        else:
            return version.parse('0.0.0')

    # Construct a version, by finding the maximum version across Github, PyPI and TestPyPI and increasing that
    gh = github.Github(os.getenv("GH_API_ACCESS_TOKEN"))
    repo = gh.get_repo('dokempf/test-gha-python-package')
    current_version = max([
        upstream_version('https://pypi.org/pypi/testghapythonpackage/json'),
        version.parse(repo.get_latest_release().title[1:])
    ])
    next_version = version.Version('{}.{}.{}'.format(current_version.major, current_version.minor, current_version.micro + 1))
    tag = f"v{str(next_version)}"

    # Create the release - this will trigger the PyPI release workflow
    repo.create_git_release(
        tag,
        tag,
        "Test Release",
        target_commitish='main'
    )
    time.sleep(2)

    # Identify the PyPI release workflow
    branch = repo.get_branch('main')
    workflow = repo.get_workflow("pypi.yml").get_runs()[0]
    assert workflow.head_sha == branch.commit.sha

    # Poll the workflow status
    while workflow.status != 'completed':
        # We poll at a relatively large interval to avoid running against the Github API
        # limitations in times of heavy development activities on the cookiecutter.
        time.sleep(30)
        workflow = repo.get_workflow("pypi.yml").get_runs()[0]

    assert workflow.conclusion == 'success'
