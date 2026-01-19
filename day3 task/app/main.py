from fastapi import FastAPI
from app.api.routes import auth, user

app = FastAPI(title="FastAPI MongoDB OAuth2")

app.include_router(auth.router)
app.include_router(user.router)
