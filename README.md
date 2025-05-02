# Python Concepts

A collection of Python concepts and examples showcasing various Python features, best practices, and patterns.

## Project Structure

```
python-concepts/
├── src/                    # Source code
│   └── python_concepts/    # Main package
│       └── examples/       # Example scripts
├── tests/                  # Test directory
└── docs/                   # Documentation
```

## Setup

1. Make sure you have Python 3.12 installed
2. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Install dependencies:
   ```bash
   poetry install
   ```

## Development

- Add new examples in `src/python_concepts/examples/`
- Add corresponding tests in `tests/`
- Run tests:
  ```bash
  poetry run pytest
  ```

## License

MIT 