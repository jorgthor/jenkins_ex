"""
The various functions that can be used in the calculator
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_number(number):
    """
    Check if the input is a number
    """
    if type(number) == int or type(number) == float:
        return True


def is_positive(number):
    """
    Check if the input is a positive number
    """
    if not is_number(number):
        return False
    return number > 0


def is_even(number):
    """
    Check if the input is an even number
    """
    if not is_number(number):
        return False
    return number % 2 == 0


def is_odd(number):
    """
    Check if the input is an odd number
    """
    if not is_number(number):
        return False
    return number % 2 != 0


def is_prime(number):
    """
    Check if the input is a prime number
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def add(a, b):
    """
    Add two numbers
    """
    if not is_number(a) or not is_number(b):
        return "Invalid input"
    return a + b


def subtract(a, b):
    """
    Subtract two numbers
    """
    if not is_number(a) or not is_number(b):
        return "Invalid input"
    return a - b


def multiply(a, b):
    """
    Multiply two numbers
    """
    if not is_number(a) or not is_number(b):
        return "Invalid input"
    return a * b


def divide(a, b):
    """
    Divide two numbers
    """
    if not is_number(a) or not is_number(b):
        return "Invalid input"
    if a == 0 or b == 0:
        return "Division by zero"
    return a / b


def power(a, b):
    """
    Calculate the power of a number
    """
    if not is_number(a) or not is_number(b):
        return "Invalid input"
    return a ** b


def percentage(a, b):
    """
    Calculate the percentage of a number
    """
    if not is_number(a) or not is_number(b):
        return "Invalid input"
    return (a * b) / 100
