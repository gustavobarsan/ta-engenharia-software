from config.db import get_database
from pymongo import ObjectId
from helpers.aluno_parse import aluno_parse

conn_db = get_database()

def deletar_aluno(id: str):
    conn_db['usuario'].delete_one({"_id":ObjectId(id)})
    return 'Deletado.'
