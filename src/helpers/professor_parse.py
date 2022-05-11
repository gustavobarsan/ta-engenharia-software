
def editar_professor_parse(entity_professor) -> dict:
    new_entity_professor = {}
    if entity_professor['nome'] :
        new_entity_professor['nome'] = entity_professor['nome']
    if entity_professor['email'] :
        new_entity_professor['email'] = entity_professor['email']
    if entity_professor['senha'] :
        new_entity_professor['senha'] = entity_professor['senha']        
    
    return new_entity_professor 