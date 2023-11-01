#
# API Connector
#
# Pozzuoli, Antony
# CSCI 333 Group Project
# 09/25/2023
#
# This program takes the ticket class from gui and sends it to the sql database
#

from gui import GUI
import mysql.connector

def __main__():
    guiFrame = GUI()
    guiFrame.mainloop()

    cnx = mysql.connector.connect(user='scott', password='password',
                              host='127.0.0.1',
                              database='employees')
    cursor = cnx.cursor()
    
    cnx.close()


    print("Employee Name:", guiFrame.ticket.emp_name)
    print("Employee Number:", guiFrame.ticket.emp_num)
    print("Department:", guiFrame.ticket.department)
    print("Platform:", guiFrame.ticket.platform)
    print("Software:", guiFrame.ticket.soft_name)
    print("Error Type:", guiFrame.ticket.error_type)
    print("Impact:", guiFrame.ticket.impact)
    print("Date & Time:", guiFrame.ticket.date_time)
    print("Email:", guiFrame.ticket.email)
    print("Phone Number:", guiFrame.ticket.phone_num)
    print("Description:", guiFrame.ticket.description)

__main__()