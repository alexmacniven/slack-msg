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

All stored in a handy config file;

```bash
$ slack config

Configurations
==============

hooks
-----
default : https://hooks.slack.com/...
```
