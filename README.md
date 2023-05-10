# flask-pypprof

Blueprint for pprof profiling endpoints a la GO that can be added to python Flask applications. *flask-pypprof* is a wrapper of [pypprof] and based on [django-pypprof] ideas.

## Installation

```bash
pip install flask-pypprof --extra-index-url https://<>/
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

## Known issues
* `zprofile issue with python 3.11`:  https://github.com/timpalpant/zprofile/pull/2 


## License

[pypprof]: https://github.com/timpalpant/pypprof
[django-pypprof]:https://gitlab.com/prologin/tech/packages/django-pypprof
