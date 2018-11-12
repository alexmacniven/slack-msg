import os
import sys

from json import dump
from setuptools import find_packages, setup, Command


here = os.path.abspath(os.path.dirname(__file__))
"""str: Path to current directory"""

# Import the README and use it as the long-description
with open(os.path.join(here, "README.md")) as f:
    long_description = "\n" + f.read()

# Load the package's __version__.py module as a dictionary
about = {}
with open(os.path.join(here, "slackli", "__version__.py")) as f:
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
        import toml
        # Create the AppData directory for "slack-msg"
        appdata = os.environ["AppData"]
        datapath = os.path.join(appdata, "slackli")
        if not os.path.isdir(datapath):
            os.makedirs(datapath)

        # Create an empty config file if one doesn't exist
        config = os.path.join(datapath, "config.toml")
        if not os.path.isfile(config):
            print("No config file found")
            t = toml.loads("[hooks]")
            with open(config, "w") as f:
                toml.dump(t, f)
            print("Created {0}".format(os.path.join(datapath, "config.toml")))
            print("Don't forget to add your hooks with ", end="")
            print("'$ slack config --add <hook> <url>'")
        else:
            print("A previous config.toml file has been found")


# Where the magic happens:
setup(
    name="asaw",
    version=about['__version__'],
    description="Use Another Slack API Wrapper for sending messages to your slack channels",
    long_description=long_description,
    author="Alex Macniven",
    author_email="apmacniven@outlook.com",
    url="https://github.com/alexmacniven/asaw",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        "requests", "docopt", "toml"
    ],
    include_package_data=True,
    license="MIT",
    entry_points={
        "console_scripts": ["asaw=asaw.cli:main"],
    },
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: ISC License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Microsoft :: Windows"
    ]
)
