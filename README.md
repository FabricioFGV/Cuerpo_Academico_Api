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

  ```bash Instalacion
  pip install -r requirements.txt
  ```

3. Iniciar la api

  ```bash Instalacion
  python main.py
  ```

4. Documentación
Inicada la API, para ir a la documentación de Fast Api en el navegador web deberas usar la siguiente dirección:

   http://localhost:8000/docs

5. Estructura del proyecto

 ```
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
 ```

6. Dependencias

Dependecias usadas en requirements.txt

| Dependencia          | Versión  |
|----------------------|----------|
| motor                | 3.2.0    |
| uvicorn              |          |
| fastapi              | 0.100.0  |
| pydantic[email]      | 2.0.3    |
| python-decouple      | 3.8      |

#Viculo pagina React

https://codesandbox.io/p/sandbox/cuerpo-academico-forked-8n7x9v?file=%2Fsrc%2Fcomponents%2FUsuario.js&layout=%257B%2522sidebarPanel%2522%253A%2522EXPLORER%2522%252C%2522rootPanelGroup%2522%253A%257B%2522direction%2522%253A%2522horizontal%2522%252C%2522contentType%2522%253A%2522UNKNOWN%2522%252C%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522id%2522%253A%2522ROOT_LAYOUT%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522UNKNOWN%2522%252C%2522direction%2522%253A%2522vertical%2522%252C%2522id%2522%253A%2522clv42b0lr00063j6gsu4ipkjm%2522%252C%2522sizes%2522%253A%255B100%252C0%255D%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522EDITOR%2522%252C%2522direction%2522%253A%2522horizontal%2522%252C%2522id%2522%253A%2522EDITOR%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522EDITOR%2522%252C%2522id%2522%253A%2522clv42b0lr00023j6gw92rnhef%2522%257D%255D%257D%252C%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522SHELLS%2522%252C%2522direction%2522%253A%2522horizontal%2522%252C%2522id%2522%253A%2522SHELLS%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522SHELLS%2522%252C%2522id%2522%253A%2522clv42b0lr00033j6gq0bn30f4%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%255D%257D%252C%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522DEVTOOLS%2522%252C%2522direction%2522%253A%2522vertical%2522%252C%2522id%2522%253A%2522DEVTOOLS%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522DEVTOOLS%2522%252C%2522id%2522%253A%2522clv42b0lr00053j6gegacyx1o%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%255D%252C%2522sizes%2522%253A%255B50%252C50%255D%257D%252C%2522tabbedPanels%2522%253A%257B%2522clv42b0lr00023j6gw92rnhef%2522%253A%257B%2522tabs%2522%253A%255B%257B%2522id%2522%253A%2522clv42b0lq00013j6g3n2pu5un%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522FILE%2522%252C%2522filepath%2522%253A%2522%252Fsrc%252Findex.js%2522%252C%2522state%2522%253A%2522IDLE%2522%252C%2522initialSelections%2522%253A%255B%257B%2522startLineNumber%2522%253A7%252C%2522startColumn%2522%253A25%252C%2522endLineNumber%2522%253A7%252C%2522endColumn%2522%253A25%257D%255D%257D%252C%257B%2522id%2522%253A%2522clv5un91r00023j6gkxknnb8i%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522FILE%2522%252C%2522filepath%2522%253A%2522%252Fsrc%252Fcomponents%252FNewPost.js%2522%252C%2522state%2522%253A%2522IDLE%2522%257D%252C%257B%2522id%2522%253A%2522clva5fz3p00023j6g2iemc6xn%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522FILE%2522%252C%2522filepath%2522%253A%2522%252Fsrc%252Fcomponents%252FUsuario.js%2522%252C%2522state%2522%253A%2522IDLE%2522%257D%255D%252C%2522id%2522%253A%2522clv42b0lr00023j6gw92rnhef%2522%252C%2522activeTabId%2522%253A%2522clva5fz3p00023j6g2iemc6xn%2522%257D%252C%2522clv42b0lr00053j6gegacyx1o%2522%253A%257B%2522tabs%2522%253A%255B%257B%2522id%2522%253A%2522clv42b0lr00043j6g306qnyx9%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522UNASSIGNED_PORT%2522%252C%2522port%2522%253A0%252C%2522path%2522%253A%2522%252FOnePublic%2522%257D%255D%252C%2522id%2522%253A%2522clv42b0lr00053j6gegacyx1o%2522%252C%2522activeTabId%2522%253A%2522clv42b0lr00043j6g306qnyx9%2522%257D%252C%2522clv42b0lr00033j6gq0bn30f4%2522%253A%257B%2522tabs%2522%253A%255B%255D%252C%2522id%2522%253A%2522clv42b0lr00033j6gq0bn30f4%2522%257D%257D%252C%2522showDevtools%2522%253Atrue%252C%2522showShells%2522%253Afalse%252C%2522showSidebar%2522%253Atrue%252C%2522sidebarPanelSize%2522%253A15%257D
