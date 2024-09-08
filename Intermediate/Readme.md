# Intermediate Python Programming

Welcome to the Intermediate Python Programming section! This folder explores more advanced topics and concepts that build upon the basics. Here, you'll find examples and explanations on object-oriented programming, modules, file handling, exception handling, and decorators.

## Introduction to Intermediate Concepts

As you progress from basic to intermediate Python programming, you'll encounter more complex concepts and tools. This section focuses on:
- **Object-Oriented Programming (OOP)**: Organizing code using classes and objects.
- **Modules**: Structuring and reusing code across different files.
- **File Handling**: Reading from and writing to files with error handling.
- **Exception Handling**: Managing errors gracefully.
- **Decorators**: Enhancing the functionality of functions.

## Intermediate Concepts

### 1. Object-Oriented Programming (OOP)

**File**: `01_oop.py`

**Explanation**: Object-Oriented Programming is a paradigm that uses "objects" to structure code. Objects are instances of classes, which can contain data (attributes) and functions (methods). This script introduces the concepts of classes, objects, inheritance, and encapsulation.

**Code Example**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def birthday(self):
        self.age += 1
        return f"Happy Birthday, {self.name}! You are now {self.age} years old."

# Creating an object of the Person class
person1 = Person("Alice", 30)
print(person1.greet())
print(person1.birthday())
```
- **Output**:
  ```
  Hello, my name is Alice and I am 30 years old.
  Happy Birthday, Alice! You are now 31 years old.
  ```

**Concepts Covered**:
- **Class Definition**: Creating a class with attributes and methods.
- **Object Instantiation**: Creating instances of the class.
- **Method Calls**: Calling methods on an object.

### 2. Modules

**File**: `02_modules.py`

**Explanation**: Modules are Python files that contain reusable code. You can import and use functions, classes, and variables defined in other modules. This script demonstrates how to create and use modules to organize code effectively.

**Code Example**:
```python
# math_operations.py (Module)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# main.py (Script using the module)
import math_operations

result_add = math_operations.add(10, 5)
result_subtract = math_operations.subtract(10, 5)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
```
- **Output**:
  ```
  Addition: 15
  Subtraction: 5
  ```

**Concepts Covered**:
- **Creating Modules**: Writing reusable code in separate files.
- **Importing Modules**: Using `import` to bring functions and classes into your script.

### 3. File Handling

**File**: `03_file_handling.py`

**Explanation**: File handling involves reading from and writing to files. This script demonstrates how to open files, read their contents, write data to files, and handle exceptions that may occur during file operations.

**Code Example**:
```python
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "Write successful."
    except IOError:
        return "Error writing to file."

# Example usage
print(write_file('example.txt', 'Hello, file!'))
print(read_file('example.txt'))
```
- **Output**:
  ```
  Write successful.
  Hello, file!
  ```

**Concepts Covered**:
- **Reading Files**: Using `open()` and `read()` to access file contents.
- **Writing Files**: Using `open()` and `write()` to modify file contents.
- **Exception Handling**: Handling file-related errors with `try` and `except`.

### 4. Exception Handling

**File**: `04_exceptions.py`

**Explanation**: Exception handling allows you to manage errors gracefully without stopping the execution of your program. This script shows how to use `try`, `except`, `else`, and `finally` blocks to handle and respond to exceptions.

**Code Example**:
```python
def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input type."
    else:
        return f"Result: {result}"
    finally:
        print("Execution completed.")

# Example usage
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
```
- **Output**:
  ```
  Result: 5.0
  Error: Cannot divide by zero.
  Execution completed.
  Execution completed.
  ```

**Concepts Covered**:
- **Handling Exceptions**: Using `try` and `except` to manage errors.
- **Finally Block**: Executing code after error handling.

### 5. Decorators

**File**: `05_decorators.py`

**Explanation**: Decorators are a way to modify or enhance functions without changing their actual code. This script demonstrates how to create and apply decorators to add functionality to existing functions.

**Code Example**:
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function.")
        result = func(*args, **kwargs)
        print("Something is happening after the function.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))
```
- **Output**:
  ```
  Something is happening before the function.
  Something is happening after the function.
  Hello, Alice!
  ```

**Concepts Covered**:
- **Creating Decorators**: Defining functions that modify other functions.
- **Applying Decorators**: Using the `@decorator` syntax to enhance functions.

## Conclusion

This intermediate section expands on basic Python concepts and introduces more advanced programming techniques. Mastery of these concepts will help you write more efficient, modular, and maintainable code. If you have questions or need further assistance, explore additional resources or seek help from the programming community.

Happy coding!
```

This `README.md` file provides an in-depth look at intermediate Python concepts, with detailed explanations and examples for each topic. Adjust or expand the content as necessary to fit your specific needs.
