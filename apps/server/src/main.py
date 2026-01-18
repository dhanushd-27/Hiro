from fastapi import FastAPI
from src.api.v1.health import router as health_router
from src.core.lifespan import lifespan

app = FastAPI(
    lifespan=lifespan
)

app.include_router(health_router)

@app.get("/")
def main():
    return {"message": "Hello World"}