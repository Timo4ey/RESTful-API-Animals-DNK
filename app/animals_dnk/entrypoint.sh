#!/bin/sh
set -e  # Exit immediately if a command fails

make makemigrations
make run-prod