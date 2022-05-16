from pydantic import BaseModel
from typing import List


class Aluno(BaseModel):
    nome: str
    email: str
    senha: str
    disciplina: List[str]
    adm: bool = False


class AlunoInDisciplina(BaseModel):
    id: str
    nome: str
