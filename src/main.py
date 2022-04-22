from fastapi import FastAPI
from .questdb_instance import QuestDB

app = FastAPI()


@app.get("/")
async def get_all_status():
    return {"message": "All questDB instances"}


@app.get("/{name}")
async def get_status_by_name(name: str):
    return {"message": f"Status {name}"}


@app.delete("/{name}")
async def delete(name: str):
    return {"message": f"Deleted {name}"}


@app.post("/")
async def create(questdb: QuestDB):
    return {"message": f"Created {questdb.name}"}