import subprocess
import sys

import pytest
from convert import c_to_f, f_to_c


def test_celsius_to_fahrenheit_math():
    assert c_to_f(100) == pytest.approx(212.0)
    assert c_to_f(0) == pytest.approx(32.0)
    assert c_to_f(-40) == pytest.approx(-40.0)
    assert c_to_f(37) == pytest.approx(98.6)


def test_fahrenheit_to_celsius_math():
    assert f_to_c(32) == pytest.approx(0.0)
    assert f_to_c(212) == pytest.approx(100.0)
    assert f_to_c(-40) == pytest.approx(-40.0)
    assert f_to_c(98.6) == pytest.approx(37.0)


def test_cli_celsius_to_fahrenheit():
    result = subprocess.run(
        [sys.executable, "convert.py", "100", "C"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "212.0 F"
    assert result.stderr == ""


def test_cli_fahrenheit_to_celsius():
    result = subprocess.run(
        [sys.executable, "convert.py", "32", "F"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "0.0 C"
    assert result.stderr == ""


def test_cli_rejects_unknown_unit():
    result = subprocess.run(
        [sys.executable, "convert.py", "100", "K"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert result.stdout == ""
    assert "Unknown unit: K" in result.stderr


def test_cli_rejects_invalid_number():
    result = subprocess.run(
        [sys.executable, "convert.py", "abc", "C"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert result.stdout == ""
    assert "Invalid number: abc" in result.stderr


def test_cli_rejects_missing_arguments():
    result = subprocess.run(
        [sys.executable, "convert.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert result.stderr != ""
