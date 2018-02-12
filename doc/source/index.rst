.. Entsoe-py documentation master file, created by
   sphinx-quickstart on Sun Feb 11 18:27:00 2018.
   
Welcome to Entsoe-py's documentation!
======================================

This is the documentation for the **Entsoe-py** python API wrapper.
It provides access to the API of the `Entso-e Transparancy <https://transparency.entsoe.eu/>`_ 
web service. To use this API you need to register and get an API key.

For details on the API please check the `API documentation <https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html>`_

.. toctree::
   :maxdepth: 2
   :caption: Contents
   
   entsoe <entsoe>
   modules <modules>
   sphinx_setup <sphinx_setup.rst>



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Source
======
The source can be found at

- `Jan Pecinovsky's <https://github.com/JrtPec>`_ EnergieID.be `original project <https://github.com/EnergieID/entsoe-py>`_
- `BF's fork <https://github.com/bfauser/entsoe-py>`_

Running Tests with ``nose2``
============================

To run all tests, go to the base directory of the package and run
.. code::
   
   > nose2 tests
   
To run a single test you can specify the name of the test case
.. code::
   
   > nose2 tests.tests.TestCase.test_price_request

To see logging informaton from the module you can run
.. code::

   > nose2 tests  --log-capture
   > nose2 tests.tests.TestCase.test_price_request --log-capture

and alike.

.. note::

   Logging is experimental and might behave in unexpected ways.   
   
   
License
=======
Entsoe-py is MIT Licensed - Copyright (c) 2017 EnergieID cvba-so


rst-file Helpers
----------------

Format rst-files: `reStrurctured cheat sheet: <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_
