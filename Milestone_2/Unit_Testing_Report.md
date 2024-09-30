# Unit Testing Report

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/XXXX/XXXXX.git

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.


## 1. **Test Summary**
list all tested functions related to the five required features and the corresponding test functions designed to test 
those functions, for example:

| **Tested Functions** | **Test Functions**                                             |
|----------------------|----------------------------------------------------------------|
| `add(x1,x2)`         | `test_add_valid()` <br> `test_add_invalid`                     |
| `divide(x1,x2)`      | `test_divide_valid()` <br> `test_divide_invalid`               |
| `multiply(a,b)`      | `test_multiply_valid()` <br> `test_multiply_invalid()`         |
| `subtract(a,b)`      | `test_subtract_valid()' <br> `test_subtract_invalid()`         |
| `process_data(data)` | `test_process_data_valid()' <br> `test_process_data_invalid()` |


---

## 2. **Test Case Details**

### Test Case 1: Division Operation
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - The divide function performs division between two numbers. It takes two arguments (a and b), where a is divided by b. The function should handle exceptions,                 particularly division by zero.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```
### Test Case 2: Addition Operation
- **Test Function/Module**
  - `test_add_valid()`
  - `test_add_invalid()`
- **Tested Function/Module**
  - `add(x1, x2)`
- **Description**
  - The add function performs the addition of two numbers. It accepts two parameters x1 and x2 and returns their sum.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `add(3, 2)`                   | `5`                 |
| `add(-1, 1)`                  | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_add_valid():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `add(3, "two")`               | `Handle TypeError`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_add_invalid():
    with pytest.raises(TypeError):
        add(3, "two")
```

### Test Case 3: Multiplication Operation
- **Test Function/Module**
  - `test_multiply_valid()`
  - `test_multiply_invalid()`
- **Tested Function/Module**
  - `multiply(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `multiply(2, 3)`              | `6`                 |
| `multiply(-2, 3)`             | `-6`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_multiply_valid():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `multiply(2, None)`           | `Handle TypeError`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_multiply_invalid():
    with pytest.raises(TypeError):
        multiply(2, None)
```

### Test Case 4: Subtraction Operation
- **Test Function/Module**
  - `test_subtract_valid()`
  - `test_subtract_invalid()`
- **Tested Function/Module**
  - `subtract(a, b)`
- **Description**
  - The subtract function returns the result of subtracting b from a.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `subtract(5, 3)`              | `2`                 |
| `subtract(-2, -3)`            | `1`                 |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_subtract_valid():
    assert subtract(5, 3) == 2
    assert subtract(-2, -3) == 1
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `subtract(5, None)`           | `Handle TypeError`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_subtract_invalid():
    with pytest.raises(TypeError):
        subtract(5, None)
```


### Test Case 5: Data Processing Function
- **Test Function/Module**
  - `test_process_data_valid()`
  - `test_process_data_invalid()`
- **Tested Function/Module**
  - `process_data(data)`
- **Description**
  - The process_data function performs operations on input data and returns processed results. It takes a dictionary as input and processes the values.
- **1) Valid Input and Expected Output**  

| **Valid Input**                  | **Expected Output** |
|----------------------------------|---------------------|
| `process_data({'a': 1, 'b': 2})` | `[1, 2]`            |
| `add more cases in necessary`    | `...`               |

- **1) Code for the Test Function**
```python
def test_process_data_valid():
    assert process_data({'a': 1, 'b': 2}) == [1, 2]
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `process_data(None)`          | `Handle ValueError` |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_process_data_invalid():
    with pytest.raises(ValueError):
        process_data(None)
```

### Test Case 6:

add more test cases if necessary.

## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./Unit_test.png)
