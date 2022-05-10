from pydantic import BaseModel
from typing import Optional
from professor_model import Professor

class Disciplina(BaseModel):
    id: Optional[str] = None
    nome_disciplina: str
    professor_vinculado: Professor
    