from settings import CSV_CITY, CSV_SCHOOL, INSEE_CODE
from database import db
from apps.cities.models import City
from apps.schools.models import School
import matplotlib.pyplot as plt
import apps.cities.city as ct
import apps.schools.school as sch
import apps.data as dt



if __name__ == '__main__':
    
    db.connect(reuse_if_open=True)

    cities = ct.extract_and_prepare_cities_from_csv(CSV_CITY)
    city_rank = dt.show_first_ten_data_in_graph(cities, 'ville_nom', 'ville_population_2012', 'barh')
    plt.show()

    schools = sch.extract_and_prepare_schools_from_csv(CSV_SCHOOL, INSEE_CODE)
    merged_data = dt.merge_data(cities, schools, "Code commune")
    new_data = sch.create_new_column_from_data(merged_data)
    sorted_data = dt.sort_data_by_column(new_data, "Taux Objectif")
    school_rank = dt.show_first_ten_data_in_graph(sorted_data, 'ville_nom', 'Taux Objectif', 'bar')
    plt.show()

    cities_rename = ct.rename_city_column(cities)

    school_reduce = dt.narrow_data_column(new_data, ['Code commune', 'Taux Brut de Réussite Total séries', 'Taux Réussite Attendu France Total séries', "Taux Objectif"])
    schools_rename = sch.rename_school_column(school_reduce)

    dt.save_data_into_database(cities_rename, City)
    dt.save_data_into_database(schools_rename, School)

    query = School.select().join(City).where(City.name == "LYON").dicts()
    print(list(query))

    db.close()
