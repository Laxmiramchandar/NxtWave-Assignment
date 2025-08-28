from fastapi import FastAPI
from .recipes import router as recipes_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe API! Visit /docs for API documentation."}

app.include_router(recipes_router, prefix="/api/recipes", tags=["recipes"])
