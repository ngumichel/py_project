from settings import CSV_CITY
import apps.data as dt

column_name = ['ville_id', 'ville_departement', 'ville_slug', 'ville_nom', 'ville_nom_simple', 'ville_nom_reel', 'ville_nom_soundex', 'ville_nom_metaphone', 'ville_code_postal', 'ville_commune', 'Code commune', 'ville_arrondissement', 'ville_canton', 'ville_amdi', 'ville_population_2010', 'ville_population_1999', 'ville_population_2012', 'ville_densite_2010', 'ville_surface', 'ville_longitude_deg', 'ville_latitude_deg', 'ville_longitude_grd', 'ville_latitude_grd', 'ville_longitude_dms', 'ville_latitude_dms', 'ville_zmin', 'ville_zmax']
narrow_column_name = ['ville_nom', 'ville_population_2012', 'Code commune', 'ville_longitude_deg', 'ville_latitude_deg']

def extract_and_prepare_cities_from_csv():
    cities = dt.read_csv_file(CSV_CITY, column_name, ",", None)
    return format_cities_data(cities)

def format_cities_data(cities):
    sorted_cities = dt.sort_data_by_column(cities, 'ville_population_2012')
    selected_cities = dt.select_data_range(sorted_cities, 50)
    return dt.narrow_data_column(selected_cities, narrow_column_name)

def rename_city_column(cities):
    return cities.rename(columns={
        "ville_nom" : "name",
        "ville_population_2012" : "population",
        "Code commune" : "city_code",
        "ville_longitude_deg" : "long_deg",
        "ville_latitude_deg" : "lat_deg"
    })