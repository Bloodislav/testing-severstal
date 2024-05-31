FROM python:3.10

RUN mkdir /roll-app

WORKDIR /roll-app

COPY pyproject.toml .

RUN pip install poetry

RUN poetry install 

COPY . .

RUN chmod a+x /roll-app/scripts/*.sh

CMD ["/roll-app/scripts/run.sh"]
# CMD ["gunicorn", "main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]