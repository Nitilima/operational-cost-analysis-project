from app.database.connection import collection
from app.models.cost import Cost
from typing import List


async def add_cost(custo: Cost):
    await collection.insert_one(custo.model_dump())


async def list_costs() -> List[Cost]:
    costs = await collection.find({}, {"id": 0}).to_list(100)
    return costs


async def analysys_cost():
    costs = await collection.find({}, {"_id": 0}).to_list(1000)
    if not costs:
        return None

    # Converte _id para string
    for cost in costs:
        cost["_id"] = str(cost["_id"])

    import pandas as pd
    df = pd.DataFrame(costs)
    resume = df.groupby("categoria")["valor"].sum().to_dict()
    return resume