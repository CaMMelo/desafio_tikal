import uvicorn
from consulta import consulta
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def search(query: str):
    return consulta(query)


uvicorn.run(app, host="127.0.0.1", port=8000)
