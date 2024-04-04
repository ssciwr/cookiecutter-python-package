{%- if cookiecutter.version_management == "setuptools_scm" %}
# The version file is generated automatically by setuptools_scm
from {{ cookiecutter|modname }}._version import version as __version__
{%- else %}
from importlib import metadata

__version__ = metadata.version(__package__)
del metadata
{%- endif %}

def add_one(x: int):
    """An example function that increases a number

    :param x: The input parameter to increase
    :return: The successor of the given number
    """
    return x + 1
