"""
slack

Usage:
  slack config [--setup] [(--add <hook> <url>)] [(--remove <hook>)]
  slack send (<message> [<hook>])
  slack -h | --help
  slack --version

Options:
  -h --help                    Show this screen
  --version                    Show version

Examples:
  slack config                 Displays the current config
  slack --add <hook> <url>     Adds a hook named <hook> with <url>
  slack --remove <hook>        Removes the hook named <hook>
  slack send <message>         Sends a message to 'default'
  slack send <message> <hook>  Sends a message using the hook <hook>

Help:
  For help using this tool, please open an issue on the repository:
  https://github.com/alexmacniven/slack-msg/issues
"""

import inspect
from docopt import docopt
from .__version__ import __version__


def main():
    """Entry to the CLI"""
    # Import the commands and let docopt parse the options and args
    # from the CLI.
    import slack.com as com
    options = docopt(__doc__, version=__version__)
    # Each option has passed has the name of the option as 'key' and
    # whether it was passed (true/false) as 'val'.
    # Eg: {'routes': true}
    for (key, val) in options.items():
        # If the commands package has a module named 'key' and its
        # 'val' is true (it's been passed)...
        if hasattr(com, key) and val:
            # Look for the corresponding class in the module and invoke
            # its constructor.
            module = getattr(com, key)
            com = inspect.getmembers(module, inspect.isclass)
            command = [c[1] for c in com if c[0] == key.capitalize()][0]
            command = command(options)
            # Invoke the command objects run function to do the 'work'.
            command.run()
