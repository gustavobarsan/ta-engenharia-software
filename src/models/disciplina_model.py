from pydantic import BaseModel
from typing import Optional, List
from src.models.professor_model import Professor
from src.models.aluno_model import AlunoInDisciplina
from src.models.professor_model import ProfessorInDisciplina


class Disciplina(BaseModel):
    nome: str
    alunos: List[AlunoInDisciplina]
    professores: List[ProfessorInDisciplina]


class DisciplinaInMensagem(BaseModel):
    id: str