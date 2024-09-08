# expense_tracker.py

import csv
from datetime import datetime

EXPENSE_FILE = 'expenses.csv'

def load_expenses():
    """Load expenses from a CSV file."""
    expenses = []
    try:
        with open(EXPENSE_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    """Save expenses to a CSV file."""
    with open(EXPENSE_FILE, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

def add_expense(expenses):
    """Add a new expense."""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    amount = input("Enter the amount: ")
    expense = {
        'date': date,
        'category': category,
        'amount': amount
    }
    expenses.append(expense)
    print("Expense added.")

def view_expenses(expenses):
    """View all expenses."""
    if not expenses:
        print("No expenses to display.")
    else:
        print("\nYour Expenses:")
        total = 0.0
        for expense in expenses:
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}")
            total += float(expense['amount'])
        print(f"\nTotal Expenses: {total}")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            save_expenses(expenses)
            print("Expenses saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
