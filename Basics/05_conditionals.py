# 05_conditionals.py

# This script demonstrates the use of conditional statements in Python.

def main():
    # Example of if-else statements
    age = 20

    print("Conditional Statements:")
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

    # Example of if-elif-else statements
    score = 85

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: D")

    # Example of nested if statements
    temperature = 30

    if temperature > 25:
        if temperature > 35:
            print("It's too hot!")
        else:
            print("The weather is warm.")
    else:
        print("The weather is cool.")

if __name__ == "__main__":
    main()
