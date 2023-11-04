build:
	pyinstaller gtiff2gjson.py

venv:
	python3 -m venv venv

deps:
	pip install -r requirements.txt

install:
	make
	ln -s $(shell pwd)/dist/gtiff2gjson/gtiff2gjson /bin/gtiff2gjson

clean-build:
	rm -rfd dist build pyinstaller *.spec

clean-cache:
	rm -rfd __pycache__ utils/__pycache__
clean-env:
	rm -rfd venv

clear:
	make clean-build
	make clean-cache
	rm /bin/gtiff2gjson
	


	
	