"""slack-msg.com.config

Implements the Config class
"""

from .base import Base, save_config, load_config, confpath


class Config(Base):
    """The Config class

    Inherits from .base.Base
    """

    def run(self):
        """A Config instance runtime

        This function implements the logic to execute the 'config
        command';

        1) Creates and loads a new configuration if the '--setup'
        argument is supplied

        2) Performs the 'add_hook' function if the '--add' argument
        is supplied

        3) Performs the 'remove_hook' function if the '--remove'
        argument is supplied

        4) Writes the configuration to the console

        """
        config = load_config(confpath)
        # Either add or remove hooks (not allowing both)
        if self.options["--add"]:
            url = self.options["<url>"]
            hook = self.options["<hook>"][0]
            self.add_hook(config, hook, url)
        elif self.options["--remove"]:
            hook = self.options["<hook>"]
            self.remove_hook(config, hook)
        else:
            # Write the configuration to the console
            print("\nConfigurations\n{0}".format("=" * len("Configurations")))
            for key, val in config.items():
                print("\n{0}\n{1}".format(key, "-" * len(key)))
                for k, v in val.items():
                    print("{0} : {1}".format(k, v))
            print("")

    def add_hook(self, config, hook, url):
        """Adds a hook to configuration"""
        # TODO: Some input validation needed
        config["hooks"][hook] = url
        print("Added hook {0}".format(hook))
        save_config(confpath, config)

    def remove_hook(self, config, hook):
        """Removes a hook from configuration

        Raises:
            KeyError: When the supplied hook name doesn't exist

        """
        try:
            config["hooks"].pop(hook)
            save_config(confpath, config)
            print("hook {0} has been removed".format(hook))
        except KeyError:
            print("hook {0} doesn't exist".format(hook))
