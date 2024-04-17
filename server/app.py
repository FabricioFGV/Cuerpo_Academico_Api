from fastapi import FastAPI
from server.routes.integrante import router as IntegranteRouter
from server.routes.proyecto import router as ProyectoRouter
from server.routes.eventos import router as EventoRouter
from server.routes.login import router as loginRouter

app = FastAPI()

app.include_router(IntegranteRouter, tags=["Integrante"], prefix="/integrante")
app.include_router(ProyectoRouter, tags=["Proyecto"], prefix="/proyecto")
app.include_router(EventoRouter, tags=["Evento"], prefix="/evento")
app.include_router(loginRouter, tags=["Login"], prefix="/login")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Inicio de la api"}
