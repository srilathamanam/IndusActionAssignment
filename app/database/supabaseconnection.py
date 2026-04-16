#This code is for connecting supabase database

from supabase import create_client
import os
from dotenv import load_dotenv
load_dotenv()

'''
Get Supabase url and key from environment variables
'''
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

'''
Create client to perform CRUD operations
'''
supabase=create_client(url,key) 