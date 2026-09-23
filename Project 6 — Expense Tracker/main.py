expenses = []

while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        print("Expense added successfully! ✅")

    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            print("\nYour Expenses:")

            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense['name']} - "
                    f"₹{expense['amount']} - "
                    f"{expense['category']}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)

        print(f"Total Expense: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Expense Tracker! 👋")
        break

    else:
        print("Invalid choice!")