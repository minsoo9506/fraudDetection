PYTHON_INTERPRETER = python3

# Install python dependency
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements/requirements.txt

# Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

#  Lint using
## flake8: PEP8 based lint
## mypy  : type check
lint:
	pytest model --flake8 --mypy

#  formatting
## black: formatting
## isort: import formatting
format:
	black model
	isort model