from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.paciente import Paciente
    from app.models.vacina import Vacina


class RegistroVacinacao(Base):
    __tablename__ = "registros_vacinacao"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_paciente: Mapped[int] = mapped_column(ForeignKey("pacientes.id"), nullable=False, index=True)
    id_vacina: Mapped[int] = mapped_column(ForeignKey("vacinas.id"), nullable=False, index=True)
    numero_dose: Mapped[int] = mapped_column(Integer, nullable=False)
    data_aplicacao: Mapped[date] = mapped_column(Date, nullable=False)
    lote: Mapped[str] = mapped_column(String(50), nullable=False)
    nome_vacinador: Mapped[str] = mapped_column(String(120), nullable=False)

    paciente: Mapped["Paciente"] = relationship(back_populates="registros")
    vacina: Mapped["Vacina"] = relationship(back_populates="registros")
