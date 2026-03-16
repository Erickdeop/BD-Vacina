"""create initial tables

Revision ID: 20260315_0001
Revises:
Create Date: 2026-03-15
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "20260315_0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pacientes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sa.String(length=120), nullable=False),
        sa.Column("cpf", sa.String(length=14), nullable=False),
        sa.Column("data_nascimento", sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_pacientes_cpf"), "pacientes", ["cpf"], unique=True)
    op.create_index(op.f("ix_pacientes_id"), "pacientes", ["id"], unique=False)

    op.create_table(
        "vacinas",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome_comercial", sa.String(length=120), nullable=False),
        sa.Column("grupo_doenca", sa.String(length=120), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_vacinas_id"), "vacinas", ["id"], unique=False)

    op.create_table(
        "registros_vacinacao",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("id_paciente", sa.Integer(), nullable=False),
        sa.Column("id_vacina", sa.Integer(), nullable=False),
        sa.Column("numero_dose", sa.Integer(), nullable=False),
        sa.Column("data_aplicacao", sa.Date(), nullable=False),
        sa.Column("lote", sa.String(length=50), nullable=False),
        sa.Column("nome_vacinador", sa.String(length=120), nullable=False),
        sa.ForeignKeyConstraint(["id_paciente"], ["pacientes.id"]),
        sa.ForeignKeyConstraint(["id_vacina"], ["vacinas.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_registros_vacinacao_id"), "registros_vacinacao", ["id"], unique=False)
    op.create_index(
        op.f("ix_registros_vacinacao_id_paciente"), "registros_vacinacao", ["id_paciente"], unique=False
    )
    op.create_index(
        op.f("ix_registros_vacinacao_id_vacina"), "registros_vacinacao", ["id_vacina"], unique=False
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_registros_vacinacao_id_vacina"), table_name="registros_vacinacao")
    op.drop_index(op.f("ix_registros_vacinacao_id_paciente"), table_name="registros_vacinacao")
    op.drop_index(op.f("ix_registros_vacinacao_id"), table_name="registros_vacinacao")
    op.drop_table("registros_vacinacao")

    op.drop_index(op.f("ix_vacinas_id"), table_name="vacinas")
    op.drop_table("vacinas")

    op.drop_index(op.f("ix_pacientes_id"), table_name="pacientes")
    op.drop_index(op.f("ix_pacientes_cpf"), table_name="pacientes")
    op.drop_table("pacientes")
