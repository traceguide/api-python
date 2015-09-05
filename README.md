# api-python

## Installation

TBD.

## Getting Started

```
from traceguide import instrument

# Retrieve Runtime singleton - Option 1
runtime = get_runtime(YOUR_GROUP_NAME, YOUR_ACCESS_TOKEN)

# Create Runtime instance - Option 2
runtime = instrument.Runtime(YOUR_GROUP_NAME, YOUR_ACCESS_TOKEN)

# Send a log to the Traceguide server
runtime.log('Log Statement', YOUR_LOG_PAYLOAD)

# Send a span with JoinId to the Traceguide server
span = runtime.start_span('python_server/test_app')
span.add_join_id('end_user_id', 'john_smith')
runtime.finish_span(span)
```

## License

[The MIT License](https://opensource.org/licenses/MIT).

Copyright (c) 2015, Resonance Labs.


