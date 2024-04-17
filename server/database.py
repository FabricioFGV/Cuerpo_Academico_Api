import asyncio
import bcrypt
import motor.motor_asyncio
from bson.objectid import ObjectId
from pymongo import IndexModel, ASCENDING
from pymongo.errors import DuplicateKeyError

# Detalles de conexión a la base de datos MongoDB
#MONGO_DETAILS = "mongodb://0.0.0.0:27017"
MONGO_DETAILS = "mongodb+srv://FGV:.N1ufu5231@dbproyect.ybmliwl.mongodb.net/"

# Conexión a la base de datos MongoDB usando el cliente motor
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# Selecciona la base de datos "students" desde el cliente
database = client.students

# Obtiene la colección de integrantes desde la base de datos
integrante_collection = database.get_collection("integrantes_collection")
proyecto_collection = database.get_collection("proyectos_collection")
evento_collection = database.get_collection("evento_collection")
student_collection = database.get_collection("student_collection")

# Crea el índice único en el campo "matricula" si no existe para integrantes
async def create_integrante_indexes():
    index_model = IndexModel([("matricula", ASCENDING)], unique=True)
    await integrante_collection.create_indexes([index_model])

# Llama a la función para crear el índice al inicio de tu aplicación
async def initialize_integrantes():
    await create_integrante_indexes()

# Función de ayuda para convertir el formato del integrante
def integrante_helper(integrante) -> dict:
    return {
        "matricula": str(integrante["matricula"]),
        "password": integrante["password"],
        "nombre": integrante["nombre"],
        "apellidoP": integrante["apellidoP"],
        "apellidoM": integrante["apellidoM"],
        "fechaNacimiento": integrante["fechaNacimiento"],
        "rol": integrante["rol"],
        "areaEsp": integrante["areaEsp"],
        "email": integrante["email"],
    }



# Crea el índice único en el campo "titulo" si no existe para proyectos
async def create_proyecto_indexes():
    index_model = IndexModel([("titulo", ASCENDING)], unique=True)
    await proyecto_collection.create_indexes([index_model])

# Llama a la función para crear el índice al inicio de tu aplicación
async def initialize_proyectos():
    await create_proyecto_indexes()

# Función de ayuda para convertir el formato del proyecto
def proyecto_helper(proyecto) -> dict:
    return {
        "titulo": proyecto["titulo"],
        "descripcion": proyecto["descripcion"],
        "contenido": proyecto["contenido"],
        "fechaInicio": proyecto["fechaInicio"],
        "fechaConclusion": proyecto["fechaConclusion"],
        "estadoP": proyecto["estadoP"],
        "participacion": proyecto["participacion"],
    }

async def retrieve_proyectos():
    proyectos = []
    async for proyecto in proyecto_collection.find():
        proyectos.append(proyecto_helper(proyecto))
    return proyectos



# Crea el índice único en el campo "nombre" si no existe para evento
async def create_evento_indexes():
    index_model = IndexModel([("nombre", ASCENDING)], unique=True)
    await evento_collection.create_indexes([index_model])

# Llama a la función para crear el índice al inicio de tu aplicación
async def initialize_evento():
    await create_evento_indexes()

# Función de ayuda para convertir el formato del evento
def evento_helper(evento) -> dict:
    return {
        "nombre": evento["nombre"],
        "descripcion": evento["descripcion"],
        "fechaInicio": evento["fechaInicio"],
        "fechaTermino": evento["fechaTermino"],
    }

async def retrieve_evento():
    evento = []
    async for evento in evento_collection.find():
        evento.append(evento_helper(evento))
    return evento



user_collection = database.user_collection

async def create_indexes():
    index_model = IndexModel([("username", ASCENDING)], unique=True)
    await user_collection.create_indexes([index_model])

async def initialize():
    await create_indexes()

async def add_user(user_data: dict) -> dict:
    try:
        user = await user_collection.insert_one(user_data)
        new_user = await user_collection.find_one({"username": user_data["username"]})
        return {
            "username": new_user["username"],
            "hashed_password": new_user["hashed_password"],
        }
    except DuplicateKeyError:
        return {"error": "DuplicateKeyError", "message": "El usuario ya existe"}
    

