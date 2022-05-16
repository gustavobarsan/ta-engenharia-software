def aluno_entity_in_disciplina(entity: dict):
    return {
        'id': entity.get('id'),
        'nome': entity.get('nome')
    }
