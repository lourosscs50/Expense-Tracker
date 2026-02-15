A modular command-line expense tracking application built in Python that supports persistent storage, transaction filtering, balance computation, and category-based aggregation with optional data visualization.

This project demonstrates structured CLI design, file persistence, data transformation, and analytical reporting logic.

The Expense Tracker allows users to:

Record income and expenses

Persist data across sessions

Calculate account balance dynamically

Filter transactions by category

Aggregate spending by category

Visualize category spending via bar chart

This project models a simplified personal finance management system with extendable architecture for database or web integration.


Program Start
      ↓
Load existing transactions
      ↓
Display interactive menu
      ↓
User action
      ↓
State update (if needed)
      ↓
Persist to file
      ↓
Repeat until exit


main()
 ├── load_expenses()
 ├── show_menu()
 ├── add_transaction()
 ├── view_balance()
 ├── view_transactions()
 ├── filter_by_category()
 ├── export_to_csv() [planned]
 └── show_category_chart()

 Example:

Groceries|45.90|Food
Gas|30.00|Transport
Freelance|500.00|Income
