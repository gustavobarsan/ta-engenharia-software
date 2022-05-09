from typing import Optional
from pydantic import BaseModel

class Professor(BaseModel):
    id: Optional[str]
    nome: str
    email: str
    password: str  