from settings import CSV_SCHOOL, INSEE_CODE
import numpy as np
import apps.data as dt

narrow_column_name = ['Code commune', 'Taux Brut de Réussite Total séries', 'Taux Réussite Attendu France Total séries', 'Taux Objectif']

def extract_and_prepare_schools_from_csv(cities):
    schools = dt.read_csv_file(CSV_SCHOOL, None, ";", 'infer')
    return format_schools_data(schools, cities, INSEE_CODE)

def format_schools_data(schools, cities, city_code):
    grouped_schools = group_disctrict_city_into_one_value(schools, city_code)
    create_new_column_from_data(grouped_schools)
    narrowed_schools = dt.narrow_data_column(grouped_schools, narrow_column_name)
    merged_schools = dt.merge_data(cities, schools, "Code commune")
    return dt.narrow_data_column(merged_schools, narrow_column_name)

def group_disctrict_city_into_one_value(schools, city_codes):
    for city in city_codes:
        schools["Code commune"] = np.where(schools["Code commune"].isin(city[1]), city[0], schools["Code commune"])
    return schools.groupby(["Code commune"], as_index=False).mean()

def create_new_column_from_data(data):
    data['Taux Objectif'] = data['Taux Brut de Réussite Total séries'] - data['Taux Réussite Attendu France Total séries']
    return data

def rename_school_column(schools):
    return schools.rename(columns={
        "Code commune" : "city_code",
        "Taux Brut de Réussite Total séries" : "total_raw_success_rate",
        "Taux Réussite Attendu France Total séries" : "expected_success_rate",
        "Taux Objectif" : "success_rate_spread"
    })

