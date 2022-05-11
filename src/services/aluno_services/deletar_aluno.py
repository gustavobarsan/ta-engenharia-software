from config.db import get_database
from bson.objectid import ObjectId
from helpers.aluno_parse import aluno_parse

conn_db = get_database()

def deletar_aluno(id: str):
    conn_db['usuarios'].delete_one({"_id":ObjectId(id)})
    return 'Deletado.'
