from fastapi import APIRouter
from models.professor_model import Professor
from config.db import get_database
from services.professor_services.find_professors import get_all_professors
from services.professor_services.criar_professor import criar_professor

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


@professor.put('/professor/{id}')
def edit_professor(professor: Professor):
    return "TAES-2022.1"


@professor.delete('/professor/{id}')
def edit_professor():
    return "TAES-2022.1"
