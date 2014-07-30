===============
openprovider.py
===============

This is an unofficial Python library for the Openprovider API. Use it to buy
domains, order SSL certificates and more from
`Openprovider <http://openprovider.com>`_.

Setting up the testing environment
----------------------------------

The testing environment uses environment variables to run. For example:

.. code:: shell

    export OPENPROVIDER_TEST_USERNAME="test"
    export OPENPROVIDER_TEST_PASSWORD="test"
    export OPENPROVIDER_URL="https://api.cte.openprovider.eu"

When using virtualenvwrapper, you can place this in $VIRTUAL_ENV/bin/postactivate.
