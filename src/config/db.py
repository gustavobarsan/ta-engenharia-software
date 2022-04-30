import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
conn_str = os.environ.get('CONNECTION_STRING')
def get_database():
    from pymongo import MongoClient
    client = MongoClient(conn_str)
    return client['taesDbDev']
    