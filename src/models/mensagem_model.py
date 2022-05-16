from pydantic import BaseModel
from datetime import datetime

from models.autor_model import AutorInMensagem
from models.disciplina_model import DisciplinaInMensagem


class Mensagem(BaseModel):
    text: str
    autor: AutorInMensagem
    disciplina: DisciplinaInMensagem
    data_hora = datetime.now()


class UpdateMensagem(BaseModel):
    new_text: str

