install:
	pipenv install --dev

check: check-black check-isort flake8 mypy

format: black isort

black:
	pipenv run black .

check-black:
	pipenv run black --check .

isort:
	pipenv run isort -rc -y hitchhiker

check-isort:
	pipenv run isort -rc --check-only hitchhiker

flake8:
	pipenv run flake8 hitchhiker

mypy:
	pipenv run mypy hitchhiker
