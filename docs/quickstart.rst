Quickstart
==========

Requirements:
-------------

- **docker**
- **python3**
- **pip3**
- **aiolambda-cli**:
    `pip install -U aiolambda`

Create `project`:
-----------------

.. code-block:: shell

    $ aiolambda-cli init jwt


`OpenAPI specs`_:
------------------------

Define microservice API specs, for example:

.. literalinclude:: ../examples/jwt/docs/api/v1/openapi.yaml
    :language: yaml

Code
----

Define your custom handlers referenced in `openAPI specs`. For example, `auth_handler`:

.. literalinclude:: ../examples/jwt/jwt/handlers.py
    :start-after: from jwt.utils import get_secret
    :end-before: async def secret_handler(*_null, **request) -> Response:




Useful commands:
----------------

See example `jwt` README.md_

.. _openapi specs: https://github.com/OAI/OpenAPI-Specification
.. _README.md : https://github.com/pando85/aiolambda/blob/master/examples/jwt/README.md
