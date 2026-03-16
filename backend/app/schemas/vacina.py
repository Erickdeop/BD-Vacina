from pydantic import BaseModel, ConfigDict, Field


class VacinaBase(BaseModel):
    nome_comercial: str = Field(min_length=2, max_length=120)
    grupo_doenca: str = Field(min_length=2, max_length=120)


class VacinaCreate(VacinaBase):
    pass


class VacinaRead(VacinaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
