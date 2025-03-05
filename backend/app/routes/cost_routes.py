from fastapi import APIRouter, HTTPException
from app.models.cost import Cost
from app.services.cost_service import add_cost, list_costs, analysys_cost

router = APIRouter()


@router.post("/custos", status_code=201)
async def create_cost(cost: Cost):
    await add_cost(cost)
    return {"message": "Custo adicionado"}


@router.get("/costs")
async def get_costs():
    return await list_costs()


@router.get("/analysys")
async def get_analysys():
    resume = await analysys_cost()
    if resume is None:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado")
    return {"resumo": resume}
