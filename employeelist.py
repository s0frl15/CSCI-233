from supabaseconnector import SupabaseConnector

class Employee():
    def __init__(self,first="", last="", email="", department="", phone_num=0, emp_num=0, is_avail=True):
        self.first = first
        self.last = last
        self.email = email
        self.department = department
        self.phone_num = phone_num
        self.emp_num = emp_num
        self.is_avail = is_avail

class EmployeeList(list):
    def __init__(self):
        self.supabase = SupabaseConnector().connect_to_supabase()
        self.response = self.supabase.table("employee").select("*").execute()

        # Dynamically creates employee objects and adds them to the list
        data = self.response.data
        i = 0

        for employee in data:
            # Ignores closed tickets
            if employee['is_avail']:
                # This creates a string of python code that we will then execute. 
                # It is useful since we do not know how many employees will be created until runtime
                new_list = ('e' + str(i) + ' = Employee(employee[\'first_name\'], '  
                                                     + 'employee[\'last_name\'], ' 
                                                     + 'employee[\'email\'], ' 
                                                     + 'employee[\'department\'], ' 
                                                     + 'employee[\'phone_number\'], ' 
                                                     + 'employee[\'emp_num\'], '
                                                     + 'employee[\'is_avail\'])' )
                # exec() is a terrible function to use, especially for this specific purpose. It is very
                # susceptible to code injection, but I could not find an alternative solution without 
                # sacrificing performance or sorting on the database side. Do not do this >:(
                exec(new_list)
                add_employee = 'self.append(e' + str(i) + ')'
                exec(add_employee)
                i += 1


# TESTING - This is how you might implement this file and access its contents

# from employeelist import EmployeeList     # Make sure this is included at the top of your file

# Create a new instance of EmployeeList (Do not put this in a loop. It will connect to the database as soon as you create it):
# employeelist = EmployeeList() 

# Examples of how to access individual variables from your employee list:
# print(employeelist[0].first)      # This prints the first name of the first person in the list
# print(employeelist[1].last)       # This prints the last name of the second person in the list
# print(employeelist[2].department) # This prints the department of the third person in the list
# print(employeelist[3].is_avail)   # This prints the availability of the fourth person in the list