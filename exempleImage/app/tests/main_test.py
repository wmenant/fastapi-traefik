import pytest
from httpx import AsyncClient
import os
os.remove('test.db')
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from app.db import User
from app.main import app

# @pytest.fixture(scope='function')
# async def setup():
#     await app.router.startup()
#     yield
#     await app.router.shutdown()

@pytest.mark.asyncio
async def test_read_root():
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await app.router.startup()
        response = await ac.get("/")
        await app.router.shutdown()
    assert response.status_code == 200
    users = response.json()
    assert any(user["email"] == "test@test.com" for user in users), 'user not found'


async def createUser(user):
    async with AsyncClient(app=app, base_url="http://test") as client:
        return await client.post("/users/", json=user)
    
@pytest.mark.asyncio
async def test_create_user():
    response = await createUser({"email": "newuser@test.com", "active": True})
    assert response.status_code == 200
    data = response.json()
    assert data['email'] == "newuser@test.com"
    assert data['active'] == True

@pytest.mark.asyncio
async def test_update_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.patch("/users/newuser@test.com", json={"email": "updateduser@test.com"})
    assert response.status_code == 200
    data = response.json()
    assert data['email'] == "updateduser@test.com"

@pytest.mark.asyncio
async def test_delete_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.delete("/users/updateduser@test.com")
    assert response.status_code == 200
    data = response.json()
    assert data['detail'] == "User deleted successfully"
