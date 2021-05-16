from fastapi import FastAPI
from app.db import database, User


# https://testdriven.io/blog/fastapi-docker-traefik/

app = FastAPI(title="FastAPI, docker and Traefik")


@app.get("/")
async def read_root():
    print(id)
    # user = User.objects.filter(id == id).get()
    user = await User.objects.get(User.id == 1)
    print(user)
    return await user

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email='teste@teste.com', password='1234')

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
