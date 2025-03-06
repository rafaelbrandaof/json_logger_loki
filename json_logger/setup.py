"""
This is the setup file for the json_logger_loki package.
It uses setuptools to manage the installation of the package and its dependencies.
"""
from setuptools import setup, find_packages

setup(
    name="json_logger_loki",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests", "opentelemetry-api"],
    author="Rafael Brandao Ferreira",
    description="A JSON logger with OpenTelemetry and Loki support",
    python_requires=">=3.7",
)
