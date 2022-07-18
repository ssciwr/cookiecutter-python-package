This TODO list is automatically generated from the cookiecutter-python-project template.
The following tasks need to be done to get a fully working project:

{% if cookiecutter.remote_url == 'None' -%}
* Set up a remote repository. You can e.g. create a project in GitHub or GitLab and run
  the following commands in your locally generated project folder: `git remote add origin <Remote-URL>`
  For a seamless integration, the name of the project should also be `{{ cookiecutter.project_slug }}`.
{%- else -%}
* Push to your remote repository for the first time by doing `git push origin main`.
{%- endif %}
* Add the secret variable `PYPI_API_TOKEN` to your GitHub project. This can be done in your
  use settings at `https://pypi.org`. Note that currently, you have to create an unscoped token
  for your first upload and only after that you can create a new token whose scope is restricted
  to the current project.
