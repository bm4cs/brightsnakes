# brights snakes

A place for my python experiments for becoming a better python programmer.

## Setup

```bash
./development/install-tools.sh
```

## Packaging

Uses poetry coupled with the [poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning) plugin.

```
poetry build
poetry publish --repository private
```

## Topics

Topics I plan to cover in due course:

- Packaging and setuptools
- Containers
- Wheels and binary distributions
- Productivity tips
- Source tree layout
- Unit testing and mocks
- Virtual environments
- Design patterns
- Multiple inheritance
- Mixins
- Logging
- Nifty parts of the standard library
- CLI's
- GraphQL servers

## Development environment

- Python 3.10+
- PIP `python3 -m ensurepip --upgrade`
- Poetry
