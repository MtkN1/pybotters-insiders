# pybotters-insiders
EXPERIMENTAL REPOSITORY FOR PYBOTTERS V2

## Contributing

### Requirements

- Python 3.10+
- uv
- Node.js (for `pyright`)

### Setup

- Install Python dependencies: `uv sync`
- Install Node.js dependencies: `npm install`

### Checks

- Run the test suite: `uv run -- pytest`
- Run the test suite with coverage: `uv run -- coverage run -m pytest`
- Run tests with coverage for all supported Python versions:
  1. `for v in 3.10 3.11 3.12 3.13 3.14; do uv run -p "$v" --isolated -- coverage run -p -m pytest; done`
  2. `uv run -- coverage combine`
- Show the coverage report: `uv run -- coverage report`
- Run Ruff lint checks: `uv run -- ruff check`
- Check formatting with Ruff: `uv run -- ruff format --check`
- Run Pyright type checks: `uv run -- npm exec --no -- pyright`
- Build the package: `uv build`
