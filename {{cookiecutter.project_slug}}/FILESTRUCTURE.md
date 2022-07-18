This is an explanation of the file structure that the cookiecutter generated for you:

* Python source files:
  * The Python package source files are located in the `{{ cookiecutter.project_slug }}` directory.
  * `tests/test_{{ cookiecutter.project_slug }}.py` contains the unit tests for the package.
  * `tests/conftest.py` contains testing setup and configuration for `pytest`
* Markdown files with meta information on the project. [Markdown](https://www.markdownguide.org/basic-syntax/) is
  a good language for these files, as it is easy to write and rendered into something beautiful by your git repository
  hosting provider.
  * `README.md` is the file that users will typically see first when discovering your project.
  * `COPYING.md` provides a list of copyright holders.
{%- if cookiecutter.license != "None" %}
  * `LICENSE.md` contains the license you selected.
{%- endif %}
  * `TODO.md` contains a list of TODOs after running the cookiecutter. Following the
    instructions in that file will give you a fully functional repository with a lot
    of integration into useful web services activated and running.
  * `FILESTRUCTURE.md` describes the generated files. Feel free to remove this from the
    repository if you do not need it.
* Python build system files
  * `pyproject.toml` is the central place for configuration of your Python package.
    It contains the project metadata, setuptools-specific information and the configuration
    for your toolchain (like e.g. `pytest`).
  * `setup.py` is still required for editable builds, but you should not need to change it.
    In the future, `setuptools` will support editable builds purely from `pyproject.toml`
    configuration.
* Configuration for CI/Code Analysis and documentation services
{%- if have_precommit %}
  * `.pre-commit-config.yaml` contains a configuration for the [pre-commit](https://pre-commit.com/)
    tool. It was added because the `pre-commit` tool was found in your Python environment.
{%- endif %}