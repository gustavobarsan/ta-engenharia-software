import os
from dotenv import load_dotenv, find_dotenv
# from pymongo import MongoClient

load_dotenv(find_dotenv())
conn_str = os.environ.get('CONNECTION_STRING')
def get_database():
    from pymongo import MongoClient
    client = MongoClient(conn_str)
    return client['taesDbDev']
    
# if __name__ == "__main__":    
#     dbconn = get_database()