from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId


class Cost(BaseModel):
    id: str = None
    categoria: str
    descricao: str
    valor: float
    data: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            ObjectId: str
        }
