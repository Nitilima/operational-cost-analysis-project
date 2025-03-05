from fastapi import FastAPI
from app.routes.cost_routes import router

app = FastAPI()

# Registrar as rotas
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
