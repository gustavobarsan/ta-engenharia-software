from config.db import get_database
from bson.objectid import ObjectId
from models.professor_model import Professor
from helpers.professor_parse import editar_professor_parse

def editar_professor(id:str, professor :professor):
    parse_professor = editar_professor_parse(professor)
    professor = conn_db['usuarios'].update_one({_id: ObjectId(id)},{
        "$set": parse_professor
        })
    
    return  'editado'