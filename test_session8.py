import session8 as main
import pytest
import random
import os
import inspect
import re
import math
import functools
random_list = random.choices(range(1000), k=5)


main_funcs = [func for func in inspect.getmembers(main) if inspect.isfunction(func[1])]



README_CONTENT_CHECK_FOR = ['add', 'counter', 'counter_without_dict', 'div', 'docstring_check_wrapper', 'fibonacci_wrapper', 'mul']

CHECK_FOR_THINGS_NOT_ALLOWED = []

def test_for_docstrings():
    for func in main_funcs:
        assert func[1].__doc__ , f'Function {func[0]} has no doc string'

def test_for_annotations():
    for func in main_funcs:
        assert func[1].__annotations__ , f'Function {func[0]} has no annotations'



def test_docstring_check_wrapper_no_docstring():
    checker = main.docstring_check_wrapper()
    def aa():
        pass
    assert checker(aa) == False, 'Should return False for no doc string'

def test_docstring_check_wrapper_50_words_doc():
    checker = main.docstring_check_wrapper()
    def aa():
        pass
    aa.__doc__ = '1'*50
    assert checker(aa) == False, 'Should return False for doc string with 50 words'

def test_docstring_check_wrapper_51_words_doc():
    checker = main.docstring_check_wrapper()
    def aa():
        pass
    aa.__doc__ = '1'*51
    assert checker(aa) == True, 'Should return False for doc string with 51 words'

def test_fibonacci_wrapper():
    fn = main.fibonacci_wrapper()
    first_10 = [fn() for _ in range(10)]
    assert first_10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 'Check your fibonacci func'

def test_counter_add():
    counter_add = main.counter(main.add)
    n = random.randint(1,20)
    _ = [counter_add(1,2) for i in range(n)]
    assert main.counter_dict.get('add') == n, 'Add counter not working'

def test_counter_mul():
    counter_add = main.counter(main.mul)
    n = random.randint(1,20)
    _ = [counter_add(1,2) for i in range(n)]
    assert main.counter_dict.get('mul') == n, 'Mul counter not working'

def test_counter_div():
    counter_add = main.counter(main.div)
    n = random.randint(1,20)
    _ = [counter_add(1,2) for i in range(n)]
    assert main.counter_dict.get('div') == n, 'Div counter not working'


def test_counter_without_dict_add():
    dict1 = {}
    counter_add = main.counter_without_dict(main.add)
    n = random.randint(1,20)
    _ = [counter_add(1,2, _dict= dict1) for i in range(n)]
    assert dict1.get('add') == n, f'Add counter with {_dict}  not working'

def test_counter_without_dict_mul():
    dict1 = {}
    counter_add = main.counter_without_dict(main.mul)
    n = random.randint(1,20)
    _ = [counter_add(1,2, _dict= dict1) for i in range(n)]
    assert dict1.get('mul') == n, f'Mul counter with {_dict}  not working'

def test_counter_without_dict_div():
    dict1 = {}
    counter_add = main.counter_without_dict(main.div)
    n = random.randint(1,20)
    _ = [counter_add(1,2, _dict= dict1) for i in range(n)]
    assert dict1.get('div') == n, f'Div counter with {_dict}  not working'

def test_add():
    a,b = random.randint(1,100), random.randint(1,100)
    out = main.add(a,b)
    assert a+b == out, f'Add function not working for {a} and {b} gives {out}'

def test_mul():
    a,b = random.randint(1,100), random.randint(1,100)
    out = main.mul(a,b)
    assert a*b == out, f'Mul function not working for {a} and {b} gives {out}'

def test_div():
    a,b = random.randint(1,100), random.randint(1,100)
    out = main.div(a,b)
    assert a/b == out, f'Div function not working for {a} and {b} gives {out}'



def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(main)
    spaces = re.findall('\n +.', lines)
    for count, space in enumerate(spaces):
        assert len(space) % 4 == 2, f"Your script contains misplaced indentations at \
n'th postion {count+1} starting \n with {space}"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(main, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
