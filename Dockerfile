FROM python:3.9-buster
LABEL org.container.image.authors="grimsleepless@protonmail.com"

ENV POETRY_VERSION=1.1.7

RUN apt update && \
    apt dist-upgrade -y && \
    apt install -y python3-dev curl build-essential python3-pip && \
    pip install poetry==$POETRY_VERSION

WORKDIR /code/
ADD poetry.lock pyproject.toml Makefile /code/
ADD anki_swiss_knife /code/anki_swiss_knife/

RUN cd /code && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

ENTRYPOINT ["poetry", "run", "python", "anki_swiss_knife/main.py"]