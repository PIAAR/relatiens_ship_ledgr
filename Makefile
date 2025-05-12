# Makefile for Relationship Ledger backend

# Default environment
# VENV ?= venv
# PYTHON ?= $(VENV)/bin/python
PYTEST ?= pytest

# Directories
TEST_DIR = backend/tests
UNIT_TESTS = $(TEST_DIR)/unit
REGRESSION_TESTS = $(TEST_DIR)/regression

# Commands
.PHONY: help install lint test unit regression clean

help:
	@echo "Makefile commands:"
	@echo "  make install        → Install dependencies"
	@echo "  make lint           → Run black and flake8 linting"
	@echo "  make test           → Run all tests"
	@echo "  make unit           → Run unit tests"
	@echo "  make regression     → Run regression tests"
	@echo "  make clean          → Clean __pycache__ and .pytest_cache"

install:
	pip install -r requirements.txt

lint:
	black . && flake8 .

test:
	$(PYTEST) $(TEST_DIR)

unit:
	$(PYTEST) $(UNIT_TESTS) -v 

regression:
	$(PYTEST) $(REGRESSION_TESTS) -v 

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache
