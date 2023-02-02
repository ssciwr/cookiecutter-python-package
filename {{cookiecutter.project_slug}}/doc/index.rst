{{ cookiecutter.project_name}}
{% for c in "{{ cookiecutter.project_name}}" %}={% endfor %}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   intro
{%- if cookiecutter.notebooks == "Yes" %}
   demo
{%- endif %}
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`