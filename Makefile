dist:
	pip install --upgrade pip setuptools wheel; \
	python setup.py sdist bdist_wheel; \
	twine upload dist/*
