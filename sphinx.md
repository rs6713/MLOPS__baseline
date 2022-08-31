**Sphinx**
==========

Installation
------------

poetry add sphinx --dev
pip install sphinx

restructuredText extension for vscode

sphinx-quickstart
Separate source/build to create clean dirs layout.
Ensure add docs/source/_build dir to .gitignore


Builds
------
Make docstrings

.. code::

    sphinx-apidoc [options] -o <output_path> <module_path> [exclude_pattern, ...]
Make html pags

.. code::

    make html

`Sources`
^^^^^^^^^
https://www.sphinx-doc.org/en/master/usage/installation.html
