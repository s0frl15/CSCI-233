#
# Ticket Class
#
# Pozzuoli, Antony
# CSCI 333 Group Project
# 09/25/2023
#

from gui import GUI
import mysql.connector

class Ticket:
    # Constructor that defaults all variables as an empty string
    def __init__(self, emp_name = "", emp_num = "123", department = "", platform = "", soft_name = "", error_type = "", impact = "", date_time = "", email = "", phone_num = "", description = ""):
        # Creates class variables and sets them equal to their default values
        self.emp_name = emp_name
        self.emp_num = emp_num
        self.department = department
        self.platform = platform
        self.soft_name = soft_name
        self.error_type = error_type
        self.impact = impact
        self.date_time = date_time
        self.email = email
        self.phone_num = phone_num
        self.description = description
        # No getters/setters required!

    def runGui(self):
        guiFrame = GUI()
        guiFrame.mainloop()

        self.emp_name = guiFrame.emp_name
        self.emp_num = guiFrame.emp_num
        self.department = guiFrame.department
        self.platform = guiFrame.platform
        self.soft_name = guiFrame.soft_name
        self.error_type = guiFrame.error_type
        self.impact = guiFrame.impact
        self.date_time = guiFrame.date_time
        self.email = guiFrame.email
        self.phone_num = guiFrame.phone_num

    # This function currently needs to be changed so that it works
    def sendToDatabase(self):
        cnx = mysql.connector.connect(user="root", password="bandana",
                              host="localhost",
                              database="bug_collector")
        cursor = cnx.cursor()

        cursor.execute("INSERT INTO bug_collector.report (agent_emp_num, emp_num, platform, software_name, error_type, impact, time_stamp, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (self.emp_num, "", self.platform, self.soft_name, self.error_type, self.impact, self.date_time, self.description))
        cnx.commit()

        cursor.close()
        cnx.close()

    # Opens database and saves data into ticket variables
    def receiveFromDatabase(self):
        print("Ticket variables copied from database")


# How to implement this:
# 1. import this file using <from ticketclass import Ticket>

# 2. Create a new ticket object:
# ticket = Ticket()

# 3. Call functions as needed:
# ticket.runGUI()
# ticket.sendToDatabase()