from fastapi import FastAPI
from db import get_database

app = FastAPI()

@app.get("/")
async def root():
    dbconn = get_database()
    response = [msg['message'] for msg in dbconn['test'].find({})]
    return response[0]
