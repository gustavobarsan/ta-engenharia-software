from typing import Optional, List
from pydantic import BaseModel

class Professor(BaseModel):
    nome: str
    email: str 
    senha: str  
    disciplina: List[str]
    adm: bool = True

class ProfessorEditar(BaseModel):
    nome: Optional[str]
    email: Optional[str]
    senha: Optional[str]

class ProfessorInDisciplina(BaseModel):
    id: str
    nome: str
