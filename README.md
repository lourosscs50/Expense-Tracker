📌 Expense Tracker – CLI Personal Finance Manager

A modular Python command-line expense tracking application that supports persistent storage, transaction filtering, balance computation, category-based aggregation, and optional data visualization.

The application models a simplified personal finance management system designed with extensibility in mind, allowing future integration with databases, APIs, or web interfaces.

⸻

🚀 Overview

Expense Tracker enables users to manage personal financial transactions directly from the command line. Data is stored persistently between sessions, allowing users to track spending habits, analyze categories, and visualize financial trends over time.

The project emphasizes structured program design, modular functions, and analytical data processing.

⸻

✨ Features
	•	Record income and expenses
	•	Persistent transaction storage
	•	Dynamic account balance calculation
	•	Filter transactions by category
	•	Aggregate spending by category
	•	Command-line interactive menu
	•	Bar chart visualization of category spending
	•	Modular architecture for future expansion
	•	CSV export support (planned feature)

⸻

🧱 Tech Stack
	•	Language: Python
	•	Libraries Used:
	•	Standard Python libraries
	•	File I/O operations
	•	Data processing logic
	•	Matplotlib (for visualization, if used)

🏗️ Application Flow
Program Start
    ↓
Load existing transactions
    ↓
Display interactive menu
    ↓
User action
    ↓
Update application state
    ↓
Persist data to file
    ↓
Repeat until exit

🧠 Architecture
The application follows a modular CLI structure:
main()
├── load_expenses()
├── show_menu()
├── add_transaction()
├── view_balance()
├── view_transactions()
├── filter_by_category()
├── export_to_csv()   # planned
└── show_category_chart()

Design Principles
	•	Separation of concerns
	•	Maintainable function structure
	•	Persistent state management
	•	Extendable architecture

⸻

🗄️ Data Format

Transactions are stored using a simple structured format:
Category|Amount|Type
Example
Groceries|45.90|Food
Gas|30.00|Transport
Freelance|500.00|Income

⚙️ How to Run

1️⃣ Clone Repository
git clone https://github.com/lourosscs50/Expense-Tracker.git
cd Expense-Tracker

2️⃣ Run Application
python expense_tracker.py

📊 Visualization

The application can generate a bar chart showing spending distribution by category, helping users quickly understand financial habits.

(Add screenshot or chart image here for stronger portfolio impact.)

⸻

🎯 Purpose

This project was developed to demonstrate practical Python programming skills through real-world financial data processing. It highlights:
	•	CLI application design
	•	Persistent data handling
	•	Analytical reporting logic
	•	Modular program architecture
	•	Extendable system design

⸻

📈 Skills Demonstrated
	•	Python application development
	•	File persistence
	•	Data transformation & aggregation
	•	CLI interface design
	•	Financial computation logic
	•	Visualization concepts
	•	Modular software structure

⸻

🔮 Future Improvements
	•	Database integration (SQLite/PostgreSQL)
	•	Web interface (Flask/Django)
	•	User authentication
	•	CSV export functionality
	•	REST API integration

⸻

👨‍💻 Author

Lou Carron
Software Developer | Python | .NET | Backend Systems

GitHub: https://github.com/lourosscs50
LinkedIn: https://www.linkedin.com/in/lou-carron-2b2652123?trk=contact-info

📄 License

This project is intended for educational and portfolio demonstration purposes.
