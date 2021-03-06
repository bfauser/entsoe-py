"""
Unit Tests
==========

We use ``nose2`` to test some of the capabilities of the **entsoe-py**
package. To run the unit tests you need a API key, which you can get
by registering at `Entso-e Transparancy's web page <https://transparency.entsoe.eu/usrm/user/createPublicUser>`_.

Install nose2
.. code::

   > pip install nose2

Go to the base directory of the package and run there
.. code::

   > nose2 tests

Run a single test like this
.. code::

   > nose2 tests.tests.TestCase.test_price_request

where in the mdoule ``tests`` we have test routine with name ``test_price_request``.
"""