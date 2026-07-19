# JourneyPrices

Compares the real cost, time, and value of different transport options so you can decide the smartest/cheapest way to travel, not just the fastest route.

## Setup

Requires Python 3.13+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

This installs the app's runtime dependencies (Flask) plus dev tooling (ruff, mypy).

## Linting and type checking

```bash
ruff check src
mypy src
```

Both also run automatically in CI on every push to `main` and on pull requests (see `.github/workflows/lint.yml`).
