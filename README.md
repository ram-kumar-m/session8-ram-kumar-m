# Assignment 8
**1.Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 200**
```python
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
```
**2.Write a closure that gives you the next Fibonacci int - 100**
   
```python 
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
```
**3.We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts - 250**

```python 
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
```
**4.Modify above such that now we can pass in different dictionary variables to update different dictionaries - 250**

```python
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
```


## **Test Cases (Pytest)**
>The names of the tests are so that `'test_'` prefix is added to the function it tests, suffied by the what the test does.

### test_readme_exists
   Checks if there is a README.md file in the same folder.

### test_readme_contents
   Checks if the README.md file has alteast 500 words.

### test_readme_proper_description
   Checks if the required functions are present in the README.md file.

### test_readme_file_for_formatting
   Checks if there are adequete headings present in the README.md file.

### test_indentations
   Checks if proper indentations are present throughout the python file.
   using the rule of 4 spaces equals 1 Tab.

### test_function_name_had_cap_letter
   Checks if any one the functions have capital letters used in their names, which breaks the PEP8 conventions.
   
### ***Annotation and Docstring tests***
tests if any of the functions in function list don't have annotations or docstrings
1. `add`
2. `counter`
3. `counter_without_dict`
4. `div`
5. `docstring_check_wrapper`
6. `fibonacci_wrapper`
7. `mul`


###  test_for_annotations
   Checks if the given number is present in the fibonacci series.


### test_docstring_check_wrapper_no_docstring
   Should return False for no doc string

### test_docstring_check_wrapper_50_words_doc
   Should return False for doc string with 50 words

### test_docstring_check_wrapper_51_words_doc
   Should return False for doc string with 51 words

### test_fibonacci_wrapper
   Check your fibonacci func

### test_counter_add
   Add counter not working

### test_counter_mul
   Mul counter not working

### test_counter_div
   Div counter not working

### test_counter_without_dict_add
   Add counter with dictionary  not working

### test_counter_without_dict_mul
   Mul counter with dictionary  not working

### test_counter_without_dict_div
   Div counter with dictionary  not working

### test_add
   Test add function

### test_mul
   Test multiplication function

### test_div
   Test division function