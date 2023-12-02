from supabaseconnector import SupabaseConnector
from ticketclass import Ticket

class TicketList(list):
    def __init__(self):
        self.supabase = SupabaseConnector().connect_to_supabase()
        self.response = self.supabase.table("bug_report").select("*").execute()

    # Dynamically creates tickets and adds them to the list
        data = self.response.data
        i = 0

        for ticket in data:
            # Ignores closed tickets
            if ticket['is_open'] == "Open":
                # This creates a string of python code that we will then execute. 
                # It is useful since we do not know how many tickets will be created until runtime
                new_ticket = ('t' + str(i) + ' = Ticket(ticket[\'agent_id\'], '  
                                                     + 'ticket[\'platform\'], ' 
                                                     + 'ticket[\'software_name\'], ' 
                                                     + 'ticket[\'error_type\'], ' 
                                                     + 'ticket[\'impact\'], ' 
                                                     + 'ticket[\'description\'], '
                                                     + 'ticket[\'created_at_time\'])' )
                # exec() is a terrible function to use, especially for this specific purpose. It is very
                # susceptible to code injection, but I could not find an alternative solution without 
                # sacrificing performance or sorting on the database side. Do not do this >:(
                exec(new_ticket)
                add_ticket = 'self.append(t' + str(i) + ')'
                exec(add_ticket)
                i += 1

    # def print_response(self):
    #     print(self.response)





# TESTING
# ticketlist = TicketList()

# ticketlist.print_response()
# print(ticketlist)
# print(ticketlist.response.data[0]['report_number'])
# ticketlist.create_list()
# print(ticketlist[0])
# printing = 'print(ticketlist[0].emp_num)'
# exec(printing)