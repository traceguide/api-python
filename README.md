# api-python

* [Installation](#installation)
* [Getting Started](#getting-started)
* [Common Tasks](#common-tasks)

## Installation

```
apt-get install python-dev
pip install traceguide
```

**Important Note:**: The Traceguide secure connection uses [Server Name Identification (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication#No_support).  This requires Python 2.7.9 or greater.


## Getting Started

```python
from traceguide import instrument

# Retrieve Runtime singleton
runtime = instrument.get_runtime("python/my_server", "{your_access_token}")


# Send a span record for a given operation
span = runtime.span('trivial/sample_span')
span.add_join_id('end_user_id', 'john_smith')

# Log a formatted message along with an attached data payload
favoriteNumbers = [ 42, 17, 1984 ]
span.infof('Hello %s!', 'World', payload=favoriteNumbers)

span.end()
```

## Common Tasks

### Adding payload data to log records

Detailed payload data can (and should!) be attached to individual load statements. The format arguments passed in with the logging call are automatically captured as part of the log payload. The `payload` keyword argument can be used to capture additional payload data that is not used in the format string.

**Example**

```python
eventName='post_shared'
eventCount=510
eventData={'post_title':'Ski Video', 'tags': set(['snow', 'winter'])}

span.infof('Event type %s occurred %d times', eventName, eventCount, payload=eventData)
```

Will log a message of `'Event type post_shared occurred 510 times'` along with a JSON payload of:

```json
{
  "arguments": [ "post_shared", 510 ],
  "payload": {
    "post_title": "Ski Video",
    "tags": [ "winter", "snow" ]
  }
}
```

## License

[The MIT License](LICENSE).

Copyright (c) 2015, Resonance Labs.
