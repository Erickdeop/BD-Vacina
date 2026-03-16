from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.paciente import PacienteRead
from app.schemas.vacina import VacinaRead


class RegistroVacinacaoBase(BaseModel):
    id_paciente: int
    id_vacina: int
    numero_dose: int = Field(ge=1, le=10)
    data_aplicacao: date
    lote: str = Field(min_length=2, max_length=50)
    nome_vacinador: str = Field(min_length=3, max_length=120)


class RegistroVacinacaoCreate(RegistroVacinacaoBase):
    pass


class RegistroVacinacaoUpdate(BaseModel):
    id_vacina: int | None = None
    numero_dose: int | None = Field(default=None, ge=1, le=10)
    data_aplicacao: date | None = None
    lote: str | None = Field(default=None, min_length=2, max_length=50)
    nome_vacinador: str | None = Field(default=None, min_length=3, max_length=120)


class RegistroVacinacaoRead(RegistroVacinacaoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class RegistroHistoricoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    numero_dose: int
    data_aplicacao: date
    lote: str
    nome_vacinador: str
    vacina: VacinaRead


class HistoricoPacienteResponse(BaseModel):
    paciente: PacienteRead
    registros: list[RegistroHistoricoRead]
