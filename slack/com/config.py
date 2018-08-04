"""slack-msg.com.config

Implements the Config class
"""

from .base import Base, new_config, save_config, load_config


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
        # Either add or remove hooks (not allowing both)
        if self.options["--add"]:
            self.add_hook()
        elif self.options["--remove"]:
            self.remove_hook()
        else:
            # Write the configuration to the console
            print("\nConfigurations\n{0}".format("=" * len("Configurations")))
            for key, val in self.config.items():
                print("\n{0}\n{1}".format(key, "-" * len(key)))
                for k, v in val.items():
                    print("{0} : {1}".format(k, v))
            print("")

    def add_hook(self):
        """Adds a hook to configuration"""
        # TODO: Some input validation needed
        hook = self.options["<hook>"][0]
        url = self.options["<url>"][0]
        self.config["hooks"][hook] = url
        print("Added hook {0}".format(hook))
        save_config(self.config)
        self.config = load_config()

    def remove_hook(self):
        """Removes a hook from configuration

        Raises:
            KeyError: When the supplied hook name doesn't exist

        """
        hook = self.options["<hook>"][0]
        try:
            self.config["hooks"].pop(hook)
            save_config(self.config)
            self.config = load_config()
            print("hook {0} has been removed".format(hook))
        except KeyError:
            print("hook {0} doesn't exist".format(hook))
