import uvicorn

# Verifica si el script se está ejecutando como el programa principal
if __name__ == "__main__":
    # Ejecuta la aplicación FastAPI usando uvicorn
    # El argumento "server.app:app" indica que la aplicación se encuentra en el módulo "server.app" y se llama "app"
    # host="0.0.0.0" permite que la aplicación sea accesible desde cualquier dirección IP
    # port=8000 establece el puerto en el que la aplicación escucha las solicitudes
    # reload=True habilita la recarga automática cuando se realizan cambios en el código (solo para desarrollo)
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)
