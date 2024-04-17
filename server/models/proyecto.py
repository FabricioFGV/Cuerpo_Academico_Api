from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date

class ProyectoSchema(BaseModel):
    titulo: str = Field(...)
    descripcion: str = Field(...)
    contenido: str = Field(...)
    fecha_inicio: date = Field(...)
    fecha_conclusion: date = Field(...)
    estado_proyecto: str = Field(...)
    participacion: List[str] = Field(...)

class UpdateProyectoModel(BaseModel):
    descripcion: Optional[str]
    contenido: Optional[str]
    fecha_inicio: Optional[date]
    fecha_conclusion: Optional[date]
    estado_proyecto: Optional[str]
    participacion: Optional[List[str]]

# Función utilitaria para construir una respuesta exitosa
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

# Función utilitaria para construir una respuesta de error
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
