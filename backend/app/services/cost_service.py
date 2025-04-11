from app.database.connection import collection
from app.models.cost import Cost
from typing import List
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
from fastapi import HTTPException
from bson import ObjectId


async def add_cost(custo: Cost):
    result = await collection["costs"].insert_one(custo.model_dump(exclude={"id"}))
    
    custo.id = str(result.inserted_id)
    return custo


async def list_costs() -> List[Cost]:
    costs = await collection.find({}, {"_id": 1}).to_list(100)
    return [Cost(**{**cost, "id": str(cost["_id"])}) for cost in costs]

async def delete_cost(cost_id: str):
    result = await collection.delete_one({"_id": ObjectId(cost_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code = 404, detail='Não encontrado')
    
    return{"message", "Deletado"}


async def analysys_cost():
    costs = await collection.find({}, {"_id": 0}).to_list(1000)
    if not costs:
        return None

    for cost in costs:
        cost["_id"] = str(cost.get("_id", ""))

    df = pd.DataFrame(costs)
    resume = df.groupby("categoria")["valor"].sum().to_dict()
    
    df_resume = pd.DataFrame(resume.items(), columns=["Categoria", "Valor"])
    plt.figure(figsize=(19, 10))
    sns.barplot(x="Categoria", y="Valor", data=df_resume, palette="Blues_d")
    plt.title("Resumo dos Custos por Categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Valor Total")

    img = BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()

    return img


