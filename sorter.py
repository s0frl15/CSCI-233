

from ticketclass import Ticket_List  
ticket_list = Ticket_List()

customer_list = []
developer_list = []
individual_list = []

for ticket in ticket_list:  # sorts based on impact
    if ticket.impact == "customer":
        customer_list.append(ticket)
        customer_list.sort(key=lambda ticket: ticket.date_time)
    elif ticket.impact == "developer":
        developer_list.append(ticket)
        developer_list.sort(key=lambda ticket: ticket.date_time)
    else:
        individual_list.append(ticket)
        individual_list.sort(key=lambda ticket: ticket.date_time)

#combines the 3 list into 1
sorted_list = customer_list + developer_list + individual_list



# TESTING USE ONLEY!!!
print("\nMerged and Sorted List:")
for ticket in sorted_list:
    print(f"{ticket.emp_name}")  #just prints the names in order for testing

#desired output
#alice
#john
#pax
#bob
#jesus
#levi
