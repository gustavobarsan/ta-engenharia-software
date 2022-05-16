from schemas.aluno import aluno_entity_in_disciplina
from schemas.professor import professor_entity_in_disciplina


def disciplina_entity(entity: dict):
    return {
        'id': str(entity.get('_id')),
        'nome': entity.get('nome'),
        'alunos': [aluno_entity_in_disciplina(aluno) for aluno in entity.get('alunos')],
        'professores': [professor_entity_in_disciplina(professor) for professor in entity.get('professores')],
    }


def disciplina_entity_in_mensagem(entity: dict):
    return {
        'id': entity.get('id')
    }
    