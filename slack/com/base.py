"""
slack-msg.com.base

Implements the Base class
"""

import json
import os


here = os.path.dirname(os.path.abspath(__file__))
"""str: Current location"""

defpath = os.path.join(here, "docs", "default_config.json")
"""str: Path to the default configuration json file"""

# TODO: Auto-detect OS; if on Linux use ~\.slack-msg
appdata = os.path.join(os.environ["APPDATA"], "slack-msg")
"""str: Path to AppData"""

confpath = os.path.join(appdata, "config.json")
"""str: Path to `config.json`"""

# Create 'appdata' if it doesn't exist
if not os.path.isdir(appdata):
    os.makedirs(appdata)


class Base(object):
    """The Base command class

    This provides the parent class for all command classes to inherit
    from
    """
    def __init__(self, options, *args, **kwargs):
        """Creates a new 'Base' object

        Makes a new instances of 'Base' and loads the configuration
        file, if no configuration file is found then the default
        configuration file is loaded.

        Args:
            options: Docopt options supplied by the cli
            args: Additional arguements
            kwargs: Additions keyword arguements

        """
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError


def load_config(path):
    """References a loaded configuration file with self.config"""
    with open(path) as jfile:
        return json.load(jfile)


def save_config(path, config):
    """Saves the configuration

    Infact it dumps the supplied configuration at the location
    referenced by 'jpath'

    *Note: Any data at the location 'jpath' is overwritten*

    Args:
        config: A configuration

    """
    with open(path, "w") as jfile:
        json.dump(config, jfile)
