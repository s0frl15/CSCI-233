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


def assign_tickets():
    employees = EmployeeList()
    sorted_list = highest_ticket()

    for ticket in sorted_list:
        if ticket.priority == 'Customer':
            employee = employees.get_next_available_employee()
            if employee is not None:
                employee.assign_ticket(ticket)
                print(f"Ticket {ticket.id} assigned to employee {employee.name}")
                ticket.mark_as_assigned()
            else:
                print(f"No available employees to assign ticket {ticket.id}")
        else:
            print(f"Skipping ticket {ticket.id} as it doesn't have the highest priority")

