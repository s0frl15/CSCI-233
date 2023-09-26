import tkinter as tk
import sqlite3
from tkinter import ttk
from datetime import datetime

root = tk.Tk()
root.title("Bug Report Form")

def save_bug_report():
    name = name_entry.get()
    employee_number = employee_number_entry.get()
    department = department_var.get()
    platform = platform_var.get()
    software_name = software_name_entry.get()
    error_type = error_type_var.get()
    impact = impact_var.get()
    date_time = date_time_entry.get()
    email = email_entry.get()
    phone_number = phone_number_entry.get()
    description = description_entry.get()

    connect = sqlite3.connect('bug_report.db')
    cursor = connect.cursor()

    cursor.execute('''
        INSERT INTO bug_report (name, employee_number, department, platform, software_name, error_type, impact, date_time, email, phone_number, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, employee_number, department, platform, software_name, error_type, impact, date_time, email, phone_number, description))

    connect.commit()
    connect.close()

    name_entry.delete(0, tk.END)
    employee_number_entry.delete(0, tk.END)
    software_name_entry.delete(0, tk.END)
    date_time_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

    print("Report submitted successfully")

#name box
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

#employee number box
employee_number_label = tk.Label(root, text="Employee Number:")
employee_number_label.pack()
employee_number_entry = tk.Entry(root)
employee_number_entry.pack()

#department
department_label = tk.Label(root, text="Department:")
department_label.pack()
department_var = tk.StringVar()
department_dropdown = ttk.Combobox(root, textvariable=department_var, values=["Accounting", "Human Resources", "Procurement", "Development", "Sales", "IT", "Logistics", "Legal"])
department_dropdown.pack()

#platform dropdown
platform_label = tk.Label(root, text="Platform:")
platform_label.pack()
platform_var = tk.StringVar()
platform_dropdown = ttk.Combobox(root, textvariable=platform_var, values=["Windows", "macOS", "Linux"])
platform_dropdown.pack()

#software box
software_name_label = tk.Label(root, text="Software Name:")
software_name_label.pack()
software_name_entry = tk.Entry(root)
software_name_entry.pack()

#error type dropdown
error_type_label = tk.Label(root, text="Error Type:")
error_type_label.pack()
error_type_var = tk.StringVar()
error_type_dropdown = ttk.Combobox(root, textvariable=error_type_var, values=["Crash", "Performance", "UI Issue", "Other (specify in description)"])
error_type_dropdown.pack()

#impact dropdown
impact_label = tk.Label(root, text="Impact:")
impact_label.pack()
impact_var = tk.StringVar
impact_dropdown = ttk.Combobox(root, textvariable=impact_var, values=["Customer", "Developer", "Individual"])
impact_dropdown.pack()

#date & time entry
date_time_label = tk.Label(root, text="Date and Time of Error Occurence:")
date_time_label.pack()
date_time_entry = tk.Entry(root)
date_time_entry.insert(0, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
date_time_entry.pack()

#email box
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

#phone number box
phone_number_label = tk.Label(root, text="Phone Number:")
phone_number_label.pack()
phone_number_entry = tk.Entry(root)
phone_number_entry.pack()

#description box
description_label = tk.Label(root, text="Description:")
description_label.pack()
description_entry = tk.Entry(root)
description_entry.pack()

root.mainloop()