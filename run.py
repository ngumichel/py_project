from settings import CSV_CITY, CSV_SCHOOL, INSEE_CODE
from database import db
from apps.cities.models import City
from apps.schools.models import School
from apps.doctors.models import Doctor
import pandas as pd
import matplotlib.pyplot as plt
import apps.cities.city as ct
import apps.schools.school as sch
import apps.doctors.doctor as dc
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
            "compute_doctor",
            "show_city_chart",
            "show_school_chart",
            "show_doctor_chart"
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
        schools = sch.extract_and_prepare_schools_from_csv(cities)
        schools_rename = sch.rename_school_column(schools)
        dt.save_data_into_database(schools_rename, School)

    if args.action == "compute_doctor":
        # compute and store result in sql
        cities = ct.extract_and_prepare_cities_from_csv()
        doctors = dc.extract_and_prepare_doctors_from_csv(cities)
        doctors_rename = dc.rename_doctor_column(doctors)
        dt.save_data_into_database(doctors_rename, Doctor)

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

    if args.action == "show_doctor_chart":
        # show result in a chart
        doctors = pd.DataFrame(Doctor.select(City, Doctor).join(City).order_by(Doctor.citizens_per_doctor.desc()).dicts())
        doctor_rank = dt.show_data_in_graph(doctors, 20, 'name', 'citizens_per_doctor', 'barh')
        plt.show()

    db.close()
