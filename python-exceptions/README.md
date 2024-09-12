# Python Exceptions

## Overview

This project contains Python scripts that demonstrate handling exceptions in various scenarios. Each script focuses on different aspects of error handling, from safely printing values to managing division and list operations.

## Files

Below is a list of the files in this project along with a brief description of what each script does. Click on the file names to view the content of each script.

### 1. [0-safe_print_list.py](./0-safe_print_list.py)

This script defines a function `safe_print_list(my_list, x)` that safely prints the first `x` elements of a list. It handles the `IndexError` exception if the list is shorter than `x`.

### 2. [1-safe_print_integer.py](./1-safe_print_integer.py)

This script defines a function `safe_print_integer(value)` that attempts to print an integer. It catches `TypeError` and `ValueError` exceptions if the value is not an integer.

### 3. [2-safe_print_list_integers.py](./2-safe_print_list_integers.py)

This script defines a function `safe_print_list_integers(my_list=[], x=0)` that prints the first `x` integers from a list, ignoring non-integer values. It raises an `IndexError` if the list is too short.

### 4. [3-safe_print_division.py](./3-safe_print_division.py)

This script defines a function `safe_print_division(a, b)` that performs division and handles the `ZeroDivisionError` exception. It uses a `finally` block to print the result, whether successful or not.

### 5. [4-list_division.py](./4-list_division.py)

This script defines a function `list_division(my_list_1, my_list_2, list_length)` that divides corresponding elements of two lists. It handles `TypeError`, `ValueError`, `ZeroDivisionError`, and `IndexError`, providing appropriate messages for each exception.

### 6. [5-raise_exception.py](./5-raise_exception.py)

This script defines a function `raise_exception()` that deliberately raises a `TypeError`.

### 7. [6-raise_exception_msg.py](./6-raise_exception_msg.py)

This script defines a function `raise_exception_msg(message)` that raises a `NameError` with a custom message.

## Contributing

If you would like to contribute to this project, please fork the repository, make your changes, and submit a pull request.