import uvicorn
from consulta import consulta
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/search")
def search(query: str):
    return consulta(query)


uvicorn.run(app, host="0.0.0.0", port=8000)
