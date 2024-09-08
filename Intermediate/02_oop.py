# 02_oop.py

# This script demonstrates basic Object-Oriented Programming (OOP) concepts in Python.

class Person:
    def __init__(self, name, age):
        """Constructor to initialize the Person object."""
        self.name = name
        self.age = age

    def greet(self):
        """Method to return a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def birthday(self):
        """Method to increment the age of the person."""
        self.age += 1

def main():
    # Creating an instance of the Person class
    person1 = Person("Alice", 30)
    
    # Calling methods
    print(person1.greet())
    
    # Celebrate birthday
    person1.birthday()
    print("After birthday:", person1.greet())

if __name__ == "__main__":
    main()
