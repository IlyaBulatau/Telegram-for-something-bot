#!/bin/sh

export $(grep -v '^#' .env | xargs)

python3 ptb/main.py