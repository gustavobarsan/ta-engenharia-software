from pydantic import BaseModel


class AutorInMensagem(BaseModel):
    id: str
    nome: str
