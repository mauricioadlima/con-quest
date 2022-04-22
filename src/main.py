from fastapi import FastAPI, Response, status
from kubernetes import client
from questdb import QuestDB
from k8s import K8s

app = FastAPI()
k8s = K8s()


@app.get("/{namespace}/{name}")
async def get_status_by_name(namespace: str, name: str):
    sts = k8s.get_status(namespace, name)
    return {"status": {sts}}


@app.delete("/{namespace}/{name}")
async def delete(name: str):
    return {"message": f"Deleted {name}"}


@app.post("/")
async def create(questdb: QuestDB, response: Response):
    try:
        k8s.create(questdb)
        return {"message": f"QuestDB {questdb.name} created with success."}
    except client.exceptions.ApiException as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": f"Fail to create QuestDB with {questdb.name}.", "reason": f"{e.reason}"}

