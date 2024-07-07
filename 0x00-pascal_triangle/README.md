# Pascal's Triangle Project

## Project Overview

**Project Duration:** June 24, 2024, 6:00 AM - June 28, 2024, 6:00 AM

In this project, you will implement a function to generate Pascal's Triangle. This exercise will help you revise fundamental Python concepts such as lists, list comprehensions, functions, loops, conditional statements, and arithmetic operations.

### Resources
- [What is Pascal’s Triangle](https://www.cuemath.com/algebra/pascals-triangle/)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?feature=shared&v=0iMtlus-afo)
- [What are Python Algorithms](https://builtin.com/data-science/python-algorithms)

### Must-Know Concepts

To successfully complete this project, review the following Python concepts:

#### Lists and List Comprehensions
- Creating, accessing, modifying, and iterating over lists.
- Utilizing list comprehensions for generating rows of Pascal’s Triangle.

#### Functions
- Defining and calling functions.
- Passing parameters and returning values, especially lists of lists representing Pascal’s Triangle.

#### Loops
- Using `for` and `while` loops to iterate through sequences.
- Employing nested loops for generating each row and calculating the values of Pascal’s Triangle.

#### Conditional Statements
- Applying `if`, `elif`, and `else` conditions for logic based on the position within Pascal’s Triangle.

#### Recursion (Optional)
- Understanding recursion for an alternative approach to generating Pascal’s Triangle.

#### Arithmetic Operations
- Performing addition for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.

#### Indexing and Slicing
- Accessing elements and slices of lists for identifying and summing elements when constructing each row.

#### Memory Management
- Being mindful of how lists are stored and copied when creating new rows.

#### Error and Exception Handling (Optional)
- Using `try-except` blocks for handling potential errors, such as invalid input types or values.

#### Efficiency and Optimization
- Considering time and space complexity for generating Pascal’s Triangle.
- Applying optimizations to improve performance.

### Tasks

#### 0. Pascal's Triangle (Mandatory)

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of `n`.

- Returns an empty list if `n <= 0`
- Assume `n` will always be an integer

**Example Usage:**
```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

