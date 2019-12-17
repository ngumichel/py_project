from settings import CSV_CITY
from settings import CSV_SCHOOL
from settings import INSEE_CODE
import matplotlib.pyplot as plt
import apps.cities.city as ct
import apps.cities.school as sch
import apps.cities.data as dt


if __name__ == '__main__':
    cities = ct.extract_and_prepare_cities_from_csv(CSV_CITY)
    city_rank = dt.show_first_ten_data_in_graph(cities, 'ville_nom', 'ville_population_2012', 'barh')
    plt.show()

    schools = sch.extract_and_prepare_schools_from_csv(CSV_SCHOOL, INSEE_CODE)
    merged_data = dt.merge_data(cities, schools, "Code commune")
    new_data = sch.create_new_column_from_data(merged_data)
    sorted_data = dt.sort_data_by_column(new_data, "Taux Objectif")
    school_rank = dt.show_first_ten_data_in_graph(sorted_data, 'ville_nom', 'Taux Objectif', 'barh')
    plt.show()