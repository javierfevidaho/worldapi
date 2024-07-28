Este proyecto proporciona una API que permite gestionar información geográfica, incluyendo países y ciudades. La API está construida utilizando Django y ofrece endpoints para listar, recuperar, crear, actualizar y eliminar datos de países y ciudades.

Endpoints Disponibles
Países
Listar todos los países

URL: /api/countries/
Método: GET
Descripción: Devuelve una lista de todos los países.
Ejemplo de respuesta:

json
Copiar código
[
    {
        "id": 1,
        "name": "Andorra",
        "code": "AD"
    },
    {
        "id": 2,
        "name": "United Arab Emirates",
        "code": "AE"
    }
]
Obtener un país por ID

URL: /api/countries/{id}/
Método: GET
Descripción: Devuelve los detalles de un país específico por ID.
Ejemplo de respuesta:

json
Copiar código
{
    "id": 1,
    "name": "Andorra",
    "code": "AD"
}
Crear un nuevo país

URL: /api/countries/
Método: POST
Descripción: Crea un nuevo país.
Ejemplo de solicitud:

json
Copiar código
{
    "name": "Spain",
    "code": "ES"
}
Ejemplo de respuesta:

json
Copiar código
{
    "id": 3,
    "name": "Spain",
    "code": "ES"
}
Actualizar un país existente

URL: /api/countries/{id}/
Método: PUT
Descripción: Actualiza los detalles de un país existente.
Ejemplo de solicitud:

json
Copiar código
{
    "name": "Spain",
    "code": "ES"
}
Ejemplo de respuesta:

json
Copiar código
{
    "id": 3,
    "name": "Spain",
    "code": "ES"
}
Eliminar un país

URL: /api/countries/{id}/
Método: DELETE
Descripción: Elimina un país por su ID.
Ciudades
Listar todas las ciudades

URL: /api/cities/
Método: GET
Descripción: Devuelve una lista de todas las ciudades.
Ejemplo de respuesta:

json
Copiar código
[
    {
        "id": 1,
        "name": "Andorra la Vella",
        "country": {
            "id": 1,
            "name": "Andorra",
            "code": "AD"
        }
    },
    {
        "id": 2,
        "name": "Dubai",
        "country": {
            "id": 2,
            "name": "United Arab Emirates",
            "code": "AE"
        }
    }
]
Obtener una ciudad por ID

URL: /api/cities/{id}/
Método: GET
Descripción: Devuelve los detalles de una ciudad específica por ID.
Ejemplo de respuesta:

json
Copiar código
{
    "id": 1,
    "name": "Andorra la Vella",
    "country": {
        "id": 1,
        "name": "Andorra",
        "code": "AD"
    }
}
Crear una nueva ciudad

URL: /api/cities/
Método: POST
Descripción: Crea una nueva ciudad.
Ejemplo de solicitud:

json
Copiar código
{
    "name": "Madrid",
    "country": 3
}
Ejemplo de respuesta:

json
Copiar código
{
    "id": 3,
    "name": "Madrid",
    "country": {
        "id": 3,
        "name": "Spain",
        "code": "ES"
    }
}
Actualizar una ciudad existente

URL: /api/cities/{id}/
Método: PUT
Descripción: Actualiza los detalles de una ciudad existente.
Ejemplo de solicitud:

json
Copiar código
{
    "name": "Barcelona",
    "country": 3
}
Ejemplo de respuesta:

json
Copiar código
{
    "id": 3,
    "name": "Barcelona",
    "country": {
        "id": 3,
        "name": "Spain",
        "code": "ES"
    }
}
Eliminar una ciudad

URL: /api/cities/{id}/
Método: DELETE
Descripción: Elimina una ciudad por su ID.
Instalación y Configuración
Clonar el repositorio:

bash
Copiar código
git clone https://github.com/tu_usuario/worldapi.git
cd worldapi
Crear y activar un entorno virtual:

bash
Copiar código
python3 -m venv .venv
source .venv/bin/activate
Instalar las dependencias:

bash
Copiar código
pip install -r requirements.txt
Aplicar migraciones:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
Descargar y poblar la base de datos con los datos de países y ciudades:

bash
Copiar código
curl -o countryInfo.txt http://download.geonames.org/export/dump/countryInfo.txt
curl -o cities500.zip http://download.geonames.org/export/dump/cities500.zip
unzip cities500.zip
python manage.py shell < populate_db.py
Iniciar el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Uso de la API
Puedes utilizar herramientas como curl, Postman o cualquier cliente HTTP para interactuar con los endpoints de la API.

Ejemplo de solicitud curl para obtener la lista de países:
bash
Copiar código
curl -X GET http://localhost:8000/api/countries/
Ejemplo de solicitud curl para crear un nuevo país:
bash
Copiar código
curl -X POST http://localhost:8000/api/countries/ -H "Content-Type: application/json" -d '{"name": "Spain", "code": "ES"}'
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request en el repositorio de GitHub.

Licencia
Este proyecto está licenciado bajo la Licencia MIT.

Este README proporciona una guía detallada sobre cómo usar y contribuir a la API. Asegúrate de adaptar las URL y los comandos según sea necesario para tu entorno específico.






