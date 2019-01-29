clean:
	rm -r *.egg-info dist

dist:
	pip install --upgrade pip setuptools wheel; \
	python setup.py sdist bdist_wheel; \
	twine upload dist/*

format:
	autopep8 -a -a -r -i --max-line-length 119 bzflag/

validate:
	mypy bzflag/
