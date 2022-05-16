from fastapi import FastAPI
from routers.professor_router import professor
from routers.aluno_router import api_aluno
from routers.disciplina_router import disciplina
from routers.mensagem_router import mensagem

app = FastAPI()

app.include_router(professor)
app.include_router(api_aluno)
app.include_router(router=disciplina, prefix='/disciplina')
app.include_router(router=mensagem, prefix='/mensagem')


@app.get("/")
async def root():
    return "PROJETO TAES 2022 - UNIFTC"
