#!/bin/bash
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

if [[ "${info[0]}" == "strict" && $(echo ruff check) == "All checks passed!" ]]
then
  echo passed linting
fi

if [[ "${info[1]}" == "production" ]]
then
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
else
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
fi