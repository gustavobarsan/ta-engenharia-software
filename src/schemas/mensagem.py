from src.schemas.autor import autor_entity_in_mensagem
from src.schemas.disciplina import disciplina_entity_in_mensagem


def mensagem_entity(entity: dict):
    return {
        'id': str(entity.get('_id')),
        'autor': autor_entity_in_mensagem(entity.get('autor')),
        'texto': entity.get('text'),
        'disciplina': disciplina_entity_in_mensagem(entity.get('disciplina')),
        'data_hora': entity.get('data_hora')
    }
