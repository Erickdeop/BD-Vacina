from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.database.session import get_db
from app.models.paciente import Paciente
from app.models.registro_vacinacao import RegistroVacinacao
from app.models.vacina import Vacina
from app.schemas.registro_vacinacao import (
    HistoricoPacienteResponse,
    RegistroVacinacaoCreate,
    RegistroVacinacaoRead,
    RegistroVacinacaoUpdate,
)

router = APIRouter(tags=["Registros de Vacinacao"])


@router.post("/registros", response_model=RegistroVacinacaoRead, status_code=status.HTTP_201_CREATED)
def create_registro(payload: RegistroVacinacaoCreate, db: Session = Depends(get_db)) -> RegistroVacinacao:
    paciente = db.get(Paciente, payload.id_paciente)
    if not paciente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente nao encontrado")

    vacina = db.get(Vacina, payload.id_vacina)
    if not vacina:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacina nao encontrada")

    registro = RegistroVacinacao(**payload.model_dump())
    db.add(registro)
    db.commit()
    db.refresh(registro)
    return registro


@router.get("/registros", response_model=list[RegistroVacinacaoRead])
def list_registros(
    paciente_id: int | None = Query(default=None, alias="id_paciente"),
    db: Session = Depends(get_db),
) -> list[RegistroVacinacao]:
    stmt = select(RegistroVacinacao)
    if paciente_id is not None:
        stmt = stmt.where(RegistroVacinacao.id_paciente == paciente_id)

    return list(db.scalars(stmt.order_by(RegistroVacinacao.data_aplicacao.desc())).all())


@router.get("/registros/{registro_id}", response_model=RegistroVacinacaoRead)
def get_registro(registro_id: int, db: Session = Depends(get_db)) -> RegistroVacinacao:
    registro = db.get(RegistroVacinacao, registro_id)
    if not registro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")
    return registro


@router.put("/registros/{registro_id}", response_model=RegistroVacinacaoRead)
def update_registro(
    registro_id: int,
    payload: RegistroVacinacaoUpdate,
    db: Session = Depends(get_db),
) -> RegistroVacinacao:
    registro = db.get(RegistroVacinacao, registro_id)
    if not registro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(registro, field, value)

    db.commit()
    db.refresh(registro)
    return registro


@router.delete("/registros/{registro_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_registro(registro_id: int, db: Session = Depends(get_db)) -> None:
    registro = db.get(RegistroVacinacao, registro_id)
    if not registro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro nao encontrado")

    db.delete(registro)
    db.commit()


@router.get("/pacientes/{paciente_id}/historico", response_model=HistoricoPacienteResponse)
def get_historico_paciente(paciente_id: int, db: Session = Depends(get_db)) -> HistoricoPacienteResponse:
    paciente = db.get(Paciente, paciente_id)
    if not paciente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente nao encontrado")

    stmt = (
        select(RegistroVacinacao)
        .options(joinedload(RegistroVacinacao.vacina))
        .where(RegistroVacinacao.id_paciente == paciente_id)
        .order_by(RegistroVacinacao.data_aplicacao.desc())
    )
    registros = list(db.scalars(stmt).all())

    return HistoricoPacienteResponse(paciente=paciente, registros=registros)
