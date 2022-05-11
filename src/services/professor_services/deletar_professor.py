from config.db import get_database
from bson.objectid import ObjectId
from models.professor_model import Professor


def deletar_professor(id: str):
     conn_db['usuarios'].delete_one({"_id":ObjectId(id)})
     return 'Deletado.'