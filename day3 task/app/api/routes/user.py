from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import create_user
from app.api.deps import get_current_user
from app.core.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
async def register(user: UserCreate, db = Depends(get_db)):
    created = await create_user(db, user)
    if not created:
        raise HTTPException(status_code=400, detail="Email already exists")
    return created

@router.get("/me")
async def read_me(current_user = Depends(get_current_user)):
    return current_user
