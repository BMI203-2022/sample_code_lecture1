#!/usr/bin/env python3

import numpy as np
import sys


def subtract(x, y):
    """
    I love to comment
    """
    return x - y

def add(x: int, y: int) -> int:
    """
    Don't forget to comment
    """
    return x + y

def log_output(
        some_number_a,
        some_number_b,
        their_sum,
        their_difference,
        to_stdout=True):
    """
    prints the output to stdout 
    or to stderr
    """
    if to_stdout:
        file_handle=sys.stdout
    else:
        file_handle=sys.stderr

    print(
        f"Here are the numbers: {some_number_a}, {some_number_b}",
        file=file_handle)
    print(
        f"Here is their sum: {their_sum}",
        file=file_handle)
    print(
        f"Here is their difference: {their_difference}",
        file=file_handle)

def main():
    """
    This is a useful comment
    """
    
    # create some numbers
    some_number_a = np.random.randint(0, 100)
    some_number_b = np.random.randint(0, 100)

    # do some math
    their_sum = add(some_number_a, some_number_b)
    their_difference = subtract(some_number_a, some_number_b)

    # tell the user (stdout)
    log_output(
        some_number_a, some_number_b,
        their_sum, their_difference)

    # tell the user (stderr)
    log_output(
        some_number_a, some_number_b,
        their_sum, their_difference,
        to_stdout=False)

if __name__ == "__main__":
    main()


