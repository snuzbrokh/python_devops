install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
lint:
	pylint --disable=R,C *.py
test:
	python -m pytest -vv --cov=devops_lib
format:
	black *.py devops_lib/*.py
	
all: install lint test format 