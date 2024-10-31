[![PyTest CI](https://github.com/BrandonFoster/softloq-build/actions/workflows/pytest-ci.yml/badge.svg)](https://github.com/BrandonFoster/softloq-build/actions/workflows/pytest-ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# softloq-build
Python console app for building C++ apps, libs, and tests

# Installation
`> python -m pip install -e .`

# Uninstall
`> python -m pip uninstall softloq-build`

# Running Tests
pytest must be installed: `> pip install pytest`

run pytest in the project directory: `> pytest`

# Usage Example
The build system uses cmake in the background

# Using command-line interface
## Help
Displays help guideline.

`> softloq-build --help`

## Version
Displays the version.

`> softloq-build --version`

## Shell Mode
Enters shell mode with more options enabled.

`> softloq-build --shell`

Extra Shell Mode Options:
### Exiting
Exits shell mode.

`softloq-build> exit`
