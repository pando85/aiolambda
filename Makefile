.PHONY: help requirements requirements_test lint test run destroy_db init_db destroy_mq init_mq build

APP := aiolambda
WORKON_HOME ?= .venv
VENV_BASE := $(WORKON_HOME)/$(APP)
VENV_ACTIVATE := $(VENV_BASE)/bin/activate
PYTHON := ${VENV_BASE}/bin/python3

.DEFAULT: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/\n\t/'

venv:	## create virtualenv
	@if [ ! -d "$(VENV_BASE)" ]; then \
		virtualenv -p python3 $(VENV_BASE); \
	fi

requirements:	## install requirements
requirements: venv
	@echo Install requirements
	@${PYTHON} -m pip install -r requirements.txt > /dev/null

requirements_test:	## install test requirements
requirements_test: requirements
	@echo Install test requirements
	@${PYTHON} -m pip install -r requirements_test.txt > /dev/null

lint:	## run pycodestyle
lint: requirements_test
	@echo Running linter
	@${PYTHON} -m pycodestyle .
	@${PYTHON} -m flake8 ${APP} ${APP}_cli test bin/aiolambda-cli
	@${PYTHON} -m mypy --ignore-missing-imports ${APP} ${APP}_cli test bin/aiolambda-cli

test:	## run tests and show report
test: lint init_db init_mq install
	@echo Running tests
	@LOG_LEVEL=DEBUG ${PYTHON} -m coverage run -m pytest test
	@${PYTHON} -m coverage report -m

run:	## run project
run: requirements init_db init_mq
	@${PYTHON} -m ${APP}

destroy_db:	## destroy docker database
	@echo Destroy postgres
	@docker rm -f postgres > /dev/null || echo Not postgres running

init_db:	## create docker database
init_db: destroy_db
	@echo Starting postgres
	@docker run -d --name postgres -e POSTGRES_DB=test -e POSTGRES_USER=test \
	-e POSTGRES_PASSWORD=test1234 -p 5432:5432 postgres > /dev/null
	@while ! docker exec postgres psql --host=localhost --username=test -c 'SELECT 1' >/dev/null 2>&1; do \
	 	echo 'Waiting for postgres...'; \
	 	sleep 1; \
	done;

destroy_mq:    ## destroy docker mq
	@echo Destroy rabbit
	@docker rm -f rabbit > /dev/null || echo Not postgres running

init_mq:       ## create docker mq
init_mq: destroy_mq
	@echo Starting rabbit
	@docker run -d --hostname localhost --name rabbit -e RABBITMQ_DEFAULT_USER=test \
		-e RABBITMQ_DEFAULT_PASS=test1234 -p 5672:5672 rabbitmq:3 > /dev/null
	@sleep 2 # sometimes rabbitmq crash: cannot read secret cookie
	@while ! docker exec rabbit rabbitmqctl status >/dev/null 2>&1; do \
		echo 'Waiting for rabbit...'; \
		sleep 1; \
	done;

clean:	## clean all artefacts
	@echo Cleaning all
	@rm -rf build dist

build:	## build package
build: clean requirements_test
	@echo Build package
	@${PYTHON} setup.py bdist_wheel > /dev/null

install:	## install packages
install: venv build
	@echo Remove old package
	@pip uninstall -y aiolambda
	@echo Install packages
	@${PYTHON} setup.py install > /dev/null
	@sudo /usr/bin/pip3 install setuptools && sudo /usr/bin/python3 setup.py install > /dev/null

template:	## aiolambda-cli execution, user ARGS var to parse ARGS. `make template ARGS="--db init test_template"`
template: install
	@./bin/aiolambda-cli ${ARGS}
