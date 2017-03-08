.PHONY: clean install help test run dependencies docs

help:
	@echo "  clean      remove unwanted stuff"
	@echo "  install    install dependencies"
	@echo "  test       run the testsuite"
	@echo "  run        run the development server with the development config"

dependencies:requirements.txt
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

test:
	TYPE=TESTING FLASK_APP=blog/__init__.py python blog_tests.py


run:
	TYPE=DEVEL FLASK_APP=blog/__init__.py flask run

install:dependencies
	clear
	flaskbb --config ./flaskbb.cfg install