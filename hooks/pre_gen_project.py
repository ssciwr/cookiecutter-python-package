# This script executes before the project is generated from your cookiecutter.
# Details about hooks can be found in the cookiecutter documentation:
# https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html
#
# An example of a pre-hook would be to validate the provided input for a
# user configuration value and exit with an error upon failure.

import sys
from importlib.metadata import version


# Cookiecutter 2.7 coerces command-line and configuration overrides to booleans.
# This check intentionally duplicates the one in pre_prompt.py: Cookiecutter
# versions older than 2.4 do not support pre-prompt hooks, so this remains as a
# fallback for them after prompting.
parts = tuple(int(part) for part in version("cookiecutter").split(".")[:3])
if parts < (2, 7, 0):
    sys.stderr.write("This template requires cookiecutter >= 2.7\n")
    sys.exit(1)


# Call fail_if with a Jinja template-based condition to abandon the
# cookiecutter generation process with an error.
def fail_if(condition, message):
    if condition:
        sys.stderr.write(message + "\n")
        sys.exit(1)
