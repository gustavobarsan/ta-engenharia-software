from config.db import get_database
from bson.objectid import ObjectId
from models.professor_model import Professor, ProfessorEditar
from helpers.professor_parse import editar_professor_parse

def editar_professor(id:str, professor: ProfessorEditar):
    conn_db = get_database()
    parse_professor = editar_professor_parse(professor)
    professor = conn_db['usuarios'].update_one({"_id": ObjectId(id)},{
        "$set": parse_professor
        })
    
    return  'editado'