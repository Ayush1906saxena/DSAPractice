#!/usr/bin/env python3
"""A small command-line tool that converts temperatures between Celsius and Fahrenheit."""

import argparse
import sys


def c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert a temperature between Celsius and Fahrenheit."
    )
    parser.add_argument("value", help="The temperature value to convert.")
    parser.add_argument("unit", help="The unit of the temperature (C or F).")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    try:
        value = float(args.value)
    except ValueError:
        print(f"Invalid number: {args.value}", file=sys.stderr)
        return 1

    unit = args.unit.upper()
    if unit == "C":
        result = c_to_f(value)
        target_unit = "F"
    elif unit == "F":
        result = f_to_c(value)
        target_unit = "C"
    else:
        print(f"Unknown unit: {args.unit}", file=sys.stderr)
        return 1

    print(f"{result} {target_unit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
