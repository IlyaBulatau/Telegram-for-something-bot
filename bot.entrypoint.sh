#!/bin/sh

export $(grep -v '^#' .env | xargs)

alembic upgrade head

python3 ptb/main.py