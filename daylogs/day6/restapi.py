from fastapi import FastAPI, HTTPException
app = FastAPI(title="User API", version="v1")
users = {}
@app.post("/api/v1/users", status_code=201)
def create_user(user_id: int, name: str):
 if user_id in users:
    raise HTTPException(status_code=400, detail="User exists")
 users[user_id] = name
 return {"id": user_id, "name": name}


@app.get("/api/v1/users/{user_id}")
def get_user(user_id: int):
 if user_id not in users:
    raise HTTPException(status_code=404, detail="User not found")
 return {"id": user_id, "name": users[user_id]}
 
