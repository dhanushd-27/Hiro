from fastapi import FastAPI
from src.api.v1.health import router as health_router

app = FastAPI()

app.include_router(health_router)

@app.get("/")
def main():
    return {"message": "Hello World"}