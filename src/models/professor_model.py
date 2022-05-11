from typing import Optional, List
from pydantic import BaseModel

class Professor(BaseModel):
    nome: str
    email: str
    password: str  
    senha: str  
    disciplina: List[str]
    adm: bool
