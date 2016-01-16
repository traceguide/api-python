# api-python

* [Installation](#installation)
* [Getting Started](#getting-started)
* [Common Tasks](#common-tasks)

## Installation

```
apt-get install python-dev
pip install lightstep
```

**Important Note:**: The LightStep secure connection uses [Server Name Identification (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication#No_support).  This requires Python 2.7.9 or greater.


## Getting Started

LightStep implements [OpenTracing's](http://opentracing.io/) [Python API](https://github.com/opentracing/api-python)

Please see the [sample programs](sample/) for examples of how to use this library.
In particular:
* [Trivial Example](sample/trivial/main.py) shows how to use the library on a single host.
* [Context in Headers](sample/http/context_in_headers.py) shows how to pass a `TraceContext` through `HTTP` headers.

Or if your python code is already instrumented for OpenTracing, you can simply switch to LightStep's implementation with:

```python
import lightstep.tracer

lightstep.tracer.init_for_opentracing(access_token='{your_access_token}')
...
```

## License

[The MIT License](LICENSE).

Copyright (c) 2015, Resonance Labs.
