# Universidad Tecnológica de Xicotepec de Juárez
## Ingeniería en Desarrollo y Gestión de Software
### Fabricio Guzmán Vite
###  Api del cuerpo academico

![Banner-de-Twitch-Nubes-Gamer-Chica-Morado.png](https://i.postimg.cc/15q3LFXF/Banner-de-Twitch-Nubes-Gamer-Chica-Morado.png)

## Desarrollo de una de una plataforma para el cuerpo académico

## Descripción
La API Rest para el cuerpo académico es una plataforma que ofrece un conjunto de servicios para gestionar datos relacionados con el cuerpo academico de la Universidad de Xicotepec de Juárez. Esta API implementa las operaciones CRUD (Crear, Leer, Actualizar y Borrar) para interactuar con la base de datos y proporciona endpoints para realizar diversas acciones, cuales como registrar nuevos integrantes, consultar información existente, actualizar datos y eliminar registros. Su objetivo principal es facilitar la gestión de proyectos académicos y el seguimiento del progreso, promoviendo la colaboración y la transparencia en la universidad. La API está diseñada para integrarse con otras aplicaciones y sistemas dentro de la universidad, proporcionando una interfaz fácil de usar para acceder y manipular los datos del cuerpo académico de manera eficiente y segura.

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/api-cuerpo-academico.git

2. Instala las dependencias necesarias:

  ```Instalacion
  pip install -r requirements.txt
  ```

3. Iniciar la api

  ```Instalacion
  python main.py
  ```

4. Documentación
Inicada la API, para ir a la documentación de Fast Api en el navegador web deberas usar la siguiente dirección:

http://localhost:8000/docs

5. Estructura del proyecto

├── app
│   ├── __init__.py
│   ├── main.py
│   └── server
│       ├── app.py
│       ├── database.py
│       ├── models
│       │   ├── eventos.py
│       │   ├── integrante.py
│       │   ├── login.py
│       │   └── proyecto.py
│       └── routes
│           ├── eventos.py
│           ├── integrante.py
│           ├── login.py
│           └── proyecto.py
└── requirements.txt


6. Dependencias

Dependecias usadas en requirements.txt

motor
uvicorn
fastapi
pydantic
python-decouple


