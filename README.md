# Welcome to Python Package Cookiecutter!

This repository is a **template (cookiecutter)** for quickly setting up new Python packages.
It’s designed with **scientific applications** in mind and follows the best-practice guidelines of the [Scientific Software Center, Heidelberg University](https://ssc.iwr.uni-heidelberg.de).

---

## Features

* **Simple and configurable setup** for a fully functional Python project
* **Modern build system** with `pyproject.toml` (PEP 517 + PEP 621)
* **Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter)** — trusted by 17k+ developers
* **Automatic versioning** using `setuptools_scm` integrated with Git
* **CI/CD support** via GitHub Actions or GitLab CI
* **Sphinx documentation** with automatic deployment to [Read the Docs](https://readthedocs.org)

> If your Python package includes compiled C++ modules, check out our
> [C++ Cookiecutter with Pybind11 bindings](https://github.com/ssciwr/cookiecutter-cpp-project).

---

## Prerequisites

To use Python Package Cookiecutter, make sure you have the following installed:

* Python **≥ 3.8**
* [Cookiecutter](https://github.com/cookiecutter/cookiecutter) — install with:

  ```bash
  pip install cookiecutter
  ```
* Git **≥ 1.8.2**

---

## Getting Started

Run the Cookiecutter command-line tool:

```bash
cookiecutter gh:ssciwr/cookiecutter-python-package
```

This launches an **interactive prompt** that helps you configure and generate your new project.

One of the prompts will ask for a remote repository URL.
Before you begin, create an empty repository on your preferred Git hosting service, e.g. [GitHub](https://github.com/new).

---

## Configuration Options

You’ll be asked to provide the following configuration values:

| Option                 | Description                                                   | Default                     |
| ---------------------- | ------------------------------------------------------------- | --------------------------- |
| `project_name`         | Human-readable name of your project                           | `My Project`                |
| `remote_url`           | Remote Git repository URL (used for integrations)             | `None` (recommended to set) |
| `project_slug`         | Directory name for the project                                | Auto-detected               |
| `full_name`            | Author name                                                   | `Your Name`                 |
| `license`              | License type (`MIT`, `BSD-2`, `GPL-3.0`, `LGPL-3.0`, or none) | `MIT`                       |
| `github_actions_ci`    | Add CI/CD workflows for GitHub Actions                        | `yes/no`                    |
| `gitlab_ci`            | Add CI/CD workflows for GitLab                                | `yes/no`                    |
| `notebooks`            | Include Jupyter notebooks for docs and testing                | `yes/no`                    |
| `commandlineinterface` | Add a CLI using `click`                                       | `yes/no`                    |

> Tip: If you use `cookiecutter-python-package` often, you can define your default answers in a `.cookiecutterrc` file in your home directory.
> Learn more in the [Cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html).

---

## Issues & Feedback

Found a bug or have a suggestion?
Please open an issue on the [GitHub issue tracker](https://github.com/ssciwr/cookiecutter-python-package).
