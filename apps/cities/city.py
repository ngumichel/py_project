import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


def extract_and_prepare_cities_from_csv(data):
    cities = read_cities_csv(data)
    narrowed_data = format_data(cities)
    return narrowed_data

def format_data(cities):
    sorted_cities = sort_cities_by_population(cities)
    selected_cities = select_first_fifty_cities(sorted_cities)
    narrowed_data = narrow_data_to_name_and_population(selected_cities)
    return narrowed_data

def read_cities_csv(file):
    cities = pd.read_csv(file, names=['ville_id', 'ville_departement', 'ville_slug', 'ville_nom', 'ville_nom_simple', 'ville_nom_reel', 'ville_nom_soundex', 'ville_nom_metaphone', 'ville_code_postal', 'ville_commune', 'ville_code_commune', 'ville_arrondissement', 'ville_canton', 'ville_amdi', 'ville_population_2010', 'ville_population_1999', 'ville_population_2012', 'ville_densite_2010', 'ville_surface', 'ville_longitude_deg', 'ville_latitude_deg', 'ville_longitude_grd', 'ville_latitude_grd', 'ville_longitude_dms', 'ville_latitude_dms', 'ville_zmin', 'ville_zmax'], header=None, low_memory=False)
    return cities

def sort_cities_by_population(city):
    sorted_cities = city.sort_values('ville_population_2012', ascending=False)
    return sorted_cities

def select_first_fifty_cities(sorted):
    selected_cities = sorted.head(50)
    return selected_cities

def narrow_data_to_name_and_population(selected):
    narrowed_data = DataFrame(selected, columns=['ville_nom', 'ville_population_2012'])
    return narrowed_data

def show_first_ten_cities_in_graph(narrowed):
    narrowed.head(10).plot(x='ville_nom', y='ville_population_2012', kind='barh')


if __name__ == '__main__':
    plt.show()