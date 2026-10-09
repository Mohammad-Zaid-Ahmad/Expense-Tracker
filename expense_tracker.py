
# Expense Tracker
import json


# Save expenses to JSON
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


# Load expenses from JSON
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Add expense
def add_expense(expenses):
    print("\n" + "-" * 35)
    print("ADD EXPENSE".center(35))
    print("-" * 35)

    expense_category = input("Category: ").strip()
    while not expense_category or expense_category.isdigit():
        print("Invalid input. Please enter a valid category.")
        expense_category = input("Category: ").strip()

    expense_description = input("Description: ").strip()
    while not expense_description or expense_description.isdigit():
        print("Invalid input. Please enter a valid description.")
        expense_description = input("Description: ").strip()

    while True:
        try:
            expense_amount = float(input("Amount (₹): "))

            if expense_amount <= 0:
                print("Amount must be greater than zero.")
            else:
                break

        except ValueError:
            print("Invalid amount. Please enter a number.")

    expense = {
        "category": expense_category,
        "description": expense_description,
        "amount": expense_amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\n✓ Expense added successfully!")


# View expenses
def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\n" + "=" * 65)
    print("YOUR EXPENSES".center(65))
    print("=" * 65)

    print(
        f"{'No.':<5}"
        f"{'Category':<15}"
        f"{'Description':<25}"
        f"{'Amount':>20}"
    )
    print("-" * 65)

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number:<5}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"{'₹' + format(expense['amount'], '.2f'):>20}"
        )

    print("=" * 65)


# Delete expense
def delete_expense(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return

    view_expenses(expenses)

    while True:
        try:
            delete = int(input("\nEnter expense number to delete: "))

            if 1 <= delete <= len(expenses):
                break

            print("Invalid number. Please select an expense from the list.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    del expenses[delete - 1]
    save_expenses(expenses)

    print("\n✓ Expense deleted successfully!")


# Calculate total
def calculate_total(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\n" + "-" * 35)
    print("EXPENSE SUMMARY".center(35))
    print("-" * 35)
    print(f"{'Total expenses:':<20} ₹{total:.2f}")
    print("-" * 35)


# Display main menu
def display_menu():
    print("\n" + "=" * 35)
    print("EXPENSE TRACKER".center(35))
    print("=" * 35)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Calculate Total")
    print("5. Exit")
    print("-" * 35)


# Load saved expenses
Add_Expense = load_expenses()


# Main menu
while True:
    display_menu()
    choice = input("Select an option (1-5): ").strip()

    if choice == "1":
        add_expense(Add_Expense)

    elif choice == "2":
        view_expenses(Add_Expense)

    elif choice == "3":
        delete_expense(Add_Expense)

    elif choice == "4":
        calculate_total(Add_Expense)

    elif choice == "5":
        print("\nThank you for using Expense Tracker. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 5.")
