from fastapi import APIRouter, HTTPException
from config.db import get_database
from bson import ObjectId

from models.mensagem_model import Mensagem, UpdateMensagem
from schemas.mensagem import mensagem_entity

mensagem = APIRouter()

conn_db = get_database()


@mensagem.get('/disciplina/{id_disciplina}', status_code=200)
def find_all_mensagens_by_id_disciplina(id_disciplina: str):
    mensagens = conn_db['mensagens'].find({'disciplina.id': id_disciplina})

    if not mensagens:
        raise HTTPException(status_code=200, detail='Nenhuma mensagem encontrada')

    return [mensagem_entity(msg) for msg in mensagens]


@mensagem.post('/create', status_code=201)
def create_mensagem(body: Mensagem):
    new_mensagem = body.dict()

    id_new_mensagem = conn_db['mensagens'].insert_one(new_mensagem).inserted_id
    msg = conn_db['mensagens'].find_one({"_id": ObjectId(id_new_mensagem)})

    return [mensagem_entity(msg)]


@mensagem.put('/update/{id_mensagem}', status_code=200)
def update_mensagem(id_mensagem: str, body: UpdateMensagem):
    mensagem_modify = body.dict()

    if not mensagem_modify['new_text']:
        raise HTTPException(status_code=400, detail='A mensagem não pode ser vazia!')

    conn_db['mensagens'].find_one_and_update(
        {'_id': ObjectId(id_mensagem)},
        {'$set': {
            'text': mensagem_modify['new_text']
        }}
    )

    mensagem_modified = conn_db['mensagens'].find_one({"_id": ObjectId(id_mensagem)})

    return [mensagem_entity(mensagem_modified)]


@mensagem.delete('/delete/{id_mensagem}')
def delete_mensagem(id_mensagem: str):
    conn_db['mensagens'].find_one_and_delete({'_id': ObjectId(id_mensagem)})
    return {'msg': 'Mensagem deletada com sucesso!'}
