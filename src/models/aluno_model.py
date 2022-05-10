from pydantic import BaseModel
from typing import Optional, List
from models import Disciplina

class Aluno(BaseModel):
    id: Optional[str] = None
    nome_aluno: str
    mensagem: str
    email_institucional_aluno: Optional[str] = ''
    disciplina_aluno: List[Disciplina]
    active: bool = False