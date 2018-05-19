from busqueda.models import Ciudad
import csv

with open('cities.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:

        instance = Ciudad.get_or_create(
            ciudad=row[0],
            pais=row[5],
            latitud=row[2],
            longitud=row[3],
        )
        #city,city_ascii,lat,lng,pop,country,iso2,iso3,province
        print('City: ' + row[0]+'\tCountry: ' + row[5]+'\tlat: ' + row[2]+'\tlong: ' + row[3])


