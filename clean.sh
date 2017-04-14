#!/bin/bash

readonly __DIR__="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ -d "${__DIR__}"/coverage ]; then
  echo "Deleting coverage directory"
  rm -r "${__DIR__}"/coverage
fi
if [ -d "${__DIR__}"/__pycache__ ]; then
  echo "Deleting __pycache__ directory"
  rm -r "${__DIR__}"/__pycache__
fi
if [ -d "${__DIR__}"/tests/__pycache__ ]; then
  echo "Deleting tests/__pycache__ directory"
  rm -r "${__DIR__}"/tests/__pycache__
fi
if [ -e "${__DIR__}"/.coverage ]; then
  echo "Deleting .coverage file"
  rm "${__DIR__}"/.coverage
fi
if [ -e "${__DIR__}"/PunchCard.pyc ]; then
  echo "Deleting PunchCard.pyc file"
  rm "${__DIR__}"/PunchCard.pyc
fi

echo "Finish clean"
