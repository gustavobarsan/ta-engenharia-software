from config.db import get_database

conn_db = get_database()

def professor_parse(entity_professor) -> dict:
    return {
        "id": str(entity_professor['_id']),
        "nome": entity_professor['nome'],
        "email": entity_professor['email'],
        "disciplina:": entity_professor['disciplina'],
    } 

def get_all_professors() -> list:
    professor_list = conn_db['usuarios'].find({"adm":True})
    return [professor_parse(professor) for professor in professor_list] 

    
