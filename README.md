# logger

Built-in logger with added functions

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Examples](#examples)
- [License](#license)

## Features

Adds ``get()``, a factory function that returns a **logger** object
(see [logging](https://docs.python.org/3.8/library/logging.html))
with minimal additions such that the LOG file:
- Contains a header with useful meta-data for debugging and record keeping
- Output is formatted to include necessary information for debugging, and is
  easy to read

## Setup

```bash
git clone https://github.com/hankadler/python-logger logger
cd logger
mkdir .venv
pipenv shell
pipenv install
```

## Examples

```python
import logger

log = logger.get(__name__, __file__)

log.debug('A DEBUG message.')
log.info('An INFO message.')
log.warning('A WARNING message.')
log.error('An ERROR message.')
log.fatal('A FATAL message.')
```

> Regarding ``get()``, the first argument sets the name attribute of the logger
> object. The second, gives the desired name for the LOG file. ``__file__``
> works, because the module recognizes that a log file shouldn't end in ``.py``
> and substitutes that for ``.log``.

## License

[MIT](LICENSE)
