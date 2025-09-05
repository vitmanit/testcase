from fastapi import FastAPI
from app.routers import answer, question

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "My test-task"}


app.include_router(answer.router)
app.include_router(question.router)
