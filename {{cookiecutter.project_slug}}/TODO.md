This TODO list is automatically generated from the cookiecutter-python-project template.
The following tasks need to be done to get a fully working project:

{% if cookiecutter.remote_url == 'None' -%}
* Set up a remote repository. You can e.g. create a project in GitHub or GitLab and run
  the following commands in your locally generated project folder: `git remote add origin <Remote-URL>`
  For a seamless integration, the name of the project should also be `{{ cookiecutter.project_slug }}`.
{%- else -%}
* Push to your remote repository for the first time by doing `git push origin main`.
{%- endif %}
* Head to your user settings at `https://pypi.org` and setup PyPI trusted publishing.
  In order to do so, you have to head to the "Publishing" tab, scroll to the bottom
  and add a "new pending publisher". The relevant information is:
  * PyPI project name: `{{ cookiecutter|modname }}`
  * Owner: `{{ cookiecutter|username }}`
  * Repository name: `{{ cookiecutter.project_slug }}`
  * Workflow name: `pypi.yml`
  * Environment name: not required
* Enable the integration of Readthedocs with your Git hoster. In the case of Github, this means
  that you need to login at [Read the Docs](https://readthedocs.org) and click the button
  *Import a Project*.
{%- if cookiecutter.github_actions_ci == 'Yes' %}
* Enable the integration with `codecov.io` by heading to the [Codecov.io Website](https://codecov.io),
  log in (e.g. with your Github credentials) and enable integration for your repository. In order to do
  so, you need to select it from the list of repositories (potentially re-syncing with GitHub). Then, head
  to the "Settings" Tab and select "Global Upload Token". Here, you should select the "not required" option.
{%- endif %}
