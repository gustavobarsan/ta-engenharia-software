from pydantic import BaseModel
from typing import List

class Login(BaseModel):
    email: str
    senha: str
