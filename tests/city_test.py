import apps.cities.city as city
from settings import csv_file

def test_golden():
    citytest = str(city.extract_and_prepare_cities_from_csv(csv_file))
    with open('tests/gstate.txt', 'r') as file:
        data = file.read()
    assert citytest == data
