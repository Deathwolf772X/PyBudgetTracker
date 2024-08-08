import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to add an expense
def add_expense(date, amount, category, description):
    new_expense = pd.DataFrame([[date, amount, category, description]], columns=["Date", "Amount", "Category", "Description"])
    try:
        expenses = pd.read_csv('expenses.csv')
        expenses = pd.concat([expenses, new_expense], ignore_index=True)
    except FileNotFoundError:
        expenses = new_expense
    expenses.to_csv('expenses.csv', index=False)
    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    try:
        expenses = pd.read_csv('expenses.csv')
        print(expenses)
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Function to visualize expenses by category
def visualize_expenses():
    try:
        expenses = pd.read_csv('expenses.csv')
        category_sums = expenses.groupby('Category')['Amount'].sum()
        category_sums.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Expenses by Category')
        plt.ylabel('')
        plt.show()
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Main function
def main():
    while True:
        print("\nBudget Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Visualize Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(date, amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            visualize_expenses()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
