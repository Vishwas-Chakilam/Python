# 05_exceptions.py

# This script demonstrates how to handle exceptions in Python.

def divide_numbers(x, y):
    """Function to divide two numbers and handle division by zero."""
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def main():
    # Test division
    num1 = 10
    num2 = 0
    print("Dividing numbers:")
    result = divide_numbers(num1, num2)
    print(result)

    # Test valid division
    num2 = 2
    result = divide_numbers(num1, num2)
    print("Result of division:", result)

if __name__ == "__main__":
    main()
