{{ cookiecutter.project_name }}
{{ "=" * cookiecutter.project_name|length }}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   intro
{%- if cookiecutter.notebooks == "Yes" %}
   ../notebooks/demo.ipynb
{%- endif %}
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
