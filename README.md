<div align="center">

# Structura (Python)

**Scaffold production-ready Python backends in one command.**

[![PyPI](https://img.shields.io/pypi/v/structura-py.svg)](https://pypi.org/project/structura-py/)
[![Downloads](https://static.pepy.tech/badge/structura-py)](https://pepy.tech/project/structura-py)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## Why

Starting a new backend means the same half hour every time: create folders, decide where routes
and services live, set up a virtual environment, install the same dependencies, write an `.env`
loader. It's mechanical work that's easy to do inconsistently.

Structura does it in one command, with the architecture pattern you choose, so every project you
start looks the same and is laid out the way it should be.

> Also available for Go — see [structura-go](https://github.com/ShyamSundhar1411/structura-go).

## Features

- **Four architecture patterns** — MVC, MVC-API, MVCS, and Hexagonal
- **Framework support** — Flask and FastAPI, with boilerplate wired up
- **Dependency management** — works with `venv`, `pipenv`, or `poetry`
- **YAML-driven templates** — every structure and dependency set is a YAML file you can edit or extend
- **Boilerplate generation** — creates config and environment files alongside the folder tree
- **Cross-platform** — Windows, macOS, and Linux

## Install

```bash
pip install structura-py
```

## Usage

**Create a new project**

```bash
structura init myproject --framework flask
```

```bash
structura init myproject --framework fastapi
```

**Choose an architecture**

```bash
structura init myproject --framework fastapi --architecture hexagonal
```

Supported values: `mvc`, `mvc-api`, `mvcs`, `hexagonal`.

Run `structura --help` to see all available flags.

## Architecture patterns

| Pattern | Best for |
|---|---|
| **MVC** | Conventional web apps with server-rendered views |
| **MVC-API** | REST APIs that don't need a view layer |
| **MVCS** | Apps where business logic deserves its own service layer |
| **Hexagonal** | Domain-centric designs that isolate business rules from adapters and I/O |

## Customising templates

Structures and dependency sets live as YAML under `structura_py/templates/`. To change what gets
generated, edit the relevant template or add your own — no code changes needed.

```
structura_py/
├── cli.py                  # CLI entry point
├── commands/               # Command implementations
├── models/                 # Project, architecture, and dependency models
├── utils/                  # File, prompt, and command helpers
└── templates/              # YAML architecture + dependency definitions
```

## Built with

Python · [Poetry](https://python-poetry.org/) · YAML-based templating · pre-commit

## Contributing

Issues and pull requests welcome. Adding a new architecture or framework is usually just a new
YAML template — a good first contribution.

## License

MIT — see [LICENSE](LICENSE).
