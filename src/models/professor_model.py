from typing import Optional, List
from pydantic import BaseModel

class Professor(BaseModel):
    nome: str
    email: str
    password: str  
    disciplina: List[str]