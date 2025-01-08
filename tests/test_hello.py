"""Test cases for hello()."""

from pybotters_insiders import hello


def test_hello() -> None:
    """Check the return value of the hello() function."""
    assert hello() == "Hello from pybotters-insiders!"
