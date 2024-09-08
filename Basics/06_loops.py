# 06_loops.py

# This script demonstrates the use of loops in Python.

def main():
    # For loop with range()
    print("For loop with range:")
    for i in range(5):
        print("Iteration", i)

    # For loop iterating over a list
    fruits = ["apple", "banana", "cherry"]
    print("\nFor loop over a list:")
    for fruit in fruits:
        print(fruit)

    # While loop
    count = 0
    print("\nWhile loop:")
    while count < 5:
        print("Count:", count)
        count += 1

    # Using break and continue statements in loops
    print("\nBreak and Continue:")
    for num in range(10):
        if num == 5:
            break  # Exit the loop
        if num % 2 == 0:
            continue  # Skip the rest of the loop body
        print(num)

if __name__ == "__main__":
    main()
