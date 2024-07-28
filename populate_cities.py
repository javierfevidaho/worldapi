from geography.models import Country, City
from django.db import transaction
import requests
import zipfile
import csv

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
            city_name = row[1]  # Corrected index for city name
            country_code = row[8]  # Index for country code might need adjustment based on file format
            try:
                country = Country.objects.get(code=country_code)
                City.objects.get_or_create(name=city_name, country=country)
                print(f"Added city: {city_name} in {country.name}")
            except Country.DoesNotExist:
                print(f"Country with code {country_code} does not exist.")
                continue

populate_cities()
