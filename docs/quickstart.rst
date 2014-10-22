Quick start
===========

.. code:: python

        import openprovider

        op = openprovider.OpenProvider(username="test", password="test")
        print(op.domain.check("this-is-a-test-214123214.info"))
