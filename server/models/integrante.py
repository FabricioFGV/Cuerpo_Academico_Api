from typing import Optional
from datetime import date
from pydantic import BaseModel, EmailStr, Field, validator
from enum import Enum
import bcrypt

class RolEnum(str, Enum):
    estudiante = "estudiante"
    maestro = "maestro"
    invitado = "invitado"

class IntegranteSchema(BaseModel):
    matricula: int = Field(...)
    password: str = Field(...)
    nombre: str = Field(...)
    apellidoP: str = Field(...)
    apellidoM: str = Field(...)
    fechaNacimiento: date = Field(...)
    rol: RolEnum = Field(...)
    areaEsp: str = Field(...)
    email: EmailStr = Field(...)

    
    class Config:
        json_schema_extra = {
            "example":{
                "matricula":"123456",
                "password":"1234",
                "nombre":"user",
                "apellidoP":"ApellidoP",
                "apellidoM":"ApellidoM",
                "fechaNacimiento":"2024-04-07",
                "rol":"estudiante",
                "areaEsp":"estudiante",
                "email":"user@x.com"
            }
        }

    # Método para hashear la contraseña
    @validator("password", pre=True, always=True)
    def hash_password(cls, v):
        return bcrypt.hashpw(v.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


class UpdateIntegranteModel(BaseModel):
    nombre: Optional[str]
    apellidoP: Optional[str]
    apellidoM: Optional[str]
    fechaNacimiento: Optional[date]
    rol: Optional[RolEnum]
    areaEsp: Optional[str]
    email: EmailStr = Optional[EmailStr]

    
    class Config:
        json_schema_extra = {
            "example":{
                "nombre":"user",
                "apellidoP":"ApellidoP",
                "apellidoM":"ApellidoM",
                "fechaNacimiento":"2024-04-07",
                "rol":"maestro",
                "areaEsp":"estudiante",
                "email":"user@x.com"
            }
        }


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
