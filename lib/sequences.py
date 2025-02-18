#!/usr/bin/env python3

def print_fibonacci(length):
    """
    Prints a list of the Fibonacci sequence up to the specified length.

    Args:
      length: The desired length of the Fibonacci sequence.
    """

    fibonacci_list = []
    a, b = 0, 1

    if length <= 0:
        print(fibonacci_list)
        return

    fibonacci_list.append(a)

    if length == 1:
        print(fibonacci_list)
        return

    fibonacci_list.append(b)

    if length == 2:
        print(fibonacci_list)
        return


    for _ in range(2, length):
        next_fib = a + b
        fibonacci_list.append(next_fib)
        a, b = b, next_fib

    print(fibonacci_list)
