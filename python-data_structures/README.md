# Python Data Structures

This repository contains a collection of Python scripts that demonstrate basic operations on lists, tuples, strings, and matrices. Each script is designed to perform a specific task and showcases fundamental data structure manipulations in Python.

## Directory Structure

The project directory `python-data_structures` contains the following files:

### [0-print_list_integer.py](0-print_list_integer.py)
Defines a function `print_list_integer(my_list)` that prints each integer in a list, with each integer on a new line.

### [1-element_at.py](1-element_at.py)
Defines a function `element_at(my_list, idx)` that returns the element at the specified index `idx` from the list `my_list`. Returns `None` if the index is out of range.

### [2-replace_in_list.py](2-replace_in_list.py)
Defines a function `replace_in_list(my_list, idx, element)` that replaces the element at index `idx` with `element` in the list `my_list`. Returns the modified list or the original list if the index is out of range.

### [3-print_reversed_list_integer.py](3-print_reversed_list_integer.py)
Defines a function `print_reversed_list_integer(my_list)` that prints each integer in a list in reverse order, with each integer on a new line.

### [4-new_in_list.py](4-new_in_list.py)
Defines a function `new_in_list(my_list, idx, element)` that creates a new list with the element at index `idx` replaced by `element`. Returns the new list while leaving the original list unchanged.

### [5-no_c.py](5-no_c.py)
Defines a function `no_c(my_string)` that returns a new string with all occurrences of the characters `'c'` and `'C'` removed.

### [6-print_matrix_integer.py](6-print_matrix_integer.py)
Defines a function `print_matrix_integer(matrix)` that prints each integer in a matrix (a list of lists) in a formatted manner, with integers separated by spaces.

### [7-add_tuple.py](7-add_tuple.py)
Defines a function `add_tuple(tuple_a, tuple_b)` that adds two tuples element-wise. Tuples with fewer than two elements are padded with zeroes. Returns a new tuple containing the sums.

### [8-multiple_returns.py](8-multiple_returns.py)
Defines a function `multiple_returns(sentence)` that returns a tuple containing the length of `sentence` and its first character. Returns `(0, None)` if `sentence` is empty.

### [9-max_integer.py](9-max_integer.py)
Defines a function `max_integer(my_list)` that returns the maximum integer in the list. Returns `None` if the list is empty.

### [10-divisible_by_2.py](10-divisible_by_2.py)
Defines a function `divisible_by_2(my_list)` that returns a list of boolean values indicating whether each element in `my_list` is divisible by 2.

### [11-delete_at.py](11-delete_at.py)
Defines a function `delete_at(my_list, idx)` that deletes the element at index `idx` from the list `my_list`. Returns the modified list or the original list if the index is out of range.

### [12-switch.py](12-switch.py)
A script that swaps the values of two variables `a` and `b` and prints the result.

## Usage

To use a specific script, run it using Python. For example, to use the `print_list_integer` function, execute:

```sh
python3 python-data_structures/0-print_list_integer.py
```

Make sure to modify the scripts if needed to provide the necessary inputs for testing.

## Dependencies

No external libraries or dependencies are required for these scripts.
