from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.registro_vacinacao import RegistroVacinacao


class Paciente(Base):
    __tablename__ = "pacientes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), unique=True, nullable=False, index=True)
    data_nascimento: Mapped[date] = mapped_column(Date, nullable=False)

    registros: Mapped[list["RegistroVacinacao"]] = relationship(
        back_populates="paciente", cascade="all, delete-orphan"
    )
