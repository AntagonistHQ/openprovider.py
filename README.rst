.. image :: https://i.imgur.com/Uje1AsW.png

===============
openprovider.py
===============

.. image:: https://travis-ci.org/AntagonistHQ/openprovider.py.svg?branch=master
    :target: https://travis-ci.org/AntagonistHQ/openprovider.py
    :alt: Build Status
.. image:: https://readthedocs.org/projects/openproviderpy/badge/?version=latest
    :target: https://readthedocs.org/projects/openproviderpy/?badge=latest
    :alt: Documentation Status

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

Now you can run the tests:

.. code:: shell

    python setup.py test

Building the docs
-----------------

Be sure to install sphinx. If you are in a virtualenv, it may be needed to
install sphinx in the virtualenv as well since it tries to import.

.. code:: shell

    make -C docs html
