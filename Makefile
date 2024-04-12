test:
	python -m unittest discover -s tests -b
.PHONY: test

run: venv
	./venv/bin/python3 ./src/main.py
.PHONY: run

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	./venv/bin/pip install -e .
	touch venv/bin/activate

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -r venv
.PHONY: clean
