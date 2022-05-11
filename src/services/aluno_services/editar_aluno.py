from config.db import get_database
from pymongo import ObjectId
from helpers.aluno_parse import editar_aluno_parse

conn_db = get_database()

def editar_aluno(id: str, aluno):
  aluno_editado = editar_aluno_parse(aluno)
  conn_db['usuario'].update_one({"_id":ObjectId(id)},{
    "$set": aluno_editado
  })
  return 'Atualizado.'
