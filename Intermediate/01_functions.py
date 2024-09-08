# 01_functions.py

# This script demonstrates how to define and use functions in Python.

def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

def add(a, b):
    """Function to add two numbers."""
    return a + b

def main():
    # Calling the greet function
    name = "Alice"
    print(greet(name))

    # Calling the add function
    num1 = 10
    num2 = 5
    print("Sum:", add(num1, num2))

if __name__ == "__main__":
    main()
