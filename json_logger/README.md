# JSON Logger with Loki Integration

A Python logger that outputs logs in JSON format and integrates with Loki for log storage and analysis.

## Installation

To install the package, run:

```bash
pip install json-logger-loki
```

## Usage

```python
from json_logger.logger import JSONLogger

# Initialize logger
logger = JSONLogger(log_file="my_log_file.log", loki_url="http://localhost:3100/loki/api/v1/push")

# Log messages
logger.info("This is an info message", module="example_module")
logger.error("This is an error message", module="example_module")
```

## Testing

To run tests, use:

```bash
pytest
```

## GitHub Actions Workflows

CI/CD workflows are set up using GitHub Actions to ensure linting, testing, and deployment. They run on each push and pull request to the `main` branch.
