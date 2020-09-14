import random
import math
from collections import defaultdict
import types
'''
1.Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 200
2.Write a closure that gives you the next Fibonacci int - 100
3.We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts - 250
4.Modify above such that now we can pass in different dictionary variables to update different dictionaries - 250
--No readme or no docstring for each function, or no test cases, 0. Write test cases to check boundary conditions that might cause your code to fail. 
'''


def docstring_check_wrapper() -> types.FunctionType:
    """Wrapper for docstring_check functiom 

    Args:
        func ([type]): callable function of any kind

    Returns:
        []: Nothing, empty wrapper
    """

    MAX_CHAR = 50

    def docstring_check(func) -> bool:
        """Returns True if docstring of func > 50 else returns False

        Returns:
            bool: True or False
        """

        return True if (bool(func.__doc__) and len(func.__doc__) > MAX_CHAR) else False
    return docstring_check


def fibonacci_wrapper() -> types.FunctionType:
    """ Empty Wrapper for fibonacci func """
    previous = 0
    current = 1

    def next_fibonacci() -> int:
        """Returns the next int in the fibonacci series

        Returns:
            int: fibonacci int
        """

        nonlocal current
        nonlocal previous

        temp, previous, current = previous, current, current + previous

        return temp

    return next_fibonacci


def add(x: int, y: int) -> int:
    """Adds given two ints

    Args:
        x (int): an int
        y (int): an int 

    Returns:
        int: addition of two given ints
    """
    return x+y


def mul(x: int, y: int) -> int:
    """Multiplies given two ints

    Args:
        x (int): an int
        y (int): an int 

    Returns:
        int: Multiplication of two given ints
    """
    return x*y


def div(x: int, y: int) -> int:
    """Divides given two ints

    Args:
        x (int): an int
        y (int): an int 

    Returns:
        int: Division of two given ints
    """
    return x/y

counter_dict = dict()

def counter(fn: types.FunctionType) -> types.FunctionType:
    """    Wrapper for counter 

    Args:
        fn (types.FunctionType): An input function to track

    Returns:
        types.FunctionType: a clousre with the input function
    """

    cnt = 0

    def inner(*args, **kwargs):
        """An Executioner of counter

        Returns:
            : Result of the function that was sent to the wrapper with the given vars
        """
        nonlocal cnt
        global counter_dict
        cnt += 1
        counter_dict[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner


def counter_without_dict(fn: types.FunctionType) -> types.FunctionType:
    """Wrapper for counter with manual input of dictionary

    Args:
        fn (types.FunctionType): Any function you want to count

    Returns:
        types.FunctionType: a clousre with the input function with a counter inbuilt
    """

    cnt = 0

    def inner(*args, _dict: dict, **kwargs):
        """A counter where you have to input a func 

        Args:
            _dict (dict): required, a dict where you want to keep counts on 

        Returns:
            [type]: Execution of the given func with the given inputs 
        """
        nonlocal cnt
        cnt += 1
        _dict[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner
