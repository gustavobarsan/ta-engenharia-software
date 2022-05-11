from pydantic import BaseModel
from typing import Optional
from professor_model import Professor

class Curso(BaseModel):
    id: Optional[str] = None
    nome_curso: str
    descricao_curso: Optional[str] = None
    professor_vinculado: Professor