"""
slack-msg.com.send

Implements the send module
"""
import requests

from .base import Base, load_config, confpath

headers = {
    'Content-type': "application/json"
}
"""dict: Request headers"""


class Send(Base):
    """The Send class

    Inherits from .base.base

    """
    def run(self):
        """A Send instance runtime

        The logic for to run the Send command;

        1) Send the message with the secified hook

        or

        2) Send the message with the first hook in the configuration

        """
        if not self.options["<hook>"]:
            send(self.options["<message>"])
        else:
            send(self.options["<message>"], self.options["<hook>"][0])


def send(msg, *args):
    """Sends 'msg' to Slack

    Sends the supplied str message to a Slack channel. If no Slack hook
    is supplied in args then the default hook is used

    Args:
        msg: A message to send
        hook: (Optional) A hook to use when sending
    """
    # Load the configuration file
    config = load_config(confpath)
    # If any optional args have been supplied; try to link them to a hook
    # in the configuration file. Else just use the default
    if args:
        if args[0] in config["hooks"].keys():
            url = config["hooks"][args][0]
        else:
            raise KeyError("Hook {0} isn't specified".format(args[0]))
    else:
        try:
            url = config["hooks"]["default"]
        except KeyError:
            # If no hooks have been specified then raise
            raise ValueError("No default hook has been specified")

    # Create the payload
    payload = {"text": msg}

    # Send the payload
    requests.post(url, headers=headers, data=str(payload))
