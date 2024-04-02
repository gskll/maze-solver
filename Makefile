test:
	python -m unittest discover -s tests -b
.PHONY: test

run: venv/bin/activate
	./venv/bin/python3 ./src/main.py
.PHONY: run

venv/bin/activate:
	python3 -m venv venv
	./venv/bin/pip install -e .

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -r venv
.PHONY: clean
