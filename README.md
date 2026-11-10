# JourneyPrices

Compares the real cost, time, and value of different transport options so you can decide the smartest/cheapest way to travel, not just the fastest route.

## Run it

You need [uv](https://docs.astral.sh/uv/). It installs Python 3.14 for you if you don't have it.

Run these commands from the repo root:

```sh
uv sync
uv run python src/main.py
```

Then open <http://127.0.0.1:5000>.

`uv sync` creates `.venv` and installs the exact versions in `uv.lock`, including the `dev` group (ruff, mypy and pytest). Dependencies are defined in `pyproject.toml`.

The server runs in debug mode, so only use it locally.

## Check the code

Run these before you commit. All three must pass:

```sh
uv run ruff check .
uv run ruff format --check .
uv run mypy .
```

`uv run ruff check --fix .` and `uv run ruff format .` fix most lint and format errors for you.

The same checks run in CI on every push to `main` and on pull requests (see `.github/workflows/lint.yml`).

## Update dependencies

Dependabot opens a PR each week when a dependency has a new release. To update by hand, run `uv lock --upgrade`, then `uv sync`, then the checks above.
