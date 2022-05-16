from fastapi import APIRouter, HTTPException
from src.config.db import get_database
from bson import ObjectId
from src.schemas.disciplina import disciplina_entity
from src.models.disciplina_model import Disciplina

disciplina = APIRouter()

conn_db = get_database()


@disciplina.get('/', status_code=200)
def find_all_disciplinas():
    disciplinas = conn_db['disciplinas'].find()

    if not disciplinas:
        raise HTTPException(status_code=200, detail='Nenhuma disciplina encontrada')

    return [disciplina_entity(d) for d in disciplinas]


@disciplina.get('/{id_disciplina}', status_code=200)
def find_disciplina_by_id(id_disciplina: str):
    disciplina = conn_db['disciplinas'].find_one({"_id": ObjectId(id_disciplina)})

    if not disciplina:
        raise HTTPException(status_code=200, detail='Nenhuma disciplina encontrada')

    return [disciplina_entity(disciplina)]


@disciplina.post('/create', status_code=201)
def create_disciplina(disciplina: Disciplina):
    new_disciplina = disciplina.dict()

    if len(new_disciplina['professores']) == 0:
        raise HTTPException(status_code=400, detail='Ao menos um professor deve ser associado a nova disciplina!')

    id_new_disciplina = conn_db['disciplinas'].insert_one(new_disciplina).inserted_id
    new_disciplina = conn_db['disciplinas'].find_one({"_id": ObjectId(id_new_disciplina)})

    return [disciplina_entity(new_disciplina)]


@disciplina.put('/update/{id_disciplina}', status_code=200)
def update_disciplina(id_disciplina: str, disciplina: Disciplina):
    disciplina_modify = disciplina.dict()

    if len(disciplina_modify['professores']) == 0:
        raise HTTPException(status_code=400, detail='Ao menos um professor deve está associado a disciplina!')

    conn_db['disciplinas'].find_one_and_update(
        {'_id': ObjectId(id_disciplina)},
        {'$set': disciplina.dict()}
    )

    disciplina_modified = conn_db['disciplinas'].find_one({"_id": ObjectId(id_disciplina)})

    return [disciplina_entity(disciplina_modified)]


@disciplina.delete('/delete/{id_disciplina}')
def delete_disciplina(id_disciplina: str):
    conn_db['disciplinas'].find_one_and_delete({'_id': ObjectId(id_disciplina)})
    return {'msg': 'Disciplina deletada com sucesso!'}
