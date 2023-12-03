from tkinter import *

class BugFixer:
    def __init__(self, master):
        self.master = master
        master.title("Bug Fixer Update Window")

        #dummy data for assigned bugs
        self.assigned_bugs = ["Bug 1", "Bug 2", "Bug 3"]

        #listbox for assigned bugs
        self.bug_listbox = Listbox(master, selectmode=SINGLE)
        for bug in self.assigned_bugs:
            self.bug_listbox.insert(END, bug)
        self.bug_listbox.pack(pady=10)

        #submit fixed button
        self.submit_button = Button(master, text="Submit Fixed", command=self.submit_fixed_bug)
        self.submit_button.pack()

        #refresh button
        self.refresh_button = Button(master, text="Refresh", command=self.refresh_bug_list)
        self.refresh_button.pack()


    def submit_fixed_bug(self):
        selected_index = self.bug_listbox.curselection()
        if selected_index:
            #fixed bug submission confirmation
            selected_bug = self.bug_listbox.get(selected_index)
            print(f"Bug '{selected_bug}' submitted as fixed.")
            #removal
            self.bug_listbox.delete(selected_index)
            
            #insert function to update the database here🚩

    def refresh_bug_list(self):
        #dummy data for updated bug list
        update_bugs = ["Bug 4", "Bug 5", "Bug 6"]
        #set the value of the variable above 
        #to the function to pull from the database🚩

        #new bug insertion
        for bug in update_bugs:
            self.bug_listbox.insert(END, bug)

    
#uncomment the 4 lines below to create a mainloop for testing
#if __name__ == "__main__":
    #root = Tk()
    #app = BugFixer(root)
    #root.mainloop()
