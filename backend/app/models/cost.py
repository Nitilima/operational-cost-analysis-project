from pydantic import BaseModel

class Cost(BaseModel):
    categoria: str
    descricao: str
    valor: float
    data: str