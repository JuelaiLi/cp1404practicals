# CP1404/CP5632 Practical
# Testing demo using assert and doctest

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)  # fix the function to pass the failing test


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length  # fix the function to pass the failing test


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # assert tests to check if Car sets the fuel correctly
    test_car_with_fuel = Car(fuel=10)
    assert test_car_with_fuel.fuel == 10, "Car does not set fuel correctly when fuel is passed"
    test_car_default_fuel = Car()
    assert test_car_default_fuel.fuel == 0, "Car does not set default fuel correctly"


run_tests()

# Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


def format_sentence(phrase):
    """Format a phrase as a sentence, starting with a capital and ending with a single full stop."""
    pass  # placeholder function body

# doctests for format_sentence function
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# 'this is a test' -> 'This is a test.'
# test this and watch the tests fail
# then write the body of the function so that the tests pass
