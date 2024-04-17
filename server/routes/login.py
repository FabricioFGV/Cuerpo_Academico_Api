from fastapi import APIRouter
from server.database import authenticate_user
from server.models.eventos import ErrorResponseModel, ResponseModel
from server.models.login import LoginSchema

router = APIRouter()

# Agrega la siguiente ruta para autenticar un estudiante por matrícula y contraseña
@router.post("/login", response_description="Student authentication")
async def authenticate_student(login: LoginSchema):
    user = await authenticate_user(login.matricula, login.contrasenia)
    if user:
        return ResponseModel(user, "Authentication successful.")
    return ErrorResponseModel("Invalid credentials", 401, "Invalid matricula or password.")
