import os
from supabase import create_client, Client

class SupabaseConnector():
    def connect_to_supabase(self):
        url = "https://khvejwjcfkodkcwtlbeo.supabase.co"
        # NOTE: Private key must be used to interact with database tables
        key = "PRIVATE KEY"
        supabase = create_client(url, key)

        return supabase
    
# READ ME
# Paste in your private key (ln 8) from supabase before running the program
# DO NOT upload this file with your private key to github