install:
	pip install poetry && \
	poetry install

start:
	poetry run python minimal-studio-bot/main.py