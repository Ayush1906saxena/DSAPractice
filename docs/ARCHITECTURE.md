# Architecture

A single-file Python command-line tool that converts a temperature value between Celsius and Fahrenheit. It validates the input, performs the conversion, and prints the result or a clear error message.

**Built with a plain Python 3 command-line program with no web framework and no database. The customer only asked for a simple command-line conversion, so Python's built-in standard library is enough and keeps the tool easy to run and test.**

- Language: python
- Framework: none
- Storage: none
- Tests: pytest

## Parts

- **CLI entry point**: Reads command-line arguments, validates the number and unit, calls the converter, and prints the result or an error message. (convert.py)
- **Temperature converter**: Contains the formulas for converting Celsius to Fahrenheit and Fahrenheit to Celsius. (convert.py)
- **Tests**: Checks correct conversions, unknown unit handling, and invalid number handling using pytest. (tests/test_convert.py)

## How it's used

- `convert <value> <unit> -> prints '<result> <target_unit>' on stdout; unknown unit prints 'Unknown unit: <unit>' on stderr and exits 1; non-number prints 'Invalid number: <value>' on stderr and exits 1. Example: 'convert 100 C' prints '212.0 F'; 'convert 32 F' prints '0.0 C'.`: The only way a user runs the tool from the terminal.
- `c_to_f(celsius: float) -> float; f_to_c(fahrenheit: float) -> float. These functions are used by the CLI and tested directly.`: Lets tests verify the conversion math without running a subprocess.

## Trade-offs

- Use argparse for command-line parsing rather than Parse sys.argv manually: argparse gives clear error messages for missing arguments and is part of Python's standard library.
- Use float for temperature values rather than Use Decimal for exact decimal arithmetic: Float is simpler and sufficient for everyday temperature conversions; Decimal would add complexity without a noticeable benefit.
- Support only C and F units rather than Support Kelvin and other temperature scales: The customer only asked for Celsius and Fahrenheit, so extra units would be unused scope.

## Risks

- Very large or unusual float inputs could produce tiny rounding differences in the output.
- Users might type a decimal comma or extra spaces, which would be rejected as an invalid number.
- The tool has no external dependencies, so there is no risk from network or third-party service outages.

## Not included

- A graphical user interface or web interface
- Saving conversion history to a file or database
- Batch conversion of files or lists
- Support for Kelvin or other temperature units
- Packaging or distribution via PyPI

