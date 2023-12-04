from listticketclass import TicketList  
from employeelist import EmployeeList

def highest_ticket():
    ticket_list = TicketList()

    customer_list = []
    developer_list = []
    individual_list = []

    for ticket in ticket_list:  # sorts based on impact
        if ticket.impact == 'Customer':
            print("Added ticket to customer list")
            customer_list.append(ticket)
            customer_list.sort(key=lambda ticket: ticket.date_time)
        elif ticket.impact == "Developer":
            developer_list.append(ticket)
            developer_list.sort(key=lambda ticket: ticket.date_time)
        else:
            individual_list.append(ticket)
            individual_list.sort(key=lambda ticket: ticket.date_time)

    #combines the 3 list into 1
    sorted_list = customer_list + developer_list + individual_list

    # TESTING ONLEY LINE 26-37, 43
    # print("\nMerged and Sorted List:")
    # for ticket in sorted_list:
    #    print(f"{ticket.emp_name}")  #just prints the names in order for testing

    #desired output
    #alice
    #john
    #pax
    #bob
    #jesus
    #levi


    return sorted_list[0]

# TESTING ONLEY
# highest_ticket()

def assign_tickets_with_priority():
    employees = EmployeeList()
    highest_priority_ticket = highest_ticket()

    for employee in employees:
        if employee.can_take_ticket(highest_priority_ticket):
            employee.assign_ticket(highest_priority_ticket)
            break  # Assign only to the first employee who can take the ticket

# Example usage:
assign_tickets_with_priority()
