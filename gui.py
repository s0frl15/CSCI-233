from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime
from ticketclass import Ticket

class GUI(Frame):
    def __init__(self,master=None):
        self.ticket = Ticket()

        Frame.__init__(self, master)
        self.grid()

        self.nameLabel = Label(master, text="Name")
        self.nameLabel.grid()
        self.nameEntry = Entry(master)
        self.nameEntry.grid()

        self.empNumLabel = Label(master, text="Employee Number")
        self.empNumLabel.grid()
        self.empNumEntry = Entry(master)
        self.empNumEntry.grid()

        self.departmentLabel = Label(master, text="Department")
        self.departmentLabel.grid()
        self.departmentEntry = StringVar()
        self.departmentDropdown = Combobox(master, textvariable=self.departmentEntry, values=["Accounting", "Human Resources", "Procurement", "Development", "Sales", "IT", "Logistics", "Legal"])
        self.departmentDropdown.grid()

        self.platformLabel = Label(master, text="Platform")
        self.platformLabel.grid()
        self.platformEntry = StringVar()
        self.platformDropdown = Combobox(master, textvariable=self.platformEntry, values=["Windows", "macOS", "Linux"])
        self.platformDropdown.grid()

        self.softwareLabel = Label(master, text="Software")
        self.softwareLabel.grid()
        self.softwareEntry = Entry(master)
        self.softwareEntry.grid()

        self.errorTypeLabel = Label(master, text="Error Type")
        self.errorTypeLabel.grid()
        self.errorTypeEntry = StringVar()
        self.errorTypeDropdown = Combobox(master, textvariable=self.errorTypeEntry, values=["Crash", "Performance", "UI Issue", "Other (specify in description)"])
        self.errorTypeDropdown.grid()

        self.impactLabel = Label(master, text="Impact")
        self.impactLabel.grid()
        self.impactEntry = StringVar()
        self.impactDropdown = Combobox(master, textvariable=self.impactEntry, values=["Customer", "Developer", "Individual"])
        self.impactDropdown.grid()

        self.dateTimeLabel = Label(master, text="Date & Time")
        self.dateTimeLabel.grid()
        self.dateTimeEntry = Entry(master)
        self.dateTimeEntry.insert(0, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.dateTimeEntry.grid()

        self.emailLabel = Label(master, text="Email")
        self.emailLabel.grid()
        self.emailEntry = Entry(master)
        self.emailEntry.grid()

        self.phoneLabel = Label(master, text="Phone Number")
        self.phoneLabel.grid()
        self.phoneEntry = Entry(master)
        self.phoneEntry.grid()

        self.descriptionLabel = Label(master, text="Description")
        self.descriptionLabel.grid()
        self.descriptionEntry = Entry(master)
        self.descriptionEntry.grid()

        self.submitButton = Button(master, command=self.buttonClick, text="Submit")
        self.submitButton.grid()


    def buttonClick(self):
        self.ticket.emp_name = self.nameEntry.get()
        self.ticket.emp_num = self.empNumEntry.get()
        self.ticket.department = self.departmentEntry.get()
        self.ticket.platform = self.platformEntry.get()
        self.ticket.soft_name = self.softwareEntry.get()
        self.ticket.error_type = self.errorTypeEntry.get()
        self.ticket.impact = self.impactEntry.get()
        self.ticket.date_time = self.dateTimeEntry.get()
        self.ticket.email = self.emailEntry.get()
        self.ticket.phone_num = self.phoneEntry.get()
    
# Uncomment this and implement a main function in this file if you want to test just this class
# if __name__ == "__main__":
#     guiFrame = GUI()
#     guiFrame.mainloop()

