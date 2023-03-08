install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
test:
	python -m pytest -v test_app.py
all: install test