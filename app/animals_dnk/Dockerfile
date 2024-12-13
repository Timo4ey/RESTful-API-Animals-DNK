FROM python:3.11 AS base

RUN groupadd -r non-root && useradd -r -g non-root non-root
WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install setuptools wheel build \
    && python -m build \
    && pip install dist/*.whl
    
RUN chmod +x /app/entrypoint.sh
RUN chown -R non-root:non-root /app    
USER non-root

CMD ["/app/entrypoint.sh"]