from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime

class GUI(Frame):
    def __init__(self,master=None): 
        Frame.__init__(self, master)

        #window
        #master = Tk()
        #master.title("Bug Report Form")
        
        # Grid has many parameters that can be set to format gui, such as row=0, col=1
        self.grid()
        
        # First/Last name box
        self.nameLabel = Label(master, text="Name")
        self.nameLabel.grid(row=0, column=0, sticky="w")
        self.nameEntry = Entry(master)
        self.nameEntry.grid(row=0, column=1)

        # Employee number box
        self.empNumLabel = Label(master, text="Employee Number")
        self.empNumLabel.grid(row=1, column=0, sticky="w")
        self.empNumEntry = Entry(master)
        self.empNumEntry.grid(row=1, column=1)

        # Department box
        self.departmentLabel = Label(master, text="Department")
        self.departmentLabel.grid(row=2, column=0, sticky="w")
        self.departmentEntry = StringVar()
        self.departmentDropdown = Combobox(master, textvariable=self.departmentEntry, values=["Accounting", "Human Resources", "Procurement", "Development", "Sales", "IT", "Logistics", "Legal"])
        self.departmentDropdown.grid(row=2, column=1)

        # Platform box
        self.platformLabel = Label(master, text="Platform")
        self.platformLabel.grid(row=3, column=0, sticky="w")
        self.platformEntry = StringVar()
        self.platformDropdown = Combobox(master, textvariable=self.platformEntry, values=["Windows", "macOS", "Linux"])
        self.platformDropdown.grid(row=3, column=1)

        # Software box
        self.softwareLabel = Label(master, text="Software")
        self.softwareLabel.grid(row=4, column=0, sticky="w")
        self.softwareEntry = Entry(master)
        self.softwareEntry.grid(row=4, column=1)

        # Error type box
        self.errorTypeLabel = Label(master, text="Error Type")
        self.errorTypeLabel.grid(row=5, column=0, sticky="w")
        self.errorTypeEntry = StringVar()
        self.errorTypeDropdown = Combobox(master, textvariable=self.errorTypeEntry, values=["Crash", "Performance", "UI Issue", "Other (specify in description)"])
        self.errorTypeDropdown.grid(row=5, column=1)

        # Impact box
        self.impactLabel = Label(master, text="Impact")
        self.impactLabel.grid(row=6, column=0, sticky="w")
        self.impactEntry = StringVar()
        self.impactDropdown = Combobox(master, textvariable=self.impactEntry, values=["Customer", "Developer", "Individual"])
        self.impactDropdown.grid(row=6, column=1)

        # Date & Time box
        # self.dateTimeLabel = Label(master, text="Date & Time")
        # self.dateTimeLabel.grid()
        # self.dateTimeEntry = Entry(master)
        # self.dateTimeEntry.insert(0, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # self.dateTimeEntry.grid()

        # Email box
        self.emailLabel = Label(master, text="Email")
        self.emailLabel.grid(row=7, column=0, sticky="w")
        self.emailEntry = Entry(master)
        self.emailEntry.grid(row=7, column=1)

        # Phone number box
        self.phoneLabel = Label(master, text="Phone Number")
        self.phoneLabel.grid(row=8, column=0, sticky="w")
        self.phoneEntry = Entry(master)
        self.phoneEntry.grid(row=8, column=1)

        # Description box
        self.descriptionLabel = Label(master, text="Description")
        self.descriptionLabel.grid(row=9, column=0, sticky="w")
        self.descriptionEntry = Entry(master)
        self.descriptionEntry.grid(row=9, column=1)

        # Submit button
        self.submitButton = Button(master, command=self.buttonClick, text="Submit")
        self.submitButton.grid(row=11, column=0, columnspan=2)

    # stores gui input in class variables
    def buttonClick(self):
        self.emp_name = self.nameEntry.get()
        self.emp_num = self.empNumEntry.get()
        self.department = self.departmentEntry.get()
        self.platform = self.platformEntry.get()
        self.soft_name = self.softwareEntry.get()
        self.error_type = self.errorTypeEntry.get()
        self.impact = self.impactEntry.get()
        # self.date_time = self.dateTimeEntry.get()
        self.email = self.emailEntry.get()
        self.phone_num = self.phoneEntry.get()
        
    
# Uncomment this and implement a main function in this file if you want to test just this class
#if __name__ == "__main__":    
    #guiFrame = GUI()
    #guiFrame.mainloop()

