# api-python

## Installation

```
apt-get install python-dev
pip install traceguide
```

**Important Note:**: The Traceguide secure connection uses [Server Name Identification (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication#No_support).  This requires Python 2.7.9 or greater.


## Getting Started

```python
# Retrieve Runtime singleton
runtime = instrument.get_runtime("my_server", "{{my_access_token}}")

# Send a regular global load along with a data payload
favoriteNumbers = [ 42, 17, 1984 ]
runtime.log('Hello Runtime!', favoriteNumbers)

# Send a span record for a given operation 
span = runtime.span('trivial/sample_span')
span.add_join_id('end_user_id', 'john_smith')
favoriteNumberSet = set(favoriteNumbers)
span.infof('Hello Span!', favoriteNumberSet)
span.end()
```

## License

[The MIT License](LICENSE).

Copyright (c) 2015, Resonance Labs.


