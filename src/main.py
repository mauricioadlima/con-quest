from fastapi import FastAPI, Response, status
from kubernetes import client
from questdb import QuestDB
from k8s import K8s

app = FastAPI()
k8s = K8s()


@app.post("/")
async def create(questdb: QuestDB, response: Response):
    try:
        k8s.create(questdb)
        return {"message": f"Instance {questdb.namespace}/{questdb.name} created with success."}
    except client.exceptions.ApiException as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": f"Fail to create {questdb.namespace}/{questdb.name}.", "reason": f"{e.reason}"}


@app.get("/{namespace}/{name}")
async def get_status_by_name(namespace: str, name: str):
    sts = k8s.get_status(namespace, name)
    return {"status": {sts}}


@app.delete("/{namespace}/{name}")
async def delete(namespace: str, name: str, response: Response):
    try:
        k8s.delete(namespace, name)
        return {"message": f"Instance {namespace}/{name} deleted with success."}
    except client.exceptions.ApiException as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": f"Fail to delete {questdb.namespace}/{questdb.name}.", "reason": f"{e.reason}"}
