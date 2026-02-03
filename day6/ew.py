import strawberry
from typing import List, Optional
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# -------------------------
# GraphQL Types
# -------------------------

@strawberry.type
class User:
    id: int
    name: str
    email: str


# In-memory database
users: List[User] = []


# -------------------------
# Queries
# -------------------------

@strawberry.type
class Query:

    @strawberry.field
    def users(self) -> List[User]:
        return users

    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        return next((u for u in users if u.id == id), None)

    @strawberry.field
    def user_count(self) -> int:
        return len(users)

    @strawberry.field
    def health(self) -> str:
        return "OK"

    @strawberry.field
    def version(self) -> str:
        return "1.0"


# -------------------------
# Mutations
# -------------------------

@strawberry.type
class Mutation:

    @strawberry.field
    def create_user(self, name: str, email: str) -> User:
        user = User(id=len(users) + 1, name=name, email=email)
        users.append(user)
        return user

    @strawberry.field
    def update_user(self, id: int, name: Optional[str] = None) -> User:
        user = next(u for u in users if u.id == id)
        if name:
            user.name = name
        return user

    @strawberry.field
    def delete_user(self, id: int) -> bool:
        global users
        users = [u for u in users if u.id != id]
        return True


# -------------------------
# Schema + App
# -------------------------

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI(title="GraphQL User API")

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