# Función de ayuda para convertir el formato del estudiante
def student_helper(student) -> dict:
    return {
        "matricula": str(student["matricula"]),
        "password": student["password"],
    }

async def authenticate_user(matricula: str, contrasenia: str):
    student = await student_collection.find_one({"matricula": matricula})
    if student and bcrypt.checkpw(contrasenia.encode('utf-8'), student["password"].encode('utf-8')):
        return student_helper(student)
    return None


# Operaciones CRUD para integrantes

async def add_integrante(integrante_data: dict) -> dict:
    integrante = await integrante_collection.insert_one(integrante_data)
    new_integrante = await integrante_collection.find_one({"matricula": integrante_data["matricula"]})
    return integrante_helper(new_integrante)

async def retrieve_integrantes():
    integrantes = []
    async for integrante in integrante_collection.find():
        integrantes.append(integrante_helper(integrante))
    return integrantes

async def retrieve_integrante(matricula: str) -> dict:
    integrante = await integrante_collection.find_one({"matricula": matricula})
    if integrante:
        return integrante_helper(integrante)

async def update_integrante(matricula: str, data: dict):
    if len(data) < 1:
        return False
    integrante = await integrante_collection.find_one({"matricula": matricula})
    if integrante:
        updated_integrante = await integrante_collection.update_one(
            {"matricula": matricula}, {"$set": data}
        )
        if updated_integrante:
            return True
    return False

async def delete_integrante(matricula: str):
    integrante = await integrante_collection.find_one({"matricula": matricula})
    if integrante:
        await integrante_collection.delete_one({"matricula": matricula})
        return True
    return False

#Operaciones Crud de proyecto
async def add_proyecto(proyecto_data: dict) -> dict:
    try:
        proyecto = await proyecto_collection.insert_one(proyecto_data)
        new_proyecto = await proyecto_collection.find_one({"titulo": proyecto_data["titulo"]})
        return proyecto_helper(new_proyecto)
    except DuplicateKeyError:
        return {"error": "DuplicateKeyError", "message": "El proyecto ya existe"}

async def retrieve_proyecto(titulo: str) -> dict:
    proyecto = await proyecto_collection.find_one({"titulo": titulo})
    if proyecto:
        return proyecto_helper(proyecto)

async def update_proyecto(titulo: str, data: dict):
    if len(data) < 1:
        return False
    proyecto = await proyecto_collection.find_one({"titulo": titulo})
    if proyecto:
        updated_proyecto = await proyecto_collection.update_one(
            {"titulo": titulo}, {"$set": data}
        )
        if updated_proyecto:
            return True
        return False

async def delete_proyecto(titulo: str):
    proyecto = await proyecto_collection.find_one({"titulo": titulo})
    if proyecto:
        await proyecto_collection.delete_one({"titulo": titulo})
        return True
    


#Eventos Crud
async def add_evento(evento_data: dict) -> dict:
    try:
        evento = await evento_collection.insert_one(evento_data)
        new_evento = await evento_collection.find_one({"nombre": evento_data["nombre"]})
        return evento_helper(new_evento)
    except DuplicateKeyError:
        return {"error": "DuplicateKeyError", "message": "El evento ya existe"}

async def retrieve_evento(nombre: str) -> dict:
    evento = await evento_collection.find_one({"nombre": nombre})
    if evento:
        return evento_helper(evento)

async def update_evento(nombre: str, data: dict):
    if len(data) < 1:
        return False
    evento = await evento_collection.find_one({"nombre": nombre})
    if evento:
        updated_evento = await evento_collection.update_one(
            {"nombre": nombre}, {"$set": data}
        )
        if updated_evento:
            return True
        return False

async def delete_evento(nombre: str):
    evento = await evento_collection.find_one({"nombre": nombre})
    if evento:
        await evento_collection.delete_one({"nombre": nombre})
        return True


# Ejecuta la función de inicialización utilizando asyncio.run
if __name__ == "__main__":
    asyncio.run(initialize())
