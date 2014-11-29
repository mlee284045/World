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


def move_cities(objects):
    with open('cities.csv', 'wb') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(objects.values_list())


def hiding_person(city_name):
    return City.objects.get(name=city_name)


def flight_cost(start, end):
    diff_lat = abs(start.latitude - end.latitude)
    diff_long = abs(start.longitude - end.longitude)
    if diff_long > 180:
        diff_long = 360 - diff_long
    distance = (float(diff_lat) ** 2 + float(diff_long) ** 2) ** (0.5)
    in_pennies = int(distance ** .66 * 5000)
    return in_pennies // 100
