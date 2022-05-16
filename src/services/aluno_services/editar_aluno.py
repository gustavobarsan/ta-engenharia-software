from config.db import get_database
from bson.objectid import ObjectId
from helpers.aluno_parse import editar_aluno_parse

conn_db = get_database()


def editar_aluno(id: str, aluno):
    aluno_editado = editar_aluno_parse(aluno)
    conn_db['usuarios'].update_one({"_id": ObjectId(id)}, {
        "$set": aluno_editado
    })
    return 'Atualizado.'
