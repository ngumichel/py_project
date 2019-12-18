import numpy as np
import apps.data as dt

narrow_column_name = ['Code commune', 'Taux Brut de Réussite Total séries', 'Taux Réussite Attendu France Total séries']

def extract_and_prepare_schools_from_csv(data_file, city_code):
    schools = dt.read_csv_file(data_file, None, ";", 'infer')
    return format_schools_data(schools, city_code)

def format_schools_data(schools, city_code):
    grouped_schools = group_disctrict_city_into_one_value(schools, city_code)
    return dt.narrow_data_column(grouped_schools, narrow_column_name)

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

