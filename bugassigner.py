from employeelist import EmployeeList
from sorter import highest_ticket

class BugAssigner:
    def __init__(self):
        self.employee_list = EmployeeList()
        self.bug_sorter = highest_ticket()
        
        # Initialize dictionary to hold bug assignments
        self.bug_assignments = {}

    def assign_bugs(self):
        # Get sorted list of bugs
        sorted_bugs = self.bug_sorter.get_sorted_bugs()
        
        # Get list of employees
        employees = self.employee_list.get_employees()

        # Assign bugs to employees based on priority
        for i in range(len(sorted_bugs)):
            # Cycle through employees as bugs are assigned
            employee = employees[i % len(employees)]
            
            # If employee has been assigned a bug before, append to their list
            if employee in self.bug_assignments:
                self.bug_assignments[employee].append(sorted_bugs[i])
            else:
                self.bug_assignments[employee] = [sorted_bugs[i]]

        return self.bug_assignments
  
