install:
	poetry install

test:
	poetry run py.test --cov=anki_swiss_knife --cov-report xml --testdox tests/
