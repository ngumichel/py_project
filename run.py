import matplotlib.pyplot as plt
import apps.cities.city as city
from settings import csv_file

def main():
    data = city.show_cities(csv_file)
    cities = city.show_first_ten_cities_in_graph(data)
    plt.show()