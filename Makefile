PYTHON=python3
NUITKA=$(PYTHON) -m nuitka

build:
	$(PYTHON) -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt nuitka
	. venv/bin/activate && $(NUITKA) --onefile __main__.py --output-filename=vibeterm

clean:
	rm -rf venv build dist *.onefile-build *.build *.dist
