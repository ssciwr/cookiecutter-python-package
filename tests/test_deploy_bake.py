import github
import gitlab
import os
import pytest
import requests
import subprocess
import time

from . import inside_bake, wait_five_seconds


@pytest.mark.deploy
def test_push_remote(cookies):
    # We configure one project that has all implemented integrations enabled.
    bake = cookies.bake(
        extra_context={
            'project_name': 'My Python Project',
            'remote_url': 'git@github.com:dokempf/test-gha-python-package.git',
        }
    )
    with inside_bake(bake):
        # Push to Github
        subprocess.check_call("git push -f origin main".split())
        # Push to Gitlab
        subprocess.check_call("git remote add gitlab git@gitlab.com:dokempf/test-gl-python-package.git".split())
        subprocess.check_call("git push -f gitlab main".split())


@pytest.mark.integrations
@pytest.mark.flaky(max_runs=3, min_passes=1, rerun_filter=wait_five_seconds)
@pytest.mark.timeout(300)
def test_github_actions_ci_on_deployed_bake():
    # Authenticate with the Github API
    gh = github.Github(os.getenv("GH_API_ACCESS_TOKEN"))

    # Identify the correct workflow
    repo = gh.get_repo('dokempf/test-gha-python-package')
    branch = repo.get_branch('main')
    workflow = repo.get_workflow("ci.yml").get_runs()[0]
    assert workflow.head_sha == branch.commit.sha

    def check_workflow(name):
        # Poll the workflow status
        workflow = repo.get_workflow(name).get_runs()[0]
        while workflow.status != 'completed':
            # We poll at a relatively large interval to avoid running against the Github API
            # limitations in times of heavy development activities on the cookiecutter.
            time.sleep(30)
            workflow = repo.get_workflow(name).get_runs()[0]

        assert workflow.conclusion == 'success'

    check_workflow("ci.yml")


@pytest.mark.integrations
@pytest.mark.flaky(max_runs=3, min_passes=1, rerun_filter=wait_five_seconds)
@pytest.mark.timeout(300)
def test_gitlab_ci_on_deployed_bake():
    # Authenticate with Gitlab API
    gl = gitlab.Gitlab('https://gitlab.com', private_token=os.getenv("GL_API_ACCESS_TOKEN"))
    gl.auth()

    # Find the correct Gitlab pipeline - after giving it 2 seconds to properly initiate
    project = gl.projects.get('dokempf/test-gl-python-package')
    pipeline = project.pipelines.list()[0]
    branch = project.branches.get('main')
    assert pipeline.sha == branch.commit['id']

    # Poll the pipeline status
    while pipeline.status != 'success':
        time.sleep(5)
        pipeline.refresh()
        if pipeline.status in ["failed", "canceled", "skipped"]:
            pytest.fail("The Gitlab API reported Status '{}' while we were waiting for 'success'".format(pipeline.status))


@pytest.mark.integrations
@pytest.mark.flaky(max_runs=3, min_passes=1, rerun_filter=wait_five_seconds)
@pytest.mark.timeout(300)
def test_readthedocs_deploy():
    # Authenticate with the Github API to get the upstream commit
    gh = github.Github(os.getenv("GH_API_ACCESS_TOKEN"))
    repo = gh.get_repo('dokempf/test-gha-python-package')
    sha = repo.get_branch('main').commit.sha

    def rtd_api_request(endpoint):
        response = requests.get(
            'https://readthedocs.org/api/v3/projects/test-gha-python-package/{}'.format(endpoint),
            headers={'Authorization': 'token {}'.format(os.getenv('RTD_API_ACCESS_TOKEN'))}
        )
        return response.json()

    # Check that the build has the correct commit
    last_build_id = rtd_api_request("versions/latest/builds")["results"][0]["id"]
    build = rtd_api_request('builds/{}'.format(last_build_id))

    # Wait until the build has finished
    while build['state']['code'] != 'finished':
        time.sleep(5)
        build = rtd_api_request('builds/{}'.format(last_build_id))

    assert build['success']
    assert build["commit"] == sha
