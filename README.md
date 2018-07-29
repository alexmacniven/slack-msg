# slack-msg

slack-msg is a Python wrapper for sending messages to your slack channels.

Use it in your own code:

```python
import slack-msg as slack

slack.send("Clear for takeoff")
```

As well as straight from the console:
```bash
$ slack send "Clear for takeoff"
```

slack-msg also supports multiple channels:

```bash
$ slack send "Clear for takeoff" "status"
$ slack send "Abort mission!" "errors"
```

All stored in a handy config file:

```bash
$ slack config

Configurations
==============

hooks
-----
default : https://hooks.slack.com/...
status : https://hooks.slack.com/...
errors: https://hooks.slack.com/...
```

## Installation

1) Clone the repository
2) Build the source `$ python setup.py build`
3) Install `$ python setup.py install`
