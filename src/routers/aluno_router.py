from fastapi import APIRouter, Request
from helpers.aluno_parse import aluno_parse
from models.aluno_model import Aluno
from config.db import get_database
from services.aluno_services.criar_aluno import criar_aluno
from services.aluno_services.buscar_alunos import buscar_alunos
from services.aluno_services.buscar_aluno_id import buscar_aluno_id
from services.aluno_services.deletar_aluno import deletar_aluno
from services.aluno_services.editar_aluno import editar_aluno


conn_db = get_database()
api_aluno = APIRouter()

@api_aluno.post('/aluno')
def create_aluno(aluno: Aluno):
    return criar_aluno(aluno)

@api_aluno.get('/aluno')
def find_all_alunos():
    return buscar_alunos()

@api_aluno.get('/aluno/{id}')
def find_aluno(id: str):
    return buscar_aluno_id(id)

@api_aluno.patch('/aluno/{id}')
def edit_aluno(id: str, aluno: Aluno):
    return editar_aluno(id, aluno)

@api_aluno.delete('/aluno/{id}')
def delete_aluno(id: str):
    return deletar_aluno(id)