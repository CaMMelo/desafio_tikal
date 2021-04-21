import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def search(query: str):
    return {"query": query}


uvicorn.run(app, host="localhost", port=8000)
