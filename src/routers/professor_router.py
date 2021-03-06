from fastapi import APIRouter
from models.professor_model import Professor, ProfessorEditar
from config.db import get_database
from services.professor_services.procurar_professors import get_all_professors
from services.professor_services.criar_professor import criar_professor
from services.professor_services.editar_professor import editar_professor
from services.professor_services.deletar_professor import deletar_professor

conn_db = get_database()
professor = APIRouter()


@professor.post('/professor')
def create_professor(professor: Professor):
    return criar_professor(professor)


@professor.get('/professor')
def find_all_professors():
    resp = get_all_professors()
    return resp


@professor.get('/professor/{id}')
def find_professor():
    return "TAES-2022.1"

@professor.patch('/professor/{id}')
def edit_professor(id: str, professor: ProfessorEditar):
    return editar_professor(id, professor)


@professor.delete('/professor/{id}')
def delet_professor(id):
    return deletar_professor(id)
