# Stream AI Backend (FastAPI)

FastAPI scaffold implementing your listed service routes with:
- JWT bearer authentication (`/auth/token`)
- Global rate limiting via `slowapi`
- Redis caching for GET/FETCH endpoints

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Default login:
- username: `admin`
- password: `admin123`

## Notes
- This is a scaffold. Replace in-memory auth and placeholder handlers with DB-backed logic.
- Query params like `PageNumber`/`PageSize` are accepted by endpoints and can be read in handler implementations.
