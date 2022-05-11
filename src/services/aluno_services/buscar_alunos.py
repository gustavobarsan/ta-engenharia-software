from config.db import get_database
from helpers.aluno_parse import aluno_parse

conn_db = get_database()

def buscar_alunos() -> list:
    aluno_list = conn_db['usuario'].find({"adm":False})
    return [aluno_parse(aluno) for aluno in aluno_list] 
