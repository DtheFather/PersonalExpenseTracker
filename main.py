from expense_tracker import ExpenseTracker


def display_menu():
    print("\n" + "=" * 60)
    print("        PERSONAL EXPENSE TRACKER")
    print("=" * 60)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. View Summary")
    print("7. Exit")
    print("=" * 60)


def main():

    tracker = ExpenseTracker()

    while True:

        display_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.search_expense()

        elif choice == "4":
            tracker.update_expense()

        elif choice == "5":
            tracker.delete_expense()

        elif choice == "6":
            tracker.view_summary()

        elif choice == "7":
            tracker.save_and_exit()
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()