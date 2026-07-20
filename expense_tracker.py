import csv
import os

from expense import Expense
from utils import *


class ExpenseTracker:

    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.load_data()

    def load_data(self):
        self.expenses.clear()

        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            next(reader, None)

            for row in reader:
                if row:
                    self.expenses.append(Expense.from_list(row))

    def save_data(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Title",
                "Amount",
                "Category",
                "Date"
            ])

            for expense in self.expenses:
                writer.writerow(expense.to_list())

    def generate_id(self):

        if len(self.expenses) == 0:
            return 101

        return max(e.expense_id for e in self.expenses) + 1

    def add_expense(self):

        print("\nADD NEW EXPENSE\n")

        title = input("Enter Title: ").strip()

        amount = get_valid_float(
            "Enter Amount: "
        )

        category = input(
            "Enter Category: "
        ).strip()

        date = get_valid_date(
            "Enter Date (DD-MM-YYYY) or leave blank: "
        )

        expense = Expense(
            self.generate_id(),
            title,
            amount,
            category,
            date
        )

        self.expenses.append(expense)

        print("\nExpense added successfully.")
        print("Generated ID:", expense.expense_id)
        
    def view_expenses(self):

        if len(self.expenses) == 0:
            print("\nNo expenses found.")
            return

        print_header()

        for expense in self.expenses:
            print_expense(expense)

        print_line()

    def search_expense(self):

        expense_id = get_valid_int(
            "Enter Expense ID: "
        )

        for expense in self.expenses:

            if expense.expense_id == expense_id:

                print_header()
                print_expense(expense)
                print_line()

                return expense

        print("Expense not found.")

        return None
    
    def update_expense(self):

        expense = self.search_expense()

        if expense is None:
            return

        print("\nLeave blank to keep old value.\n")

        title = input(
            "New Title: "
        ).strip()

        if title:
            expense.title = title

        amount = input(
            "New Amount: "
        ).strip()

        if amount:

            try:
                expense.amount = float(amount)
            except ValueError:
                print("Invalid amount. Keeping previous value.")

        category = input(
            "New Category: "
        ).strip()

        if category:
            expense.category = category

        date = input(
            "New Date (DD-MM-YYYY): "
        ).strip()

        if date:

            try:
                import datetime

                datetime.datetime.strptime(
                    date,
                    "%d-%m-%Y"
                )

                expense.date = date

            except ValueError:
                print("Invalid date. Keeping previous value.")

        print("\nExpense updated.")
    
    def delete_expense(self):

        expense = self.search_expense()

        if expense is None:
            return

        choice = input(
            "Are you sure you want to delete this expense? (y/n): "
        ).lower()

        if choice == "y":
            self.expenses.remove(expense)
            print("\nExpense deleted successfully.")
        else:
            print("\nDeletion cancelled.")
    
    def view_summary(self):

        if len(self.expenses) == 0:
            print("\nNo expense records found.")
            return

        total = 0
        categories = {}

        for expense in self.expenses:

            total += expense.amount

            if expense.category not in categories:
                categories[expense.category] = 0

            categories[expense.category] += expense.amount

        print("\n" + "=" * 60)
        print("FINANCIAL SUMMARY")
        print("=" * 60)

        print(f"Total Expenses Recorded : {len(self.expenses)}")
        print(f"Grand Total             : {currency(total)}")

        print("\nCategory Wise Breakdown")
        print("-" * 60)

        for category, amount in categories.items():
            print(f"{category:<20}{currency(amount)}")

        print("=" * 60)

    def save_and_exit(self):

        self.save_data()

        print("\nData saved successfully.")
        print("Thank you for using Personal Expense Tracker.")