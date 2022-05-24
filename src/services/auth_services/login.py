from config.db import get_database
from datetime import datetime, timedelta
from jose import jwt
import os
from models.auth_model import Login
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
SECRET_KEY = os.environ.get('SECRET_KEY')

expire = datetime.utcnow() + timedelta(minutes=1000)
conn_db = get_database()

def login(email_c:str, senha_c:str): 
    credenciais = {
        "email": email_c,
        "senha": senha_c
    }
    usuario = conn_db.usuarios.find_one(credenciais, {"senha": 0})

    print(usuario)

    if usuario:
        usuario['id'] = str(usuario['_id'])
        del usuario['_id']
        encoded_jwt = jwt.encode(usuario, SECRET_KEY, algorithm="HS256")
        return encoded_jwt

    return False

    
