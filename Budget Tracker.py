import os
import json
import datetime

class BudgetTracker:
    def __init__(self, user_name):
        # Initialize the budget with user details
        self.user_name = user_name
        self.budget = {
            'income': [],
            'expenses': []
        }

    def add_income(self, amount, description):
        # Record income details
        income_entry = {
            'amount': amount,
            'description': description,
            'date': str(datetime.date.today())
        }
        self.budget['income'].append(income_entry)

    def add_expense(self, amount, category, description):
        # Record expense details
        expense_entry = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': str(datetime.date.today())
        }
        self.budget['expenses'].append(expense_entry)

    def calculate_balance(self):
        # Calculate the balance by subtracting total expenses from total income
        total_income = sum(entry['amount'] for entry in self.budget['income'])
        total_expenses = sum(entry['amount'] for entry in self.budget['expenses'])
        balance = total_income - total_expenses
        return balance

    def save_to_file(self, file_path):
        # Save budget data to a JSON file
        with open(file_path, 'w') as file:
            json.dump({'user_name': self.user_name, 'budget': self.budget}, file)

    def load_from_file(self, file_path):
        # Load budget data from a JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.user_name = data['user_name']
            self.budget = data['budget']

if __name__ == '__main__':
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
    print("\nBudget Data loaded from file:")
    print(f"User Name: {new_budget_tracker.user_name}")
    print("Income Entries:")
    print(new_budget_tracker.budget['income'])
    print("Expense Entries:")
    print(new_budget_tracker.budget['expenses'])
