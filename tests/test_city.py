import apps.cities.city as city
from settings import CSV_CITY


def test_city_data():
    city_data = city.extract_and_prepare_cities_from_csv().to_string()
    with open('tests/results/golden_master.txt', 'r') as file:
        data = file.read()
    assert city_data == data
