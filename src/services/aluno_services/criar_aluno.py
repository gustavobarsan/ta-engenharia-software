from config.db import get_database
from models.aluno_model import Aluno

conn_db = get_database()

def criar_aluno(aluno: Aluno):
    new_aluno = dict(aluno)
    resp = conn_db.usuario.insert_one(new_aluno).inserted_id
    return str(resp)
