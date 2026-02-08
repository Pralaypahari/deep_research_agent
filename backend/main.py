from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.database import get_db
from backend.auth import hash_password, verify_password, create_token
from backend.api.research import router as research_router

app = FastAPI(
    title="Deepsync Backend",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db = get_db()
app.include_router(research_router, prefix="/research")

@app.get("/")
async def root():
    return {"status": "Backend running"}
@app.post("/auth/register")
def register(
    email: str = Form(...),
    password: str = Form(...)
):
    try:
        db.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (email, hash_password(password))
        )
        db.commit()
        return {"message": "Account created successfully"}
    except:
        raise HTTPException(status_code=400, detail="User already exists")


@app.post("/auth/login")
def login(
    email: str = Form(...),
    password: str = Form(...)
):
    user = db.execute(
        "SELECT * FROM users WHERE email = ?", (email,)
    ).fetchone()

    if not user or not verify_password(password, user[2]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(email)

    return {
        "message": "Login successful",
        "token": token
    }