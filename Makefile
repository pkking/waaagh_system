.PHONY: clean help test test-db run dependencies db

help:
	@echo "  clean      remove unwanted stuff"
	@echo "  dependencies    install dependencies"
	@echo "  test       run the testsuite"
	@echo "  run        run the development server with the development config"
	@echo "  db         init devel database"
	@echo "  test-db	init test database"


dependencies:requirements.txt
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

db:migrations
	TYPE=DEVEL FLASK_APP=start_blog.py flask db upgrade

test-db:migrations
	TYPE=TESTING FLASK_APP=start_blog.py flask db upgrade

test:
	pytest -v

run:
	TYPE=DEVEL FLASK_APP=start_blog.py flask run 