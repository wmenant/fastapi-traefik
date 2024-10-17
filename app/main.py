from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.db import database, User


app = FastAPI(title="FastAPI, Docker, and Traefik")

class UserModel(BaseModel):
    email: str = None
    active: bool = None


@app.get("/")
async def read_root():
    return await User.objects.all()

@app.post("/users/", response_model=UserModel)
async def create_user(user: UserModel):
    existing_user = await User.objects.get_or_none(email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await User.objects.create(**user.dict())
    return new_user

@app.patch("/users/{email}", response_model=UserModel)
async def update_user(email: str, user: UserModel):
    db_user = await User.objects.get_or_none(email=email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.dict(exclude_unset=True)
    updated_user = await db_user.update(**user_data)
    return updated_user

@app.delete("/users/{email}", response_model=dict)
async def delete_user(email: str):
    db_user = await User.objects.get_or_none(email=email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    await db_user.delete()
    return {"detail": "User deleted successfully"}


@app.on_event("startup")
async def startup():
    print('je suis dans startup')
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
