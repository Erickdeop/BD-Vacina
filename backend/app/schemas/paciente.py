from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class PacienteBase(BaseModel):
    nome: str = Field(min_length=3, max_length=120)
    cpf: str = Field(min_length=11, max_length=14)
    data_nascimento: date


class PacienteCreate(PacienteBase):
    pass


class PacienteRead(PacienteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
