def autor_entity_in_mensagem(entity: dict):
    return {
        'id': entity.get('id'),
        'nome': entity.get('nome')
    }
