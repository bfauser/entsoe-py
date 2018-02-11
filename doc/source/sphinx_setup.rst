Setting up **Sphinx** documentation tool
========================================

rst Cheat Sheet
===============

Format docstrings according to `rst-file format <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#internal-and-external-links>`_

set up Sphinx
-------------

Goto projcet folder and create a ``doc`` folder:

.. code::

   > mkdir doc
   > cd doc

Inside the doc folder setup **Sphinx** using

.. code::

   > sphinx-quickstart

and answer the questions. This will create some configuration files.
Customise the ``doc\config.py`` file where you can set the theme etc.
For details see the `Sphinx documentation <http://www.sphinx-doc.org/en/stable/>`_.

To build the documentation use the following commands (on Windows in an
anaconda prompt ``make.bat`` is provided if you said 'y' in quickstart)

.. code::

   > sphinx-apidoc -f -o source/ ../
   > make html

Then go to doc/build and open 'index.html' with a browser