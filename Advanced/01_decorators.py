# 01_decorators.py

# This script demonstrates how to use decorators in Python.

def my_decorator(func):
    """A simple decorator that prints a message before and after the function call."""
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

def main():
    # Calling the decorated function
    message = say_hello("Alice")
    print(message)

if __name__ == "__main__":
    main()
