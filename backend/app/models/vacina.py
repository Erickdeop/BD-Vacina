from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.registro_vacinacao import RegistroVacinacao


class Vacina(Base):
    __tablename__ = "vacinas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome_comercial: Mapped[str] = mapped_column(String(120), nullable=False)
    grupo_doenca: Mapped[str] = mapped_column(String(120), nullable=False)

    registros: Mapped[list["RegistroVacinacao"]] = relationship(back_populates="vacina")
