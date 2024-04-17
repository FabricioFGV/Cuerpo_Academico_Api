from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import (
    add_integrante,
    delete_integrante,
    retrieve_integrante,
    retrieve_integrantes,
    update_integrante,
)
from server.models.integrante import (
    ErrorResponseModel,
    IntegranteSchema,
    ResponseModel,
)

router = APIRouter()

@router.post("/", response_description="Integrante data added into the database")
async def add_integrante_data(integrante: IntegranteSchema = Body(...)):
    integrante = jsonable_encoder(integrante)
    new_integrante = await add_integrante(integrante)
    return ResponseModel(new_integrante, "Integrante added successfully.")

@router.get("/", response_description="Integrantes retrieved")
async def get_integrantes():
    integrantes = await retrieve_integrantes()
    if integrantes:
        return ResponseModel(integrantes, "Integrantes data retrieved successfully")
    return ResponseModel(integrantes, "Empty list returned")

@router.get("/{matricula}", response_description="Integrante data retrieved")
async def get_integrante_data(matricula: str):
    integrante = await retrieve_integrante(matricula)
    if integrante:
        return ResponseModel(integrante, "Integrante data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Integrante doesn't exist.")

@router.put("/{matricula}")
async def update_integrante_data(matricula: str, req: IntegranteSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_integrante = await update_integrante(matricula, req)
    if updated_integrante:
        return ResponseModel(
            "Integrante with matrícula: {} update is successful".format(matricula),
            "Integrante data updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the integrante data.",
    )

@router.delete("/{matricula}", response_description="Integrante data deleted from the database")
async def delete_integrante_data(matricula: str):
    deleted_integrante = await delete_integrante(matricula)
    if deleted_integrante:
        return ResponseModel(
            "Integrante with matrícula: {} removed".format(matricula),
            "Integrante deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Integrante with matrícula {0} doesn't exist".format(matricula)
    )
