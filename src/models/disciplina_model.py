from pydantic import BaseModel
from typing import Optional, List
from models.professor_model import Professor
from models.aluno_model import AlunoInDisciplina
from models.professor_model import ProfessorInDisciplina


class Disciplina(BaseModel):
    nome: str
    alunos: List[AlunoInDisciplina]
    professores: List[ProfessorInDisciplina]


class DisciplinaInMensagem(BaseModel):
    id: str