# 02_generators.py

# This script demonstrates how to use generators in Python.

def count_up_to(max):
    """A generator function that counts up to a maximum value."""
    count = 1
    while count <= max:
        yield count
        count += 1

def main():
    # Using the generator
    print("Counting up to 5:")
    for number in count_up_to(5):
        print(number)

if __name__ == "__main__":
    main()
