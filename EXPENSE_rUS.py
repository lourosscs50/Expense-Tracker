import os
from typing import Any

import amt

FILE_NAME = "expenses.txt"

def load_expense():
    expenses: list[Any] = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                description, amount = line.strip().split('|')
                expenses.append((description, float(amount)))
    return expenses

def save_expenses(expenses) :
    with open(FILE_NAME, 'w') as file:
        for description, amount in expenses:
            file.write(f"{description} {amount})\n")

def show_menu():
    print("\n=== Expense Tracker ===") #
    print("1. Add expense")
    print("2. Add income")
    print("3. View balance")
    print("4. View transactions")
    print("5. Exit")

def add_transaction(expenses, is_income=False):
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    if not is_income:
        amount = amount # Expenses are negative
        expenses.append((description, amount))
        save_expenses(expenses)
        print("Transaction saved.")

def view_balance(expenses):
    balance = sum(amount for _, amount in expenses)
    print(f"Current balance: ${balance: .2f}")

def view_transactions(expenses):
    if not expenses:
        print("No transactions recorded.")
        for desc, amount in expenses:
            print(f"{desc}: ${amt:.2f}")

def main():
    expenses = load_expense()
    while True:
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_transaction(expenses, is_income=False)
        elif choice == '2':
            add_transaction(expenses, is_income=True)
        elif choice == '3':
            view_balance(expenses)
        elif choice == '4':
            view_transactions(expenses)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()