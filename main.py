from tabulate import tabulate
import matplotlib.pyplot as plt

from database.db import (
    create_table,
    add_expense,
    view_expenses,
    delete_expense,
    update_expense,
    search_expenses,
    monthly_summary,
    get_chart_data
)


def main():
    create_table()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Edit Expense")
        print("5. Search Expenses")
        print("6. Monthly Summary")
        print("7. Show Pie Chart")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                title = input("Enter Expense Title: ")
                amount = float(input("Enter Amount: "))
                category = input("Enter Category: ")
                date = input("Enter Date (YYYY-MM-DD): ")

                add_expense(title, amount, category, date)

                print("Expense Added Successfully!")

            except ValueError:
                print("Please enter a valid amount!")

        elif choice == "2":
            expenses = view_expenses()

            if expenses:
                headers = [
                    "ID",
                    "Title",
                    "Amount",
                    "Category",
                    "Date"
                ]

                print(
                    tabulate(
                        expenses,
                        headers=headers,
                        tablefmt="grid"
                    )
                )
            else:
                print("No expenses found.")

        elif choice == "3":
            try:
                expense_id = int(
                    input("Enter Expense ID to delete: ")
                )

                delete_expense(expense_id)

                print("Expense Deleted Successfully!")

            except ValueError:
                print("Please enter a valid ID!")

        elif choice == "4":
            try:
                expense_id = int(
                    input("Enter Expense ID to edit: ")
                )

                title = input("Enter New Title: ")
                amount = float(
                    input("Enter New Amount: ")
                )
                category = input(
                    "Enter New Category: "
                )
                date = input(
                    "Enter New Date (YYYY-MM-DD): "
                )

                update_expense(
                    expense_id,
                    title,
                    amount,
                    category,
                    date
                )

                print(
                    "Expense Updated Successfully!"
                )

            except ValueError:
                print("Invalid Input!")

        elif choice == "5":
            keyword = input(
                "Enter title, category or date to search: "
            )

            results = search_expenses(keyword)

            if results:
                headers = [
                    "ID",
                    "Title",
                    "Amount",
                    "Category",
                    "Date"
                ]

                print(
                    tabulate(
                        results,
                        headers=headers,
                        tablefmt="grid"
                    )
                )
            else:
                print("No matching expenses found.")

        elif choice == "6":
            summary = monthly_summary()

            print("\n===== MONTHLY SUMMARY =====")

            total = 0

            for category, amount in summary:
                print(f"{category}: ₹{amount}")
                total += amount

            print(f"\nTotal Expense: ₹{total}")

        elif choice == "7":

            data = get_chart_data()

            if data:
                categories = []
                amounts = []

                for category, amount in data:
                    categories.append(category)
                    amounts.append(amount)

                plt.figure(figsize=(7, 7))

                plt.pie(
                    amounts,
                    labels=categories,
                    autopct="%1.1f%%"
                )

                plt.title("Expense Distribution")
                plt.show()

            else:
                print("No expense data available.")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()