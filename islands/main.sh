#! /bin/bash

if [[ $# -eq 0 ]]; then
  echo 'This is an island counter. You should specify a path with a -p argument, such as "main.sh -p <yourpath>".'
  exit 0
fi

python3 main.py $1
