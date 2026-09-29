# Rubayet Adbir

import os
from supabase import create_client, Client

PROJECT_URL = os.getenv("PROJECT_URL", "https://mwmbefrrpujuzqyiqkgz.supabase.co")
PROJECT_KEY = os.getenv("PROJECT_KEY", "sb_publishable_ggUAjGg45DgfjpVQvfJ7Ow_ETkOIYN-")

   # create a connection to our supabase using url,key,and it store it in a "db", create_client is the command between the python and supabase 
db: Client = create_client(PROJECT_URL, PROJECT_KEY)