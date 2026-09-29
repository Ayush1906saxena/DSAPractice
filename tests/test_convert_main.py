import pytest
from convert import main, parse_args


def test_main_celsius_to_fahrenheit(capsys):
    assert main(["100", "C"]) == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "212.0 F"
    assert captured.err == ""


def test_main_fahrenheit_to_celsius(capsys):
    assert main(["32", "F"]) == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "0.0 C"
    assert captured.err == ""


def test_main_converts_decimal_celsius(capsys):
    assert main(["37.0", "C"]) == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "98.6 F"


def test_main_converts_negative_fahrenheit(capsys):
    assert main(["-40", "F"]) == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "-40.0 C"


def test_main_rejects_unknown_unit(capsys):
    assert main(["100", "K"]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "Unknown unit: K" in captured.err


def test_main_rejects_invalid_number(capsys):
    assert main(["abc", "C"]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "Invalid number: abc" in captured.err


def test_main_preserves_original_unit_case_in_error(capsys):
    assert main(["100", "k"]) == 1
    captured = capsys.readouterr()
    assert "Unknown unit: k" in captured.err


def test_main_rejects_missing_arguments():
    with pytest.raises(SystemExit) as exc_info:
        main([])
    assert exc_info.value.code != 0


def test_main_accepts_lowercase_celsius_unit(capsys):
    assert main(["100", "c"]) == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "212.0 F"


def test_main_accepts_lowercase_fahrenheit_unit(capsys):
    assert main(["32", "f"]) == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "0.0 C"


def test_parse_args_returns_parsed_arguments():
    args = parse_args(["100", "C"])
    assert args.value == "100"
    assert args.unit == "C"


def test_parse_args_requires_both_arguments():
    with pytest.raises(SystemExit) as exc_info:
        parse_args([])
    assert exc_info.value.code != 0
