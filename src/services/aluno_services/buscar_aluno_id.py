from config.db import get_database
from helpers.aluno_parse import aluno_parse
from bson.objectid import ObjectId

conn_db = get_database()

def buscar_aluno_id(id: str) -> list:
    aluno = conn_db['usuarios'].find_one({"_id":ObjectId(id)})
    return aluno_parse(aluno)
