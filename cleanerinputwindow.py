import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

root = tk.Tk()
root.title("Bug Report Form")

#save bug report
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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

#default date and time
def set_default_date_time():
    date_time_entry.delete(0, tk.END)
    date_time_entry.insert(0, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

#name box
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

#employee number box
employee_number_label = tk.Label(root, text="Employee Number:")
employee_number_label.grid(row=1, column=0, sticky="w")
employee_number_entry = tk.Entry(root)
employee_number_entry.grid(row=1, column=1)

#department dropdown
department_label = tk.Label(root, text="Department:")
department_label.grid(row=2, column=0, sticky="w")
department_var = tk.StringVar()
department_dropdown = ttk.Combobox(root, textvariable=department_var, values=["Accounting", "Human Resources", "Procurement", "Development", "Sales", "IT", "Logistics", "Legal"])
department_dropdown.grid(row=2, column=1)

#platform dropdown
platform_label = tk.Label(root, text="Platform:")
platform_label.grid(row=3, column=0, sticky="w")
platform_var = tk.StringVar()
platform_dropdown = ttk.Combobox(root, textvariable=platform_var, values=["Windows", "macOS", "Linux"])
platform_dropdown.grid(row=3, column=1)

#software box
software_name_label = tk.Label(root, text="Software Name:")
software_name_label.grid(row=4, column=0, sticky="w")
software_name_entry = tk.Entry(root)
software_name_entry.grid(row=4, column=1)

#error type dropdown
error_type_label = tk.Label(root, text="Error Type:")
error_type_label.grid(row=5, column=0, sticky="w")
error_type_var = tk.StringVar()
error_type_dropdown = ttk.Combobox(root, textvariable=error_type_var, values=["Crash", "Performance", "UI Issue", "Other (specify in description)"])
error_type_dropdown.grid(row=5, column=1)

#impact dropdown
impact_label = tk.Label(root, text="Impact:")
impact_label.grid(row=6, column=0, sticky="w")
impact_var = tk.StringVar()
impact_dropdown = ttk.Combobox(root, textvariable=impact_var, values=["Customer", "Developer", "Individual"])
impact_dropdown.grid(row=6, column=1)

#date & time entry
date_time_label = tk.Label(root, text="Date and Time of Error Occurrence:")
date_time_label.grid(row=7, column=0, sticky="w")
date_time_entry = tk.Entry(root)
date_time_entry.grid(row=7, column=1)
set_default_date_time() 

#email box
email_label = tk.Label(root, text="Email:")
email_label.grid(row=8, column=0, sticky="w")
email_entry = tk.Entry(root)
email_entry.grid(row=8, column=1)

#phone number box
phone_number_label = tk.Label(root, text="Phone Number:")
phone_number_label.grid(row=9, column=0, sticky="w")
phone_number_entry = tk.Entry(root)
phone_number_entry.grid(row=9, column=1)

#description box
description_label = tk.Label(root, text="Description:")
description_label.grid(row=10, column=0, sticky="w")
description_entry = tk.Entry(root)
description_entry.grid(row=10, column=1)

#save button
save_button = tk.Button(root, text="Submit Report", command=save_bug_report)
save_button.grid(row=11, column=0, columnspan=2)

root.mainloop()
