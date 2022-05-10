from pydantic import BaseModel
from typing import Optional
from models import Curso

class Aluno(BaseModel):
    id: Optional[str] = None
    nome_aluno: str
    mensagem: str
    email_institucional_aluno: Optional[str] = ''
    curso_aluno: Curso