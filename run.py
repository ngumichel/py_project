from settings import CSV_CITY, CSV_SCHOOL, INSEE_CODE
from database import db
from apps.cities.models import City
from apps.schools.models import School
import pandas as pd
import matplotlib.pyplot as plt
import apps.cities.city as ct
import apps.schools.school as sch
import apps.data as dt
import argparse


if __name__ == '__main__':

    db.connect(reuse_if_open=True)
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        help="Choose an action to execute",
        nargs="?",
        choices=[
            "compute_city",
            "compute_school",
            "show_city_chart",
            "show_school_chart",
        ],
    )
    args = parser.parse_args()

    if args.action == "compute_city":
        # compute and store result in sql
        cities = ct.extract_and_prepare_cities_from_csv()
        cities_rename = ct.rename_city_column(cities)
        dt.save_data_into_database(cities_rename, City)

    if args.action == "compute_school":
        # compute and store result in sql
        cities = ct.extract_and_prepare_cities_from_csv()
        schools = sch.extract_and_prepare_schools_from_csv()
        merged_data = dt.merge_data(cities, schools, "Code commune")
        school_reduce = dt.narrow_data_column(merged_data, ['Code commune', 'Taux Brut de Réussite Total séries', 'Taux Réussite Attendu France Total séries', "Taux Objectif"])
        schools_rename = sch.rename_school_column(school_reduce)
        dt.save_data_into_database(schools_rename, School)

    if args.action == "show_city_chart":
        # show result in a chart
        cities = pd.DataFrame(City.select().order_by('population').limit(10).dicts())
        print(cities)
        city_rank = dt.show_data_in_graph(cities, 10, 'name', 'population', 'barh')
        plt.show()
    
    if args.action == "show_school_chart":
        # show result in a chart
        schools = pd.DataFrame(School.select(City, School).join(City).order_by(School.success_rate_spread.desc()).dicts())
        print(schools)
        school_rank = dt.show_data_in_graph(schools, 50, 'name', 'success_rate_spread', 'bar')
        plt.show()

    db.close()
