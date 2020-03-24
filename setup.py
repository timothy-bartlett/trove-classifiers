from io import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='trove-classifiers',
    version='1.0.0',
    description="Cannonical source for classifiers on PyPI (pypi.org).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/packaging-classifiers",
    author="The PyPI Admins",
    author_email="admin@pypi.org",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python :: 3',
    ],
    keywords="classifiers",
    packages=find_packages(),
)
