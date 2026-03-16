# BD-Vacina

Projeto full-stack para digitalizacao do comprovante de vacinacao do adulto.

## Stack

- Mobile: React Native + Expo + TypeScript + React Navigation + Zustand + Axios
- API: FastAPI + SQLAlchemy 2.0 + Pydantic + Alembic
- Banco: MySQL 8.0
- Infra local: Docker Compose

## Estrutura

```text
BD-Vacina/
  backend/
    app/
      database/
      models/
      routes/
      schemas/
      main.py
    alembic/
    alembic.ini
    Dockerfile
    requirements.txt
  mobile/
    src/
      components/
      navigation/
      screens/
      services/
      store/
      types/
    App.tsx
  docker-compose.yml
```

## 1) Subir backend + MySQL com Docker

Na raiz do projeto:

```bash
docker compose up --build
```

Servicos disponiveis:

- MySQL: `localhost:3306`
- API FastAPI: `http://localhost:8000`
- Docs Swagger: `http://localhost:8000/docs`

A API executa `alembic upgrade head` automaticamente ao iniciar o container.

## 2) Rodar app mobile (Expo)

Em outro terminal:

```bash
cd mobile
npm install
npm run start
```

Para abrir em plataforma especifica:

```bash
npm run android
npm run ios
```

### Base URL da API no mobile

Arquivo: `mobile/src/services/api.ts`

Regra padrao:

- Android Emulator: `http://10.0.2.2:8000/api/v1`
- iOS Simulator: `http://localhost:8000/api/v1`

Opcionalmente, defina em `mobile/.env`:

```env
EXPO_PUBLIC_API_URL=http://SEU_IP_LOCAL:8000/api/v1
```

Use essa opcao para dispositivo fisico.

## 3) Endpoints principais

Base: `/api/v1`

### Cadastros base

- `POST /pacientes`
- `GET /pacientes`
- `POST /vacinas`
- `GET /vacinas`

### Registro de vacinacao (CRUD)

- `POST /registros`
- `GET /registros`
- `GET /registros/{registro_id}`
- `PUT /registros/{registro_id}`
- `DELETE /registros/{registro_id}`

### Historico do paciente

- `GET /pacientes/{paciente_id}/historico`

## 4) Exemplo rapido de fluxo (curl)

Criar paciente:

```bash
curl -X POST "http://localhost:8000/api/v1/pacientes" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Maria Oliveira",
    "cpf": "12345678901",
    "data_nascimento": "1985-04-12"
  }'
```

Criar vacina:

```bash
curl -X POST "http://localhost:8000/api/v1/vacinas" \
  -H "Content-Type: application/json" \
  -d '{
    "nome_comercial": "Influvac",
    "grupo_doenca": "Influenza"
  }'
```

Criar registro:

```bash
curl -X POST "http://localhost:8000/api/v1/registros" \
  -H "Content-Type: application/json" \
  -d '{
    "id_paciente": 1,
    "id_vacina": 1,
    "numero_dose": 1,
    "data_aplicacao": "2026-03-01",
    "lote": "L202603",
    "nome_vacinador": "Enf. Carlos"
  }'
```

Consultar historico:

```bash
curl "http://localhost:8000/api/v1/pacientes/1/historico"
```

## 5) Observacoes de qualidade

- Separacao por camadas (`models`, `schemas`, `routes`, `database`)
- Validacao de entrada com Pydantic
- ORM SQLAlchemy 2.0 com tipagem forte
- Migracoes versionadas com Alembic
- Estado no app centralizado com Zustand
