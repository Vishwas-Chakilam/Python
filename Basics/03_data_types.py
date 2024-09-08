# 03_data_types.py

# This script demonstrates the different built-in data types in Python.

def main():
    # Integer
    number = 10
    print("Integer:", number, type(number))

    # Float
    pi = 3.14159
    print("Float:", pi, type(pi))

    # String
    greeting = "Hello, Python!"
    print("String:", greeting, type(greeting))

    # Boolean
    is_valid = False
    print("Boolean:", is_valid, type(is_valid))

    # List
    fruits = ["apple", "banana", "cherry"]
    print("List:", fruits, type(fruits))

    # Tuple (immutable list)
    coordinates = (10.0, 20.0)
    print("Tuple:", coordinates, type(coordinates))

    # Set (unordered collection of unique elements)
    unique_numbers = {1, 2, 3, 3, 4}
    print("Set:", unique_numbers, type(unique_numbers))

    # Dictionary (key-value pairs)
    student = {
        "name": "John",
        "age": 21,
        "is_graduate": True
    }
    print("Dictionary:", student, type(student))

if __name__ == "__main__":
    main()
