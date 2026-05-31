import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt  # ✅ Import upar aa gaya
 
from database.db import (
    create_table,
    add_expense,
    view_expenses,
    delete_expense,
    search_expenses
)
 
create_table()
 
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("1200x700")
root.resizable(False, False)
 
# =========================
# FUNCTIONS
# =========================
 
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
 
    expenses = view_expenses()
 
    for expense in expenses:
        tree.insert("", tk.END, values=expense)
 
 
def add_expense_gui():
    try:
        title = title_entry.get()
        amount = float(amount_entry.get())
        category = category_entry.get()
        date = date_entry.get()
 
        add_expense(
            title,
            amount,
            category,
            date
        )
 
        clear_fields()
        refresh_table()
 
        messagebox.showinfo(
            "Success",
            "Expense Added Successfully!"
        )
 
    except ValueError:
        messagebox.showerror(
            "Error",
            "Amount must be a number!"
        )
 
 
def clear_fields():
    title_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
 
 
def delete_selected():
    selected = tree.selection()
 
    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select an expense first!"
        )
        return
 
    values = tree.item(selected[0])["values"]
 
    expense_id = values[0]
 
    delete_expense(expense_id)
 
    refresh_table()
 
    messagebox.showinfo(
        "Deleted",
        "Expense Deleted Successfully!"
    )
 
 
def search_gui():
    keyword = search_entry.get()
 
    for row in tree.get_children():
        tree.delete(row)
 
    results = search_expenses(keyword)
 
    for expense in results:
        tree.insert("", tk.END, values=expense)
 
 
# ✅ show_chart ab buttons se PEHLE define hai — error fix!
def show_chart():
    expenses = view_expenses()
 
    if not expenses:
        messagebox.showinfo(
            "No Data",
            "Koi expense nahi mila chart ke liye!"
        )
        return
 
    categories = {}
 
    for expense in expenses:
        category = expense[3]
        amount = expense[2]
 
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
 
    plt.figure(figsize=(7, 7))
 
    plt.pie(
        categories.values(),
        labels=categories.keys(),
        autopct="%1.1f%%",
        startangle=140
    )
 
    plt.title("Expense Distribution by Category")
    plt.tight_layout()
    plt.show()
 
 
# =========================
# HEADING
# =========================
 
heading = tk.Label(
    root,
    text="Expense Tracker",
    font=("Segoe UI", 26, "bold")
)
 
heading.pack(pady=10)
 
# =========================
# FORM
# =========================
 
form_frame = tk.Frame(root)
form_frame.pack(pady=10)
 
tk.Label(
    form_frame,
    text="Title"
).grid(row=0, column=0, padx=10)
 
title_entry = tk.Entry(
    form_frame,
    width=25
)
title_entry.grid(row=0, column=1)
 
tk.Label(
    form_frame,
    text="Amount"
).grid(row=1, column=0)
 
amount_entry = tk.Entry(
    form_frame,
    width=25
)
amount_entry.grid(row=1, column=1)
 
tk.Label(
    form_frame,
    text="Category"
).grid(row=2, column=0)
 
category_entry = tk.Entry(
    form_frame,
    width=25
)
category_entry.grid(row=2, column=1)
 
tk.Label(
    form_frame,
    text="Date"
).grid(row=3, column=0)
 
date_entry = tk.Entry(
    form_frame,
    width=25
)
date_entry.grid(row=3, column=1)
 
# =========================
# BUTTONS
# =========================
 
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
 
tk.Button(
    button_frame,
    text="Add Expense",
    command=add_expense_gui
).grid(row=0, column=0, padx=5)
 
tk.Button(
    button_frame,
    text="Delete Selected",
    command=delete_selected
).grid(row=0, column=1, padx=5)
 
tk.Button(
    button_frame,
    text="Refresh",
    command=refresh_table
).grid(row=0, column=2, padx=5)
 
# ✅ Show Chart button — ab show_chart defined hai toh error nahi aayega
tk.Button(
    button_frame,
    text="Show Chart",
    command=show_chart
).grid(row=0, column=3, padx=5)
 
# =========================
# SEARCH
# =========================
 
search_frame = tk.Frame(root)
search_frame.pack(pady=10)
 
search_entry = tk.Entry(
    search_frame,
    width=40
)
 
search_entry.grid(
    row=0,
    column=0,
    padx=10
)
 
tk.Button(
    search_frame,
    text="Search",
    command=search_gui
).grid(row=0, column=1)
 
# =========================
# TABLE
# =========================
 
columns = (
    "ID",
    "Title",
    "Amount",
    "Category",
    "Date"
)
 
tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=15
)
 
for col in columns:
    tree.heading(col, text=col)
 
tree.column("ID", width=70)
tree.column("Title", width=250)
tree.column("Amount", width=150)
tree.column("Category", width=200)
tree.column("Date", width=150)
 
tree.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)
 
refresh_table()
 
root.mainloop()
 