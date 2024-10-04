# Coverage Testing Report

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/XXXX/XXXXX.git

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.

You should perform statement coverage testing and branch coverage testing. For each type, provide a description and an analysis explaining how you evaluated the coverage.

## 1. **Test Summary**
list all tested functions related to the five required features, for example:

| **Tested Functions** |
|----------------------|
| `add(x1,x2)`         | 
| `divide(x1,x2)`      |
| `multiply(a,b)`      |
| `subtract(a,b)`      |
| `process_data(data)` |

---

## 2. **Statement Coverage Test**

### 2.1 Description

Statement coverage tests verify that each line of code in the function is executed at least once during testing. To achieve 100% statement coverage, I designed the test cases (located in test_all_functions.py) to ensure that every line of each function is executed.

For example:

- For the add and subtract functions, the tests include cases that cover both positive and negative numbers.
- For the divide function, cases for valid inputs (e.g., divide by non-zero) and invalid inputs (e.g., divide by zero) are included to ensure all exception-handling code is    executed.
- Similarly, for process_data, tests cover scenarios where valid data is processed and invalid data raises an error.

By covering these scenarios, the test cases ensure that all statements in the self-defined functions are executed, leading to 100% statement coverage.

### 2.2 Testing Results
You can use the following command to run the statement coverage test and generate the report in the terminal. Afterward, include a screenshot of the report. 

You must provide the test_all_functions.py file, which contains all test functions, otherwise pytest will not be able to execute the tests.

```commandline
pytest --cov=all_functions --cov-report=term
```
Note: In the command above, the file/module `all_functions` does not include the .py extension. all_functions.py should contain all the tested functions related to the five required features.

![Statement Coverage Test.png](Statement%20Coverage%20Test.png)

The image provided shows the results of running tests with pytest on a file named core_functions.py using the --cov option for code coverage.

Here’s a breakdown of the output:

- Tests Summary: All three tests in test_all_functions.py passed.
- Coverage: core_functions.py has 27 statements, with 1 missed, resulting in a 96% coverage rate.
- Execution Time: The tests took 2.53 seconds to complete.

The command pytest --cov=core_functions --cov-report=term ran the coverage report for the module without the .py extension, following the expected format.

## 3. **Branch Coverage Test**

### 3.1 Description

Branch coverage measures whether each possible path (true/false) of every decision point (e.g., if statements) in the code is executed. To achieve 100% branch coverage, the test cases in test_all_functions.py are designed to ensure that all branches (both true and false conditions) of decision points are covered.

For example:

- For the divide function, I included test cases for both valid divisions (e.g., divide(10, 2)) and invalid divisions (e.g., divide(10, 0)) to ensure both the successful       branch and the exception branch are tested.
- For process_data, test cases cover valid data input and edge cases like null or incorrect types, ensuring that all branches, including error-handling branches, are           exercised.

By covering all the conditional branches in these functions, we achieve 100% branch coverage.

### 3.2 Testing Results
You can use the following command to run the branch coverage test and generate the report in the terminal. Afterward, include a screenshot of the report. 

You must provide the test_all_functions.py file, which contains all test functions, otherwise pytest will not be able to execute the tests.

```commandline
pytest --cov=all_functions --cov-branch --cov-report=term
```
Note: In the command above, the file/module `all_functions` does not include the .py extension. all_functions.py should contain all the tested functions related to the five required features.

![Branch Coverage Test.png](Branch%20Coverage%20Test.png)
