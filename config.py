from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

TOKEN = getenv("TOKEN", None)
TOKEN = getenv("START_PIC", None)



"""
class Config:
    API_ID = 
    API_HASH = ""
    TOKEN = ""  
    START_PIC = "" 
    CHAT = ""    
"""
