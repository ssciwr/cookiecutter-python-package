from setuptools import setup

setup(
    name='{{ cookiecutter.project_slug.replace("-", "") }}',
    version='0.0.1',
    author='{{ cookiecutter.full_name }}',
    author_email='your@email.com',
    description='Add description here',
    long_description='',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
{%- if cookiecutter.license == "MIT" %}
        "License :: OSI Approved :: MIT License",
{%- elif cookiecutter.license == "BSD-2" %}
        "License :: OSI Approved :: BSD License",
{%- elif cookiecutter.license == "GPL-3.0" %}
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
{%- elif cookiecutter.license == "LGPL-3.0" %}
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
{%- endif %}
    ],
)
