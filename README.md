# FastAPI Quiz Backend (Complete Template)

## Features
- FastAPI backend with JWT auth (register/login)
- Question CRUD (admin-protected endpoint) and public endpoints to get questions
- Quiz submission endpoint scoring by question id
- SQLite by default for local development; supports PostgreSQL via DATABASE_URL env var
- Configurable via `.env` or environment variables

## Quickstart (local)
1. Create a virtualenv and install dependencies:
   ```bash
   pytho3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and edit values if needed.
3. Run:
   ```bash
   uvicorn main:app --reload
   ```
4. Open docs: http://127.0.0.1:8000/docs

## Deployment
- For Railway + Supabase, set `DATABASE_URL` to your Supabase connection string and `SECRET_KEY` to a random value.


copilot - CMD + I


copilot chat - CMD Opt B


brew install postgresql@15
brew services start postgresql@15
psql -d postgres -U your_mac_username

# Connect as the postgres user
psql -U postgres
# Inside the psql shell, run these commands
CREATE DATABASE my_new_db;
CREATE USER my_new_user WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE my_new_db TO my_new_user;
\q # to quit

psql -U my_new_user -d my_new_db