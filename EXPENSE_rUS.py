import os

import amt

FILE_NAME = "expenses.txt"

def show_category_chart(expenses, plt=None):
    if not expenses:
        print("No data to chart.")
        return

    # Sum by category
    category_totals = {}
    for _, amount, category in expenses:
        category_totals[category] = category_totals.get(category, 0) + amount

    categories = list(category_totals.keys())
    totals = list(category_totals.values())

    plt.bar(categories, totals, color='skyblue')
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def load_expenses():
    expenses = []
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    description, amount, category = parts
                    expenses.append((description, float(amount), category))
    return expenses

def filter_by_category(expenses):
    category = input("Enter category to filter: ").strip()
    filtered = [exp for exp in expenses if exp[2].lower() == category.lower()]

    if not filtered:
        print(f"No transactions found for category '{category}'.")
        return

    print(f"\nTransactions in category '{category}':")
    for desc, AMT, cat in filtered:
        print(f"{desc} | ${AMT:.2f} | {cat}")

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
    print("5. Filter by category")
    print("6. Export to CSV")
    print("7. Show category chart")
    print("8. Exit")

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


def export_to_csv():
    pass


def main():
    expenses = load_expenses()
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ")

        if choice == '1':
            add_transaction(expenses, is_income=False)
        elif choice == '2':
            add_transaction(expenses, is_income=True)
        elif choice == '3':
            view_balance(expenses)
        elif choice == '4':
            view_transactions(expenses)
        elif choice == '5':
            filter_by_category(expenses)
        elif choice == '6':
            export_to_csv()
        elif choice == '7':
            show_category_chart(expenses)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()