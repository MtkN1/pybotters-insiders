# pybotters-insiders
EXPERIMENTAL REPOSITORY FOR PYBOTTERS V2

## Contributing

- Install `uv`

  https://docs.astral.sh/uv/getting-started/installation/
- Install dependencies
  ```console
  $ uv sync
  ```
- Run tests
  ```console
  $ uv run pytest
  ```
- Run linter
  ```console
  $ uv run ruff check
  ```
- Run formatter
  ```console
  $ uv run ruff format
  ```
- Run type checker

  Static code analysis is provided from the VS Code Pylance extension.
> [!IMPORTANT]
> To run in the CLI, there are [`pyright`](https://github.com/microsoft/pyright) (First-party, Node.js) and [`pyright-python`](https://github.com/RobertCraigie/pyright-python) (Third-paty, Python), but be careful to [synchronize versions with Pylance](https://github.com/microsoft/pylance-release/blob/main/USING_WITH_PYRIGHT.md#pyright-version-and-pylances-underlying-pyright-version-are-different).
