from config.db import get_database
from models.professor_model import Professor

conn_db = get_database()

def criar_professor(professor: Professor):
    new_professor = dict(professor)
    print(new_professor)
    resp = conn_db.usuario.insert_one(new_professor).inserted_id
    return str(resp)
