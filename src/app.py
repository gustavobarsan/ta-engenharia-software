from fastapi import FastAPI
from config.db import get_database

app = FastAPI()

@app.get("/")
async def root():
    # dbconn = get_database()
    # response = [msg['message'] for msg in dbconn['test'].find({})]
    # return response[0]
    return "PROJETO TAES 2022 - UNIFTC"
