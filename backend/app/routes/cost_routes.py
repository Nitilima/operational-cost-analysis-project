from fastapi import APIRouter, HTTPException
from app.models.cost import Cost
from app.services.cost_service import add_cost, list_costs, analysys_cost, delete_cost
from fastapi.responses import StreamingResponse

router = APIRouter()


@router.post("/custos", status_code=201)
async def create_cost(cost: Cost):
    await add_cost(cost)
    return {"message": "Custo adicionado"}

@router.delete("/custos/{cost_id}")
async def del_cost(cost_id: str):
    return await delete_cost(cost_id)

@router.get("/costs")
async def get_costs():
    costs = await list_costs()
    return costs


@router.get("/analysys")
async def get_analysys():
    img = await analysys_cost()
    if not img:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado")
    
    return StreamingResponse(img, media_type="image/png")
