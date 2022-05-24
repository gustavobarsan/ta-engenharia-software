from fastapi import APIRouter, Request, HTTPException
from services.auth_services.login import login
from models.auth_model import Login
auth_routes = APIRouter()

@auth_routes.post('/login')
def login_route(credenciais: Login):
    resp = login(str(credenciais.email), str(credenciais.senha))
    
    if not resp: 
        raise HTTPException(status_code=200, detail='Usuário ou senha incorreto')

    return resp

