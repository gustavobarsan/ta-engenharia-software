from pydantic import BaseModel
from typing import Optional, List
from aluno_model import Aluno
from curso_model import Curso

class Professor(BaseModel):
    id: Optional[str] = None
    nome_professor: str
    mensagem: str
    email_institucional_professor: str
    lista_alunos: List[Aluno]
    lista_cursos: List[Curso]