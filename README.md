# Stream AI Backend (FastAPI)

Refactored to a domain-driven `src/` layout with separate module routes/controllers/services.

## Structure
- `src/core`: shared config, middleware, utils, database bootstrap.
- `src/modules`: identity, camera, zone, notification, dashboard domains.

## Features
- JWT auth: `POST /auth/token`
- Global rate limiting: `slowapi`
- Redis cache for read-heavy endpoints

## Run
```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```
