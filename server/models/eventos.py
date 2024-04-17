from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class EventoSchema(BaseModel):
    nombre: str = Field(...)
    descripcion: str = Field(...)
    fecha_inicio: datetime = Field(...)
    fecha_termino: datetime = Field(...)

class UpdateEventoModel(BaseModel):
    descripcion: Optional[str]
    fecha_inicio: Optional[datetime]
    fecha_termino: Optional[datetime]



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
