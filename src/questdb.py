from pydantic import BaseModel


class QuestDB(BaseModel):
    name: str
    namespace: str
