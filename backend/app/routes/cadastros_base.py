from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.paciente import Paciente
from app.models.vacina import Vacina
from app.schemas.paciente import PacienteCreate, PacienteRead
from app.schemas.vacina import VacinaCreate, VacinaRead

router = APIRouter(tags=["Cadastros Base"])


@router.post("/pacientes", response_model=PacienteRead, status_code=status.HTTP_201_CREATED)
def create_paciente(payload: PacienteCreate, db: Session = Depends(get_db)) -> Paciente:
    existing = db.scalar(select(Paciente).where(Paciente.cpf == payload.cpf))
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CPF ja cadastrado")

    paciente = Paciente(**payload.model_dump())
    db.add(paciente)
    db.commit()
    db.refresh(paciente)
    return paciente


@router.get("/pacientes", response_model=list[PacienteRead])
def list_pacientes(db: Session = Depends(get_db)) -> list[Paciente]:
    return list(db.scalars(select(Paciente).order_by(Paciente.nome)).all())


@router.post("/vacinas", response_model=VacinaRead, status_code=status.HTTP_201_CREATED)
def create_vacina(payload: VacinaCreate, db: Session = Depends(get_db)) -> Vacina:
    vacina = Vacina(**payload.model_dump())
    db.add(vacina)
    db.commit()
    db.refresh(vacina)
    return vacina


@router.get("/vacinas", response_model=list[VacinaRead])
def list_vacinas(db: Session = Depends(get_db)) -> list[Vacina]:
    return list(db.scalars(select(Vacina).order_by(Vacina.nome_comercial)).all())
