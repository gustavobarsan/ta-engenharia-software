from fastapi import APIRouter
from models.professor_model import Professor

professor = APIRouter()

@professor.get('/professor')
def find_professor():
    return "TAES-2022.1"

@professor.post('/professor')
def create_professor(professor: Professor):
    return "TAES-2022.2"

@professor.get('/professor/{id}')
def create_professor():
    return "TAES-2022.1"

@professor.put('/professor/{id}')
def edit_professor(professor: Professor):
    return "TAES-2022.1"

@professor.delete('/professor/{id}')
def edit_professor():
    return "TAES-2022.1"