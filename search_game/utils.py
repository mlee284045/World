import csv
from search_game.models import City


def create_cities(f):
    with open(f, 'rb') as city_file:
        for row in csv.reader(city_file):
            try:
                City.objects.create(name=row[1], country=row[2], latitude=float(row[3]), longitude=float(row[4]))
                print row[1], row[3], row[5], row[6]
            except (IndexError, ValueError):
                pass
            # loc_id, country, region, city, postal, latitude, longitude, metrocode, areacode = row
            # country = row[1]
            # city = row[3]
            # latitude = row[5]
            # longitude = row[6]
            # print country, city, latitude, longitude

def move_cities(objects):
    with open('cities.csv', 'wb') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(objects.values_list())

def hiding_person():
    return City.objects.get(name='Rome')

