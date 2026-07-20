import datetime


def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("[ERROR] Please enter a valid integer.")


def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("[ERROR] Amount cannot be negative.")
                continue
            return value
        except ValueError:
            print("[ERROR] Please enter a valid amount.")


def get_valid_date(prompt):
    while True:
        date = input(prompt).strip()

        if date == "":
            today = datetime.datetime.now().strftime("%d-%m-%Y")
            print(f"[SYSTEM] Auto assigned today's date: {today}")
            return today

        try:
            datetime.datetime.strptime(date, "%d-%m-%Y")
            return date
        except ValueError:
            print("[ERROR] Invalid date. Use DD-MM-YYYY.")


def print_line():
    print("-" * 90)


def print_header():
    print_line()
    print(f"{'ID':<8}{'TITLE':<25}{'AMOUNT':<12}{'CATEGORY':<20}{'DATE':<15}")
    print_line()


def print_expense(expense):
    print(
        f"{expense.expense_id:<8}"
        f"{expense.title:<25}"
        f"{expense.amount:<12.2f}"
        f"{expense.category:<20}"
        f"{expense.date:<15}"
    )


def currency(value):
    return f"₹{value:.2f}"