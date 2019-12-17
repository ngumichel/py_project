import apps.cities.city as city
from settings import CSV_CITY


def test_main_data():
    citytest = str(city.extract_and_prepare_cities_from_csv(CSV_CITY))
    with open('tests/results/golden_master.txt', 'r') as file:
        data = file.read()
    assert citytest == data
