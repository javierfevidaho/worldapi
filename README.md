# WorldAPI

WorldAPI es una API para manejar información de países y ciudades.

## Descripción

Esta API permite obtener información sobre países y ciudades. Incluye endpoints para listar, buscar y gestionar datos geográficos.

## Endpoints

### Países

- `GET /api/countries/` - Lista todos los países.
- `GET /api/countries/<code>/` - Obtiene detalles de un país específico por su código.



## Instalación

1. Clona el repositorio: `git clone https://github.com/javierfevidaho/worldapi.git`
2. Navega al directorio del proyecto: `cd worldapi`
3. Crea y activa un entorno virtual: `python -m venv .venv && source .venv/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Realiza las migraciones de la base de datos: `python manage.py migrate`
6. Ejecuta el servidor: `python manage.py runserver`

## Población de la Base de Datos

Para poblar la base de datos con países:

Ejemplos de uso con curl

Obtener todos los países:
curl -X GET http://localhost:8000/api/countries/

Obtener un país por ID:
curl -X GET http://localhost:8000/api/countries/1/


