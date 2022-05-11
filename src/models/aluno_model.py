from pydantic import BaseModel
from typing import Optional, List

class Aluno(BaseModel):
    nome: str
    email: str
    senha: str
    disciplina: List[str]
    adm: bool = False