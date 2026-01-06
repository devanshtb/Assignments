from functools import reduce
from exceptions import NoValidDataError


def remove_invalid(values):     # it will Remove None values from a list
    
    valid = list(filter(lambda x: x is not None, values))
    if not valid:
        raise NoValidDataError("No valid numeric values provided.")
    return valid


def square_numbers(numbers):    #Square each number
    
    return list(map(lambda x: x ** 2, numbers))


def filter_even(numbers):        # Keep only even numbers.
    
    return list(filter(lambda x: x % 2 == 0, numbers))


def sum_numbers(numbers):     # Calculate the sum of numbers
    
    return reduce(lambda a, b: a + b, numbers, 0)
