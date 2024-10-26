install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check mylib/*.py *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

all: install lint test format 

setup_package:
	#pip install --user -e .
	python setup.py develop 

etl:
	etl extract
	etl transform_load

query:
	etl query "SELECT Indicator, MAX(Value) Max_Value_Across_States FROM default.rr368_mentalhealth GROUP BY Indicator"