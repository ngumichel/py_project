import matplotlib.pyplot as plt
import apps.cities.city as city
from settings import CSV_CITY
from settings import CSV_SCHOOL


def show_city_rank():
    data = city.extract_and_prepare_cities_from_csv(csv_city)
    cities = city.show_first_ten_cities_in_graph(data)
    plt.show()
