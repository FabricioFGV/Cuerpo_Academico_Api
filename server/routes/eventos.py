from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import (
    add_evento,
    delete_evento,
    retrieve_evento,
    retrieve_evento,
    update_evento,
)
from server.models.eventos import (
    ErrorResponseModel,
    EventoSchema,
    ResponseModel,
    UpdateEventoModel,
)

router = APIRouter()

@router.post("/", response_description="Evento data added into the database")
async def add_evento_data(evento: EventoSchema = Body(...)):
    evento = jsonable_encoder(evento)
    new_evento = await add_evento(evento)
    return ResponseModel(new_evento, "Evento added successfully.")

@router.get("/", response_description="Eventos retrieved")
async def get_eventos():
    eventos = await retrieve_evento()
    if eventos:
        return ResponseModel(eventos, "Eventos data retrieved successfully")
    return ResponseModel(eventos, "Empty list returned")

@router.get("/{nombre}", response_description="Evento data retrieved")
async def get_evento_data(nombre: str):
    evento = await retrieve_evento(nombre)
    if evento:
        return ResponseModel(evento, "Evento data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Evento doesn't exist.")

@router.put("/{nombre}")
async def update_evento_data(nombre: str, req: UpdateEventoModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_evento = await update_evento(nombre, req)
    if updated_evento:
        return ResponseModel(
            "Evento with nombre: {} update is successful".format(nombre),
            "Evento updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the evento data.",
    )

@router.delete("/{nombre}", response_description="Evento data deleted from the database")
async def delete_evento_data(nombre: str):
    deleted_evento = await delete_evento(nombre)
    if deleted_evento:
        return ResponseModel(
            "Evento with nombre: {} removed".format(nombre), "Evento deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Evento with nombre {0} doesn't exist".format(nombre)
    )
