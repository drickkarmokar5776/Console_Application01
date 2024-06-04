import json
import os

# Define the file path for data storage
DATA_FILE = 'budget_data.json'

# Check if data file exists, if not, create one
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump({'income': [], 'expenses': []}, file)

def load_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_income(data):
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    data['income'].append({'category': category, 'amount': amount})
    save_data(data)
    print("Income added successfully!")

def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': amount})
    save_data(data)
    print("Expense added successfully!")

def calculate_budget(data):
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    remaining_budget = total_income - total_expenses
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Remaining Budget: ${remaining_budget}")

def expense_analysis(data):
    expenses_by_category = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in expenses_by_category:
            expenses_by_category[category] += amount
        else:
            expenses_by_category[category] = amount
    
    print("Expense Analysis:")
    for category, total in expenses_by_category.items():
        print(f"Category: {category}, Total Spent: ${total}")

def main():
    data = load_data()
    
    while True:
        print("\nBudget Tracker Menu")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            calculate_budget(data)
        elif choice == '4':
            expense_analysis(data)
        elif choice == '5':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
