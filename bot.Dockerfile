FROM python:3.10.6-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /code/bot

COPY poetry.lock pyproject.toml /

RUN pip install poetry && poetry config virtualenvs.create false

COPY . .

COPY .env .

COPY bot.entrypoint.sh .

RUN chmod 777 bot.entrypoint.sh

RUN poetry install --no-interaction --no-ansi

ENTRYPOINT [ "./bot.entrypoint.sh" ]