import pytest

# Example function definitions to be tested
def add(x1, x2):
    return x1 + x2

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def process_data(data):
    if data is None:
        raise ValueError("Invalid data provided.")
    return list(data.values())


# Test cases for addition operation
def test_add_valid():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0

def test_add_invalid():
    with pytest.raises(TypeError):
        add(3, "two")


# Test cases for division operation
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5

def test_divide_invalid():
    with pytest.raises(ValueError):
        divide(10, 0)


# Test cases for multiplication operation
def test_multiply_valid():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6

def test_multiply_invalid():
    with pytest.raises(TypeError):
        multiply(2, None)


# Test cases for subtraction operation
def test_subtract_valid():
    assert subtract(5, 3) == 2
    assert subtract(-2, -3) == 1

def test_subtract_invalid():
    with pytest.raises(TypeError):
        subtract(5, None)


# Test cases for data processing function
def test_process_data_valid():
    assert process_data({'a': 1, 'b': 2}) == [1, 2]

def test_process_data_invalid():
    with pytest.raises(ValueError):
        process_data(None)


# Add more test cases if necessary
