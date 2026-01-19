from app.core.security import hash_password, verify_password
from app.models.user import user_helper

async def create_user(db, user):
    existing = await db.users.find_one({"email": user.email})
    if existing:
        return None

    new_user = {
        "email": user.email,
        "hashed_password": hash_password(user.password),
    }
    result = await db.users.insert_one(new_user)
    created = await db.users.find_one({"_id": result.inserted_id})
    return user_helper(created)

async def authenticate_user(db, email: str, password: str):
    user = await db.users.find_one({"email": email})
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return user
