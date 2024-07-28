# WorldAPI

WorldAPI es una API para manejar información de países y ciudades.

## Descripción

Esta API permite obtener información sobre países y ciudades. Incluye endpoints para listar, buscar y gestionar datos geográficos.

## Endpoints

### Países

- `GET /api/countries/` - Lista todos los países.
- `GET /api/countries/<code>/` - Obtiene detalles de un país específico por su código.

### Ciudades

- `GET /api/cities/` - Lista todas las ciudades.
- `GET /api/cities/<id>/` - Obtiene detalles de una ciudad específica por su ID.

## Instalación

1. Clona el repositorio: `git clone https://github.com/javierfevidaho/worldapi.git`
2. Navega al directorio del proyecto: `cd worldapi`
3. Crea y activa un entorno virtual: `python -m venv .venv && source .venv/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Realiza las migraciones de la base de datos: `python manage.py migrate`
6. Ejecuta el servidor: `python manage.py runserver`

## Población de la Base de Datos

Para poblar la base de datos con países y ciudades:

```bash
python manage.py shell

from geography.models import Country, City
from django.db import transaction
import requests
import zipfile
import csv

@transaction.atomic
def populate_countries():
    url = 'http://download.geonames.org/export/dump/countryInfo.txt'
    response = requests.get(url)
    lines = response.text.splitlines()
    reader = csv.reader(lines, delimiter='\t')
    
    for row in reader:
        if not row or row[0].startswith('#'):
            continue
        country_code = row[0]
        country_name = row[4]
        Country.objects.get_or_create(name=country_name, code=country_code)
        print(f"Added country: {country_name}")

populate_countries()

@transaction.atomic
def populate_cities():
    url = 'http://download.geonames.org/export/dump/cities500.zip'
    response = requests.get(url, stream=True)
    with open('cities500.zip', 'wb') as f:
        f.write(response.content)

    with zipfile.ZipFile('cities500.zip', 'r') as zip_ref:
        zip_ref.extractall('.')

    with open('cities500.txt', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if not row:
                continue
            city_name = row[1]
            country_code = row[8]
            try:
                country = Country.objects.get(code=country_code)
                City.objects.get_or_create(name=city_name, country=country)
                print(f"Added city: {city_name} in {country.name}")
            except Country.DoesNotExist:
                print(f"Country with code {country_code} does not exist.")
                continue

populate_cities()

Ejemplos de uso con curl
Obtener todos los países:


curl -X GET http://localhost:8000/api/countries/
Obtener un país por ID:


curl -X GET http://localhost:8000/api/countries/1/
Obtener todas las ciudades:


curl -X GET http://localhost:8000/api/cities/
Obtener una ciudad por ID:

