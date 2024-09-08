# 03_modules.py

# This script demonstrates how to use built-in and custom modules in Python.

# Importing a built-in module
import math

# Importing a custom module
import custom_module

def calculate_circle_area(radius):
    """Function to calculate the area of a circle given its radius."""
    return math.pi * (radius ** 2)

def main():
    # Using the imported math module
    print("Value of pi:", math.pi)
    
    # Using the custom module
    result = custom_module.greet("Alice")
    print(result)

    # Using the custom function
    radius = 5
    area = calculate_circle_area(radius)
    print(f"Area of the circle with radius {radius}: {area}")

if __name__ == "__main__":
    main()
