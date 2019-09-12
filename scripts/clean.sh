#!/bin/bash -xe

poetry run isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=100 --recursive doctype/ tests/
poetry run black doctype tests/ -l 100
