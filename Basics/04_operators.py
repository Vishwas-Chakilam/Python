# 04_operators.py

# This script demonstrates different operators in Python.

def main():
    # Arithmetic Operators
    a = 10
    b = 5

    print("Arithmetic Operators:")
    print("a + b =", a + b)  # Addition
    print("a - b =", a - b)  # Subtraction
    print("a * b =", a * b)  # Multiplication
    print("a / b =", a / b)  # Division
    print("a % b =", a % b)  # Modulus
    print("a ** b =", a ** b)  # Exponentiation
    print("a // b =", a // b)  # Floor Division

    # Comparison Operators
    print("\nComparison Operators:")
    print("a == b:", a == b)  # Equal to
    print("a != b:", a != b)  # Not equal to
    print("a > b:", a > b)    # Greater than
    print("a < b:", a < b)    # Less than
    print("a >= b:", a >= b)  # Greater than or equal to
    print("a <= b:", a <= b)  # Less than or equal to

    # Logical Operators
    x = True
    y = False

    print("\nLogical Operators:")
    print("x and y:", x and y)  # Logical AND
    print("x or y:", x or y)    # Logical OR
    print("not x:", not x)      # Logical NOT

    # Assignment Operators
    c = 15
    c += 5
    print("\nAssignment Operators:")
    print("c += 5:", c)  # c = c + 5

    c -= 3
    print("c -= 3:", c)  # c = c - 3

    c *= 2
    print("c *= 2:", c)  # c = c * 2

    c /= 4
    print("c /= 4:", c)  # c = c / 4

if __name__ == "__main__":
    main()
