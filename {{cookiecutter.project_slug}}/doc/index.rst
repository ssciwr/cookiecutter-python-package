{{ cookiecutter.project_name}}
{% for c in "{{ cookiecutter.project_name}}" %}={% endfor %}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

This is an example function:

.. automodule:: {{ cookiecutter|modname }}
    :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`