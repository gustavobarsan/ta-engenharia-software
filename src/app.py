from sys import prefix
from fastapi import FastAPI
from routers.professor_router import professor
from routers.aluno_router import api_aluno
from routers.disciplina_router import disciplina
from routers.mensagem_router import mensagem
from routers.auth_router import auth_routes

app = FastAPI()

app.include_router(professor)
app.include_router(api_aluno)
app.include_router(router=disciplina, prefix='/disciplina')
app.include_router(router=mensagem, prefix='/mensagem')
app.include_router(router=auth_routes, prefix='/auth')


@app.get("/")
async def root():
    return "PROJETO TAES 2022 - UNIFTC"
