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

Use `aiolambda-cli` to initialize project dir:

.. code-block:: shell

    $ aiolambda-cli init jwt


API specs:
------------------------

Define microservice `OpenAPI specs`_, for `example`_:

.. literalinclude:: ../examples/jwt/docs/api/v1/openapi.yaml
    :language: yaml
    :start-after: paths
    :end-before: /secret

Code
----

Define your custom handlers referenced in `openAPI specs`. For example, `auth_handler`:

.. literalinclude:: ../examples/jwt/jwt/handlers.py
    :start-after: from jwt.utils import get_secret
    :end-before: async def secret_handler(*_null, **request) -> Response:




Useful commands:
----------------

- `make lint`
- `make run`
- `make test`

See example `jwt` README.md_:

.. _openapi specs: https://github.com/OAI/OpenAPI-Specification
.. _example: ../examples/jwt/docs/api/v1/openapi.yaml
.. _README.md : https://github.com/pando85/aiolambda/blob/master/examples/jwt/README.md
