# 💰 Expense Tracker Application

## Overview

Expense Tracker is a Python-based application designed to help users manage and monitor their daily expenses efficiently. The application allows users to add, view, update, delete, and search expense records while maintaining all data in a database. It also provides expense analysis through monthly summaries and graphical charts for better financial insights.

The project includes both a Command Line Interface (CLI) and a Graphical User Interface (GUI), making it suitable for beginners as well as users who prefer a visual experience.

---

## Features

### Expense Management

* Add new expenses
* View all expenses
* Update existing expenses
* Delete expenses
* Search expenses by title, category, or date

### Data Storage

* Stores expense records in a database
* Persistent data management
* Automatic table creation

### Expense Analysis

* Monthly expense summary
* Category-wise expense tracking
* Pie chart visualization of spending patterns

### User Interface

* Interactive GUI built using Tkinter
* Tabular display using Treeview
* Command Line Interface (CLI) support
* Easy-to-use search functionality

---

## Technologies Used

* Python
* Tkinter
* SQLite Database
* Matplotlib
* Tabulate

---

## Modules and Libraries

### Tkinter

Used for creating the graphical user interface.

### SQLite

Used to store expense records permanently.

### Matplotlib

Used to generate pie charts for expense analysis.

### Tabulate

Used in CLI mode to display data in table format.

---

## Project Structure

```text
Expense Tracker
│
├── database/
│   └── db.py
│
├── gui.py
│
├── main.py
│
└── expense_tracker.db
```

### Database Module

Handles all database operations:

* Create Table
* Insert Records
* Update Records
* Delete Records
* Search Records
* Generate Monthly Summary

### GUI Module

Provides a desktop application where users can:

* Add expenses
* Delete expenses
* Search expenses
* View expenses
* Generate expense charts

### CLI Module

Provides terminal-based interaction for users who prefer command-line operations.

---

## How It Works

### Step 1: Add Expense

User enters:

* Expense Title
* Amount
* Category
* Date

The data is stored in the database.

### Step 2: View Expenses

All expense records are fetched and displayed in a table.

### Step 3: Search Expenses

Users can search expenses based on:

* Title
* Category
* Date

### Step 4: Edit Expense

Existing expense records can be modified.

### Step 5: Delete Expense

Selected records can be removed permanently.

### Step 6: Analyze Expenses

The application calculates category-wise expenses and displays them as a pie chart.

---

## Requirements

Install the required packages:

```bash
pip install matplotlib
pip install tabulate
```

Tkinter and SQLite are included with most Python installations.

---

## Running the GUI Version

Save the GUI file and run:

```bash
python gui.py
```

Features available in GUI:

* Add Expense
* Delete Expense
* Search Expense
* Refresh Records
* View Pie Chart

---

## Running the CLI Version

Run:

```bash
python main.py
```

Menu Options:

```text
1. Add Expense
2. View Expenses
3. Delete Expense
4. Edit Expense
5. Search Expenses
6. Monthly Summary
7. Show Pie Chart
8. Exit
```

---

## Sample Expense Record

| Title        | Amount | Category      | Date       |
| ------------ | ------ | ------------- | ---------- |
| Food         | 250    | Food          | 2026-06-20 |
| Bus Fare     | 50     | Transport     | 2026-06-20 |
| Movie Ticket | 300    | Entertainment | 2026-06-21 |

---

## Monthly Summary Feature

The application calculates:

* Total spending
* Category-wise spending
* Monthly expense distribution

Example:

```text
Food: ₹2500
Transport: ₹1200
Entertainment: ₹1800

Total Expense: ₹5500
```

---

## Pie Chart Visualization

The application generates a pie chart showing:

* Food Expenses
* Transport Expenses
* Entertainment Expenses
* Shopping Expenses
* Other Expenses

This helps users understand where most of their money is being spent.

---

## Learning Outcomes

Through this project, students can learn:

* Python Programming
* Database Management with SQLite
* CRUD Operations
* GUI Development using Tkinter
* Data Visualization using Matplotlib
* Modular Programming
* Search and Filtering Techniques
* Financial Data Management

---

## Future Enhancements

### User Authentication

Allow multiple users with separate accounts.

### Budget Planning

Set monthly spending limits.

### Export Reports

Export expenses to PDF or Excel.

### Expense Categories

Predefined category selection through dropdown menus.

### Dark Mode

Modern UI with light and dark themes.

### Cloud Synchronization

Store data online and access it from multiple devices.

### Dashboard Analytics

Advanced charts and financial insights.

---

## Conclusion

The Expense Tracker Application is a complete personal finance management system developed using Python. It combines database management, graphical user interfaces, and data visualization techniques to help users record, organize, and analyze their expenses effectively. The project is an excellent example of integrating multiple Python technologies into a practical real-world application.
