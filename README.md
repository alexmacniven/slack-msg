# Another Slack API Wrapper (asaw)

Use Another Slack API Wrapper for sending messages to your slack channels.

It's written in Python.

Use it in your own code:

```python
import asaw

asaw.send("Clear for takeoff")
```

As well as straight from the console:
```bash
$ asaw send "Clear for takeoff"
```

asaw supports multiple channels:

```bash
$ asaw send "Clear for takeoff" "status"
$ asaw send "Abort mission!" "errors"
```

All stored in a handy config file:

```bash
[hooks]
default = "https://hooks.slack.com/..."
status = "https://hooks.slack.com/..."
errors =  "https://hooks.slack.com/..."
```

## Installation

### pip(env)

`$ pip(env) install asaw`

## Setup

Setup a config file;

`$ asaw install`

You'll be prompted to supply a default hook

Additional hooks can be supplied via;

`$ asaw config --add [hook_name] [hook_url]` 
