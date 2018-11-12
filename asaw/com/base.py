import os

import toml


here = os.path.dirname(os.path.abspath(__file__))
"""str: Current location"""

appdata = os.path.join(os.environ["APPDATA"], "slackli")
"""str: Path to AppData"""

confpath = os.path.join(appdata, "config.toml")
"""str: Path to `config.json`"""


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
    with open(path) as f:
        return toml.load(f)


def save_config(path, config):
    """Saves the configuration

    Infact it dumps the supplied configuration at the location
    referenced by 'jpath'

    *Note: Any data at the location 'jpath' is overwritten*

    Args:
        config: A configuration

    """
    with open(path, "w") as f:
        toml.dump(config, f)
