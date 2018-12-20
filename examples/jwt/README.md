# JWT Example

## Lint

Lint: `make lint`

## Dev

Run app: `export LOG_LEVEL=DEBUG;make run `

## Doc

Run app: `make run` and [click](http://localhost:8080/v1/ui/)

## Tests

Run tests: `make test`

### Production

**Warning**: aiohttp is [slower with gnunicorn](https://docs.aiohttp.org/en/stable/deployment.html#start-gunicorn). Basic `python -m my_app` execution is prefered.
