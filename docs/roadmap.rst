Roadmap
=======

- Add more examples:
    - **crud_users**: postgres. Postgres calls.
        \*Document project: [**page:database:postgres**]
    - **user_settings**: mq. Send and subscribe AMQP messages.
        \*Document project: [**page:amqp**]
    - `jwt`: ci integration. Basic CI integration with travis.
        \*Document project: [**page:ci:travisci**]
    - `jwt`: container integration. Basic container integration.
        \*Document project: [**page:containers:docker:**]
    - `jwt`: functional implementations. Async compose, types: errors, `ROP`_ documentation.
        \*Document project: [**page:functional**]

- Change command definitions:
    - **inputs**:
        Command defined with env vars, not cli commands (only use cli commands for short
        commands [big execution number of times]).
    - **updates**:
        Makes with inline, replace based ansible filters.
        (same things: number_of_postgres versions, etc... with default values)
    - **.env**:
        Recomend .env for auto updates and load envars in each directory (`projects`).

- Contributions:
    - databases:
        - **redis**...
        - **mongo**...
    - containers:
        - **firecracker**...
    - code analysis:
        - **code climate**
    - automated api tests:
        - **dredd**
    - aiolambda functional

.. _rop: https://fsharpforfunandprofit.com/rop/
