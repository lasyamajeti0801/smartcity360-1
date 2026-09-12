.PHONY: help install build test run clean

help:
	@echo "SmartCity360 - Municipal Operations Platform"
	@echo "  make install - Install backend and frontend dependencies"
	@echo "  make build   - Build frontend assets and prepare static bundle"
	@echo "  make test    - Run pytest test suite"
	@echo "  make run     - Run development server"

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install

build:
	cd frontend && npm run build

test:
	pytest backend/tests

run:
	python main.py
