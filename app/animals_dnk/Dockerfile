FROM python:3.11 AS base

WORKDIR app

COPY . app

RUN pip install build \ 
    && python -m build \
    && pip install dist/*.whl


CMD ["python", "app/animals_dnk/manage.py", "runserver"]