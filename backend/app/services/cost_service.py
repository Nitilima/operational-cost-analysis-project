from app.database.connection import collection
from app.models.cost import Cost
from typing import List
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO


async def add_cost(custo: Cost):
    await collection.insert_one(custo.model_dump())


async def list_costs() -> List[Cost]:
    costs = await collection.find({}, {"_id": 0}).to_list(100)
    return costs


async def analysys_cost():
    costs = await collection.find({}, {"_id": 0}).to_list(1000)
    if not costs:
        return None

    for cost in costs:
        cost["_id"] = str(cost.get("_id", ""))

    df = pd.DataFrame(costs)
    resume = df.groupby("categoria")["valor"].sum().to_dict()
    
    df_resume = pd.DataFrame(resume.items(), columns=["Categoria", "Valor"])
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Categoria", y="Valor", data=df_resume, palette="Blues_d")
    plt.title("Resumo dos Custos por Categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Valor Total")

    img = BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()

    return img


