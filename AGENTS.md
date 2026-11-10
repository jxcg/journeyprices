# Agent Instructions

## Write for humans and agents

Write issues, code, comments, commits and PRs so both a human and an agent can understand them without extra context.

- Say what changed and why. Don't assume the reader saw the conversation.
- Use plain language and descriptive names.
- Name exact files, commands and issue numbers instead of saying "the file" or "that bug".

## Layout

- `src/main.py` is the Flask app. Its templates are in `src/templates/`.
- `src/transport_modalities/` holds the journey classes. `src/units.py` holds unit constants.
- `src` is the import root, so write `from units import ...` and `from transport_modalities.Journey import Journey`.

## Code checks

The project uses Python 3.14 or newer and uv. Run `uv sync` to set up, and `uv run python src/main.py` to start the app.

Run `uv run ruff check .`, `uv run ruff format --check .` and `uv run mypy .` before every commit. All three must pass. Configuration lives in `pyproject.toml`. `.github/workflows/lint.yml` runs the same three checks on every pull request.

## Dependencies

- Add or remove dependencies with `uv add` and `uv remove`, never by hand-editing `uv.lock`. Commit `uv.lock` with the change.
- Use the latest release. Check the version on PyPI, not from memory, and set it as the minimum in `pyproject.toml`.

## Commits

- Subject line uses a conventional prefix: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `build:`, `chore:`.
- The body is 3-4 bullet points, each one or two sentences.
- Each bullet says what changed and why.

Example:

```
build: manage dependencies with uv

- Add `uv.lock` and `.python-version`, so every install gets the same versions on Python 3.14.
- Move ruff, mypy and pytest to a `[dependency-groups]` dev group, which `uv sync` installs by default.
- Run the checks in `.github/workflows/lint.yml` through `uv run`, so CI uses the locked versions.
```

## Pull requests

- Never commit or push to `main`. Do all work on a branch.
- Every PR references its GitHub issue. Put `Closes #<number>` in the description so the issue closes on merge.
- If no issue exists, create one with `gh issue create` before opening the PR.
- Name branches `scm-<issue-number>`, for example `scm-3` or `scm-7`. `scm` stands for source code modification. A type prefix and a short slug are optional: `docs/scm-3`, `scm-3-readme-run-instructions` and `docs/scm-3-readme-run-instructions` are all valid.
- The description is 3-4 bullets of one or two sentences, unless the change needs more.
