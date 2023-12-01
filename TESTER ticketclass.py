# ticketclass.py
class Ticket:
    def __init__(self, emp_name="", emp_num="123", impact="", date_time=""):
        self.emp_name = emp_name
        self.emp_num = emp_num
        self.impact = impact
        self.date_time = date_time

class Ticket_List:
    def __init__(self):
        # Sample Ticket data
        self.tickets = [
            Ticket(emp_name="John", emp_num="101", impact="customer", date_time="2023/02/20, 11:30AM"),
            Ticket(emp_name="Alice", emp_num="102", impact="customer", date_time="2023/02/20, 10:45AM"),
            Ticket(emp_name="Bob", emp_num="103", impact="developer", date_time="2023/03/05, 02:00PM"),
            Ticket(emp_name="pax", emp_num="104", impact="developer", date_time="2023/03/05, 01:00PM"),
            Ticket(emp_name="levi", emp_num="105", impact="individual", date_time="2023/04/05, 02:00PM"),
            Ticket(emp_name="jesus", emp_num="106", impact="individual", date_time="2023/04/05, 01:00PM")
            # Add more sample Ticket instances as needed
        ]

    def __iter__(self):
        return iter(self.tickets)
