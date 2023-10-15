"""
*******************************************************************************************
Program: PokhrelbashuFinalProject.py
Author: Bashu Pokhrel
Date created: 09/11/2023
Last Modified: 10/15/2023

The purpose of this application is to ask user to enter their monthly gross income. There are different expenses category listed in the drop-down.
User will select each category and enter the amount for the selected category. Once all the data is entered correctly, it will calculate the income after tax and
monthly savings. The application will also display the pie chart with different expenses category.


*******************************************************************************************
"""
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox

# Function to calculate net income, expenses, and savings
def calculate():
    try:
        income = float(income_entry.get())
        total_expenses = sum(expenses_dict.values())
        net_income = income - (income * 0.2)
        savings = net_income - total_expenses

        # Displaying the results for income and savings.
        net_income_label.config(text=f"Net Income is the income after tax. \nIn this application, tax is assumed to be 20% . \nYour Income After Tax: ${net_income:.2f}",bg="#A2CD5A",width=40, height=3, font=("Arial",15))
        savings_label.config(text=f"Your Savings for this Month: ${savings:.2f}", bg="#6495ED",width=35, height=2, font=("Arial",15))

        # Updating the pie chart and legend. They have different colors
        draw_pie_chart()
        update_legend()

    except ValueError:
        messagebox.showerror("Error: No Entries")

# Function to add expense category and amount to the expenses dictionary
def add_expense():
    try:
        category = category_var.get()
        amount = float(expense_entry.get())

        # Check if the category already exists in expenses_dict
        if category in expenses_dict:
            # Subtract the previous amount associated with that category
            total_expenses = sum(expenses_dict.values()) - expenses_dict[category]
            # Add the new amount
            expenses_dict[category] = amount
        else:
            expenses_dict[category] = amount

        # Update the list of expenses
        update_expense_list()

        # Clear the entry fields
        category_var.set("")  # Clearing the category dropdown selection after the first entry
        expense_entry.delete(0, tk.END)  # Clearing the expense entry field inorder to enter the another expense.

    except ValueError:
        messagebox.showerror("Error: Looks like you are clicking too fast.")

# Function to update the list of expenses
def update_expense_list():
    expenses_listbox.delete(0, tk.END)
    for category, amount in expenses_dict.items():
        expenses_listbox.insert(tk.END, f"{category}: ${amount:.2f}")

# Function to draw a pie chart on the canvas with different colors for each category
def draw_pie_chart():
    canvas.delete("all")
    start_angle = 0

    total = sum(expenses_dict.values())

    # colors for each category of expense
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd","#6495ED"]

    for category, amount in expenses_dict.items():
        portion = amount / total
        extent_angle = 360 * portion
        color_idx = list(expenses_dict.keys()).index(category) % len(colors)
        color = colors[color_idx]

        # Calculate the coordinates for the text label
        mid_angle = start_angle + extent_angle / 2
        label_x = 150 + 100 * 0.8 * (mid_angle * 3.141592653589793 / 180)
        label_y = 150 - 100 * 0.8 * (mid_angle * 3.141592653589793 / 180)

        canvas.create_arc(50, 50, 250, 250, start=start_angle, extent=extent_angle, fill=color, tags=category)
        canvas.create_text(label_x, label_y, text=category, anchor=tk.CENTER, font=("Arial", 8, "bold"))

        start_angle += extent_angle

# Function to update the legend with category names and colors
def update_legend():
    legend.delete("all")
    y_position = 20

    # color code for legend items. The name of expense will be displayed
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd","#6495ED"]

    for category, color in zip(expenses_dict.keys(), colors):
        legend.create_rectangle(10, y_position, 30, y_position + 20, fill=color, outline="")
        legend.create_text(40, y_position + 10, text=category, anchor=tk.W)
        y_position += 30
       

# GUI window setup
import tkinter as tk
window = tk.Tk()
window.geometry("1000x820")
window.config(bg="#7FFFD4")
window.resizable(width=True,height=True)
window.title('Income-Expenses Calculator')


# Right Frame for pie chart and legend
right_frame = tk.Frame(window, width=400, height=300)
right_frame.pack(side=tk.RIGHT, padx=38, pady=18)

# Canvas to draw pie chart
canvas = tk.Canvas(right_frame, width=300, height=300)
canvas.pack()

# Legend canvas to display legend
legend = tk.Canvas(right_frame, width=200, height=200)
legend.pack()

# Asking user to input their monthly gross income
income_label = tk.Label(window, text="Enter Your Monthly Gross Income:",bg="#6495ED",width=37, height=2, font=("Arial",15))
income_label.pack()
income_entry = tk.Entry(window)
income_entry.pack()


# Expense category dropdown
category_var = tk.StringVar()
category_label = tk.Label(window, text="Select Expense Category From the list below:", bg="#6495ED",width=37, height=2, font=("Arial",15))
category_label.pack()
categories = ["Housing", "Education", "Groceries", "Travel", "Utility","Other"]
category_dropdown = tk.OptionMenu(window, category_var, *categories)
category_dropdown.config(width=20,height=2,bg="#EEB422",font=("Arial",10))
category_dropdown.pack()

# Expense amount input
expense_label = tk.Label(window, text="Enter Your Monthly Expense Amount for Above Category:",bg="#6495ED",width=50, height=2, font=("Arial",15))
expense_label.pack()
expense_entry = tk.Entry(window,width=15)
expense_entry.pack()

# Button to add expenses
add_button = tk.Button(window, text="Add Expense", command=add_expense, bg="#FF7F50",font=("Arial",15))
add_button.pack()

# Listbox to display expenses
expenses_listbox = tk.Listbox(window)
expenses_listbox.pack()

# Button to calculate and display results
calculate_button = tk.Button(window, text="Calculate", command=calculate, bg="#FF7F50",font=("Arial",15))
calculate_button.pack()

# Labels to display net income and savings
net_income_label = tk.Label(window, text="")
net_income_label.pack()
savings_label = tk.Label(window, text="")
savings_label.pack()

# Load the first cat image
load_cat = Image.open("cat.jpg")
render_cat = ImageTk.PhotoImage(load_cat)

# Creating a Label to display the first image
img_label_cat = Label(window, image=render_cat, text="Did you save some $$?", compound='top')
img_label_cat.image = render_cat  # Keep a reference to the image to prevent garbage collection
img_label_cat.pack(side=LEFT)  # Position the first cat image label on the left

# Loading the second image
load_travel = Image.open("travel.jpg")
render_travel = ImageTk.PhotoImage(load_travel)

# Creating a Label to display the second image
img_label_travel = Label(window, image=render_travel, text="I like travelling!", compound='top')
img_label_travel.image = render_travel  # Keep a reference to the image to prevent garbage collection
img_label_travel.pack(side=RIGHT)  # Position the second cat image label on the right


# Expenses dictionary to store category-wise expenses
expenses_dict = {}

# Running the Tkinter main loop
window.mainloop()
