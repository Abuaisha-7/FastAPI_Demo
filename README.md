# FastAPI Demo

✅ **A minimal FastAPI example demonstrating a small backend with users, images, and database integration.**

---

## 🔧 Quick overview

- **Framework:** FastAPI
- **Purpose:** Demo project for learning FastAPI basics — routing, schemas, DB access, and serving images.
- **Runserver:** Uvicorn (development with `--reload`)

---

## 🧰 Tech stack

- **Python:** 3.10+
- **Web framework:** FastAPI
- **ASGI server:** Uvicorn
- **Validation:** Pydantic
- **Database:** SQLite / SQLAlchemy (see `app/db.py`) — replace with PostgreSQL or another DB for production
- **Testing:** pytest (recommended)

---

## 🚀 Setup (local)

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows PowerShell: .venv\Scripts\Activate.ps1
```

2. Install dependencies (this project uses `pyproject.toml`):

```bash
# If you use pip + setuptools
pip install -e .

# Or, if you have a requirements file, you can run:
pip install -r requirements.txt  # (if present)
```

3. Copy environment variables:

```bash
cp example.env .env   # or create .env based on example.env and fill any secrets
```

4. Start the development server:

```bash
uvicorn main:app --reload
```

Open your browser at: http://127.0.0.1:8000

---

## 📚 API documentation

FastAPI auto-generates interactive OpenAPI docs:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## 🔎 Key files

- `main.py` — app entrypoint
- `frontend.py` — (if present) simple frontend or static demo
- `app/` — application modules
  - `app.py` — app factory or additional routes
  - `db.py` — database utilities
  - `users.py`, `schemas.py` — user routes and Pydantic schemas
  - `images.py` — image upload/serve logic

---

## ✅ Contributing & development tips

- Keep code small and focused — this is a learning repo.
- Use the interactive docs to inspect available endpoints and test payloads.

---

## 📄 License

This repository does not include a license by default — add one if you plan to share or publish.

---

