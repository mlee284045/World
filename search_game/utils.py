import csv
from psycopg2._psycopg import DataError
from search_game.models import City


def create_cities(f):
    with open(f, 'rb') as city_file:
        for row in csv.reader(city_file):
            try:
                # print row[5], type(row[5])
                if row[3] == '':
                    pass
                else:
                    City.objects.create(name=row[3], country=row[1], latitude=float(row[5]), longitude=float(row[6]))
                print row[1], row[3], row[5], row[6]
            except (IndexError, ValueError, DataError):
                pass
            # loc_id, country, region, city, postal, latitude, longitude, metrocode, areacode = row
            # country = row[1]
            # city = row[3]
            # latitude = row[5]
            # longitude = row[6]
            # print country, city, latitude, longitude