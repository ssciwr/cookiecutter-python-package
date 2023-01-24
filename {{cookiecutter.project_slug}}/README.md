# Welcome to {{ cookiecutter.project_name }}

{# The white-space control of the below template is quite delicate - if you add one, do it exactly like this (mind the -'s) -#}
{% if cookiecutter.license == "MIT" -%}
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
{% endif -%}
{% if cookiecutter.license == "BSD-2" -%}
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
{% endif -%}
{% if cookiecutter.license == "GPL-3.0" -%}
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
{% endif -%}
{% if cookiecutter.license == "LGPL-3.0" -%}
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
{% endif -%}
{% if cookiecutter.remote_url != "None" -%}
{% if cookiecutter.github_actions_ci == "Yes" and cookiecutter|is_github -%}
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter|username }}/{{ cookiecutter|remote_slug }}/ci.yml?branch=main)](https://github.com/{{ cookiecutter|username }}/{{ cookiecutter|remote_slug }}/actions/workflows/ci.yml)
{% endif -%}
{% if cookiecutter.gitlab_ci == "Yes" and cookiecutter|is_gitlab -%}
[![Gitlab pipeline status](https://img.shields.io/gitlab/pipeline/{{ cookiecutter|username }}/{{ cookiecutter|remote_slug }}/main
{%- if "gitlab.com" not in cookiecutter.remote_url -%}
?gitlab_url={{ cookiecutter|gitlab_instance }}
{%- endif -%}
)]({{ cookiecutter|gitlab_instance }}/{{ cookiecutter|username }}/{{ cookiecutter|remote_slug }}/-/pipelines)
{% endif -%}
{% endif -%}
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter|remote_slug }}/badge/)](https://{{ cookiecutter|remote_slug }}.readthedocs.io/)
[![codecov](https://codecov.io/{{ cookiecutter|provider_acronym }}/{{ cookiecutter|username }}/{{ cookiecutter|remote_slug }}/branch/main/graph/badge.svg)](https://codecov.io/{{ cookiecutter|provider_acronym }}/{{ cookiecutter|username }}/{{ cookiecutter|remote_slug }})
{{ "\n" -}}

## Installation

The Python package `{{ cookiecutter|modname }}` can be installed from PyPI:

```
python -m pip install {{ cookiecutter|modname }}
```

## Development installation

If you want to contribute to the development of `{{ cookiecutter|modname }}`, we recommend
the following editable installation from this repository:

```
{%- if cookiecutter.remote_url != "None" %}
git clone {{ cookiecutter.remote_url }}
cd {{ cookiecutter.project_slug }}
{%- endif %}
python -m pip install --editable .[tests]
```

Having done so, the test suite can be run using `pytest`:

```
python -m pytest
```

## Acknowledgments

This repository was set up using the [SSC Cookiecutter for Python Packages](https://github.com/ssciwr/cookiecutter-python-package).
