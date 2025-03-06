
# JSON Logger Loki

A Python logging utility for logging JSON formatted logs, integrated with Loki for log aggregation. This project uses `uv` to manage dependencies, testing, and workflows.

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [GitHub Actions Workflows](#github-actions-workflows)
- [Contributing](#contributing)
- [License](#license)

## About

`json-logger-loki` is a Python-based logging utility that outputs logs in a structured JSON format. This log format is useful for log aggregation systems like **Loki**.

The project is managed using `uv`, which simplifies setting up Python virtual environments, installing dependencies, and running the project.

## Installation

### Prerequisites

Make sure you have `uv` installed. If not, install it by running:

```bash
pip install uv
```

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/rafaelbrandaof/json_logger_loki.git
   cd json_logger_loki
   ```

2. Install dependencies using `uv`:

   ```bash
   uv venv  # Creates a virtual environment
   uv pip install -e .  # Installs the dependencies in the current environment
   ```

## Usage

After setting up the project, you can use the `JSONLogger` class to log messages in JSON format.

### Example:

```python
from json_logger.logger import JSONLogger

# Initialize the logger
logger = JSONLogger(log_file="test.log", loki_url="http://localhost:3100/loki/api/v1/push", loki_labels={"job": "test_logger"})

# Log an info message
logger.info("This is an info log", module="test")

# Log an error message
logger.error("This is an error log", module="test")
```

Logs will be written to the specified log file in JSON format, and if Loki is configured, the logs will be pushed to the Loki server.

## Testing

To run tests, use `uv` to set up the virtual environment and install dependencies:

```bash
uv venv  # Creates a virtual environment
uv pip install -e .  # Installs dependencies
uv run pytest  # Run tests with pytest
```

### Linting and Code Style

To ensure your code follows Python's PEP-8 style guide, we use **flake8** and **pylint** for linting.

You can run these tools manually:

```bash
flake8 .  # Run flake8 for linting
pylint .  # Run pylint for linting
```

Or, these linters will run automatically in the GitHub Actions workflows.

## GitHub Actions Workflows

The project includes GitHub Actions workflows that automate testing and linting.

### Workflow: `python-lint.yml`

This workflow is triggered on every push and pull request to the `main` branch.

It does the following:

1. Installs Python 3.12 (as defined in the matrix).
2. Installs dependencies using `uv`.
3. Runs tests with `pytest`.
4. Lints the code with **flake8** and **pylint**.

You can find the workflow file in `.github/workflows/python-lint.yml`.

Here’s the content of the file:

```yaml
name: Python Linting and Testing

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.12"]

    steps:
    - uses: actions/checkout@v4

    - name: Install uv
      uses: astral-sh/setup-uv@v3
      with:
          enable-cache: true
          cache-dependency-glob: uv.lock

    - name: Set up Python ${{ matrix.python-version }}
      run: uv python install ${{ matrix.python-version }}

    - name: Install Venv
      run: uv venv

    - name: Install Dependencies
      run: uv pip install -e .

    - name: Test
      run: uv run pytest

    - name: Flake 8
      run: flake8 .

    - name: Pylint
      run: pylint .
```

### Additional Workflows

- **Continuous Integration (CI)**: The workflow ensures that tests are run and that the code adheres to the linting standards before being merged into the `main` branch.
- **Deployment**: In the future, you can add another workflow for automatic deployment to a server or PyPI.

## Contributing

If you want to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write tests for your changes.
4. Ensure that tests pass by running `pytest` and linting using `flake8` and `pylint`.
5. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
