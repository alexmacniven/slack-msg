"""setup.py

The setup file
"""

import codecs
import os
import sys

from json import dump
from setuptools import find_packages, setup, Command

here = os.path.abspath(os.path.dirname(__file__))
"""str: Path to current directory"""

# TODO: Auto-detect OS; if on Linux use ~\.slack-msg
appdata = os.environ["AppData"]
"""str: path to application data directory"""

# Import the README and use it as the long-description
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

# Load the package's __version__.py module as a dictionary
about = {}
with open(os.path.join(here, "slack", "__version__.py")) as f:
    exec(f.read(), about)


class InitializeCommand(Command):
    """Initializes the module on the host machine"""

    description = "Initializes the module on the host"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Create the AppData directory for "slack-msg"
        datapath = os.path.join(appdata, "slack-msg")
        if not os.path.isdir(datapath):
            os.makedirs(datapath)

        # Create a new configuration file
        config = {"hooks": {"default": ""}}
        configpath = os.path.join(datapath, "config.json")
        if not os.path.isfile(configpath):
            with open(configpath, 'w') as fi:
                dump(config, fi, indent=2)
            print("A brand new configuration file has been created ✨")
            print("It's empty, so add your hooks with ", end="")
            print("'$ slack config --add <hook> <url>'")


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
        "console_scripts": ["slack=slack.cli:main"],
    },
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: ISC License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    # Support for $ setup.py init
    cmdclass={
        "init": InitializeCommand
    }
)
