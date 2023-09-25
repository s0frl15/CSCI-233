#
# Ticket Class
#
# Pozzuoli, Antony
# CSCI 333 Group Project
# 09/25/2023
#

class Ticket:
    # Constructor that defaults all variables as an empty string
    def __init__(self, emp_num = "123", platform = "", soft_name = "", error_type = "", impact = "", dteo = "", email = "", phone_num = "", description = ""):
        # Creates class variables and sets them equal to their default values
        self.emp_num = emp_num
        self.platform = platform
        self.soft_name = soft_name
        self.impact = impact
        self.dteo = dteo
        self.email = email
        self.phone_num = phone_num
        self.description = description
        # No getters/setters required!

# How to implement this:
# 1. import this file using <from ticketclass import Ticket>

# 2. Create a new ticket object:
# ticket = Ticket()

# 3. Set the variables of your new ticket object as needed:
# ticket.emp_num = "123"