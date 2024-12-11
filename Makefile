run:
	python app/animals_dnk/manage.py runserver

install-build:
	pip install build && python -m build

install-egg:
	python -m build

install:
	pip install dist/*.whl
