#!/bin/bash

# Install dependencies
if [[ ! -d ".venv" ]]; then
  python3.14 -m venv .venv
fi
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r app/requirements.txt

# Upgrade to latest alembic revision
alembic upgrade head

# Check for arguments
info=("lenient" "development")
for arg in "$@"
do
  if [[ "$arg" == "--strict" || "$arg" == "-s" ]]
  then
    info[0]="strict"
  elif [[ "$arg" == "--prod" || "$arg" == "--production" || "$arg" == "-p" ]]
  then
    info[1]="production"
  fi
done

echo "== Running ${info[1]} mode of the application in ${info[0]} mode =="

# Additional checks for strict mode
if [[ "${info[0]}" == "strict" ]]
then
  if ! ruff check .;
  then
    echo "failed linting"
    exit 1
  fi
  echo "linting passed"
fi

# Run the application
if [[ "${info[1]}" == "production" ]]
then
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
else
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
fi