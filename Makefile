setup-pre-commit:
	pre-commit install

setup: setup-pre-commit
	pip install -r requirements.txt
