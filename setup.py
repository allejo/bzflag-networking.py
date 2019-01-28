import setuptools

setuptools.setup(
    name='bzflag-networking',
    version='1.0.0',
    author='Vladimir "allejo" Jimenez',
    author_email='me@allejo.io',
    description='A Python library for reading and unpacking BZFlag network packets',
    url='https://github.com/allejo/bzflag-networking.py',
    packages=setuptools.find_packages(),
    classifiers={
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    },
)
