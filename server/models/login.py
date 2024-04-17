from pydantic import BaseModel


class LoginSchema(BaseModel):
    matricula: str
    contrasenia: str
