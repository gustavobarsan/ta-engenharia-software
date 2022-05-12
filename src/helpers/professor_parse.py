
from models.professor_model import ProfessorEditar

def editar_professor_parse(entity_professor: ProfessorEditar) -> dict:
    
    # print(entity_professor.nome)
    new_entity_professor = entity_professor.dict()
    # for key in new_entity_professor.keys(): 
    #     if new_entity_professor[key] == None or new_entity_professor[key] == '':
    #         del new_entity_professor[key]

    if entity_professor.nome :
        new_entity_professor['nome'] = entity_professor.nome
    if entity_professor.email :
        new_entity_professor['email'] = entity_professor.email
    if entity_professor.senha :
        new_entity_professor['senha'] = entity_professor.senha        
    return new_entity_professor 