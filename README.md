# Budget Tracker

Welcome to the Budget Tracker! This Python project provides a simple budget tracker that allows users to manage income, expenses, and calculate their balance.

## How to Use

1. Run the script (`budget_tracker.py`).
2. Enter your name when prompted.
3. Add income and expenses to track your budget.
4. The script will calculate and display your current balance.

## Features

### `BudgetTracker` Class

- Manages user details and budget data.
- Provides methods to add income, add expenses, calculate balance, save to file, and load from file.

### Methods

### `add_income(amount, description)`

- Records details for income entries.

### `add_expense(amount, category, description)`

- Records details for expense entries.

### `calculate_balance()`

- Calculates the balance by subtracting total expenses from total income.

### `save_to_file(file_path)`

- Saves budget data to a JSON file.

### `load_from_file(file_path)`

- Loads budget data from a JSON file.

## Example Usage

```python
# Example usage
user_name = input("Enter your name: ")
budget_tracker = BudgetTracker(user_name)

# Add income and expenses
budget_tracker.add_income(2000, 'Salary')
budget_tracker.add_expense(500, 'Groceries', 'Weekly shopping')
budget_tracker.add_expense(200, 'Utilities', 'Electricity bill')

# Calculate and display the balance
balance = budget_tracker.calculate_balance()
print(f"Current Balance: ${balance}")

# Save and load budget data to/from a file
file_path = 'budget_data.json'
budget_tracker.save_to_file(file_path)

# Create a new BudgetTracker instance and load data from the file
new_budget_tracker = BudgetTracker(user_name)
new_budget_tracker.load_from_file(file_path)

# Display the loaded budget data
print("\\nBudget Data loaded from file:")
print(f"User Name: {new_budget_tracker.user_name}")
print("Income Entries:")
print(new_budget_tracker.budget['income'])
print("Expense Entries:")
print(new_budget_tracker.budget['expenses'])

```

## Additional Considerations

- **Data Persistence:**
    - Ensure that the budget data is saved and loaded securely.
- **User Input:**
    - Validate user input for amounts, categories, and descriptions.
- **File Handling:**
    - Handle file operations securely and consider error handling.

## Author

Jeel patel
