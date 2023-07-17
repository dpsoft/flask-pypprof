# flask-pypprof

Blueprint for pprof profiling endpoints a la GO's that can be added to python Flask applications. *flask-pypprof* is a wrapper of [pypprof] and based on [django-pypprof] ideas.

## Installation

```bash
pip install flask-pypprof
```

## Usage

To add the pprof endpoints to your application, simply register the blueprint:

```python
from flask_pypprof import get_pprof_blueprint

app.register_blueprint(get_pprof_blueprint())
```

Once registered, you will be able to access the following endpoints:

* `/debug/pprof/profile`: will return a CPU profile
* `/debug/pprof/heap`: will return a heap profile
* `/debug/pprof/thread`: will return a thread profile
* `/debug/pprof/wall`: will return a wall time profile(work in progress)

## Configuration

You can configure the memory sample rate by setting the following environment variable:

* `MEMORY_SAMPLE_RATE`: sets the memory profiling sample rate (default: 128 * 1024)

```bash
export MEMORY_SAMPLE_RATE = 128 * 1024
```

## Fetching profiles from your application
Fetch a 30 seconds CPU profile:

```bash
go tool pprof -http=:8088 http://localhost:8081/debug/pprof/profile?seconds=30
```


Fetch a heap profile:

```bash
go tool pprof -http=:8088 http://localhost:8081/debug/pprof/heap
```

## Compatibility 
Python 3.8, 3.9, 3.10 and Flask >= 2.0.0
    
## Known issues
* `zprofile issue with python 3.11`:  https://github.com/timpalpant/zprofile/pull/2 


## License
This code base is available under the Apache License, version 2.

[pypprof]: https://github.com/timpalpant/pypprof
[django-pypprof]:https://gitlab.com/prologin/tech/packages/django-pypprof
