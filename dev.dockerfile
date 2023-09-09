FROM python:3.11-alpine3.18
ENV PYTHONUNBUFFERED=true
WORKDIR /app
COPY Pipfile .
RUN pip install pipenv
RUN pipenv install --deploy

ENTRYPOINT []
CMD pipenv run python manage.py runserver 0.0.0.0:8080
