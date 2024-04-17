from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import (
    add_proyecto,
    delete_proyecto,
    retrieve_proyecto,
    retrieve_proyectos,
    update_proyecto,
)
from server.models.proyecto import (
    ErrorResponseModel,
    ProyectoSchema,
    ResponseModel,
    UpdateProyectoModel,
)

router = APIRouter()

@router.post("/", response_description="Proyecto data added into the database")
async def add_proyecto_data(proyecto: ProyectoSchema = Body(...)):
    proyecto = jsonable_encoder(proyecto)
    new_proyecto = await add_proyecto(proyecto)
    return ResponseModel(new_proyecto, "Proyecto added successfully.")

@router.get("/", response_description="Proyectos retrieved")
async def get_proyectos():
    proyectos = await retrieve_proyectos()
    if proyectos:
        return ResponseModel(proyectos, "Proyectos data retrieved successfully")
    return ResponseModel(proyectos, "Empty list returned")

@router.get("/{titulo}", response_description="Proyecto data retrieved")
async def get_proyecto_data(titulo: str):
    proyecto = await retrieve_proyecto(titulo)
    if proyecto:
        return ResponseModel(proyecto, "Proyecto data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Proyecto doesn't exist.")

@router.put("/{titulo}")
async def update_proyecto_data(titulo: str, req: UpdateProyectoModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_proyecto = await update_proyecto(titulo, req)
    if updated_proyecto:
        return ResponseModel(
            "Proyecto with titulo: {} update is successful".format(titulo),
            "Proyecto updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the proyecto data.",
    )

@router.delete("/{titulo}", response_description="Proyecto data deleted from the database")
async def delete_proyecto_data(titulo: str):
    deleted_proyecto = await delete_proyecto(titulo)
    if deleted_proyecto:
        return ResponseModel(
            "Proyecto with titulo: {} removed".format(titulo), "Proyecto deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Proyecto with titulo {0} doesn't exist".format(titulo)
    )
