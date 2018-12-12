Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================

.. include:: ../README.rst

User's guide
------------

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   readme
   installation
   usage
   modules
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
