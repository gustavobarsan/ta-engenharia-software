from fastapi import APIRouter
from models.professor_model import Professor
from config.db import get_database
from services.professor_services.find_professors import get_all_professors

conn_db = get_database()
professor = APIRouter()

@professor.post('/professor')
def create_professor(professor: Professor):
    new_professor = dict(professor)
    print(new_professor)
    resp = conn_db.professor.insert_one(new_professor).inserted_id
    return str(resp)

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