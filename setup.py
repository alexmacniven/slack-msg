"""setup.py

The setup file
"""

import codecs
import os
import sys

from setuptools import find_packages, setup, Command
from shutil import rmtree

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANFEST.in file!
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, "slack-msg", "__version__.py")) as f:
    exec(f.read(), about)


# Where the magic happens:
setup(
    name="slack-msg",
    version=about['__version__'],
    description="A Python wrapper for sending messages to your Slack channels",
    long_description=long_description,
    author="A Macniven",
    author_email="apmacniven@outlook.com",
    url="https://github.com/alexmacniven/slack-msg",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        "requests", "docopt"
    ],
    include_package_data=True,
    license="ISC",
    entry_points={
        "console_scripts": ["slack=slack-msg.cli:main"],
    },
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: ISC License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
