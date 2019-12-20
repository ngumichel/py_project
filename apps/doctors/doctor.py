from settings import CSV_DOCTOR, INSEE_CODE
import numpy as np
import apps.data as dt

def extract_and_prepare_doctors_from_csv(cities):
    doctors = dt.read_csv_file(CSV_DOCTOR, None, ",", 'infer')
    return format_doctors_data(doctors, cities, INSEE_CODE)

def format_doctors_data(doctors, cities, city_code):
    narrowed_doctors = dt.narrow_data_column(doctors, ["c_depcom"])
    renamed_doctors = narrowed_doctors.rename(columns={"c_depcom" : "Code commune"})
    grouped_doctors = group_city_values_into_one_value(renamed_doctors, city_code)
    merged_doctors = dt.merge_data(cities, grouped_doctors, "Code commune")
    return dt.narrow_data_column(merged_doctors, ["Code commune", "Nombre docteur"])

def group_city_values_into_one_value(doctors, city_codes):
    for city in city_codes:
        doctors["Code commune"] = np.where(doctors["Code commune"].isin(city[1]), city[0], doctors["Code commune"])
    return doctors.groupby(["Code commune"]).size().reset_index(name='Nombre docteur')

def rename_doctor_column(doctors):
    return doctors.rename(columns={
        "Code commune" : "city_code",
        "Nombre docteur" : "doctor_count"
    })