#!/bin/bash

readonly __DIR__="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

echo "Start clean"
echo ""
# Check for and delete coverage artifacts
echo "Checking for and deleting coverage artifacts."
if [ -d "${__DIR__}"/coverage ]; then
  echo "Found coverage directory"
  rm -r "${__DIR__}"/coverage
  echo "Deleted coverage directory"
fi
if [ -e "${__DIR__}"/.coverage ]; then
  echo "Found .coverage file"
  rm "${__DIR__}"/.coverage
  echo "Deleted .coverage file"
fi
echo ""
# Recursively check for and delete pycache dirctories
echo "Checking for and deleting __pycache__/ artifacts."
(cd -P -- "${__DIR__}" && \
find . -name "__pycache__" -type d \
-exec sh -c '
  for dir do
    echo "Found $dir"
    rm -r $dir
    echo "Deleted $dir"
  done' sh {} +)
echo ""
# Recursively check for and delete pyc files
echo "Checking for and deleting *.pyc artifacts."
(cd -P -- "${__DIR__}" && \
find . -name "*.pyc" -type f \
-exec sh -c '
  for file do
    echo "Found $file"
    rm $file
    echo "Deleted $file"
  done' sh {} +)
echo ""
echo "Finish clean"
