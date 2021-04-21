import uvicorn
from fastapi import FastAPI

from desafio_tikal.msconsulta.consulta import consulta

app = FastAPI()


@app.get("/")
def search(query: str):
    return consulta(query)


uvicorn.run(app, host="localhost", port=8000)
