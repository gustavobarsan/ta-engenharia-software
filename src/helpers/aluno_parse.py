def aluno_parse(entity_aluno) -> dict:
    return {
        "id": str(entity_aluno['_id']),
        "nome": entity_aluno['nome'],
        "email": entity_aluno['email'],
        "disciplinas": entity_aluno['disciplina'],
        "adm": entity_aluno['adm'],
    } 

def editar_aluno_parse(entity_aluno) -> dict:
    for i in entity_aluno:
        if entity_aluno[i] == None:
            del entity_aluno[i]
    return {
        "nome": entity_aluno['nome'],
        "email": entity_aluno['email'],
        "senha": entity_aluno['senha'],
    } 

def aluno_parse_adm(entity_aluno) -> dict:
    return {
        "nome": entity_aluno['nome'],
        "email": entity_aluno['email'],
        "senha": entity_aluno['senha'],
        "disciplinas": entity_aluno['disciplina'],
        "adm": entity_aluno['adm'],
    } 