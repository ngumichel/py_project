import apps.schools.school as school
import apps.data as dt
from settings import CSV_SCHOOL, CSV_CITY, INSEE_CODE

def test_main_city_code_should_be_in_dataframe():
    schools = dt.read_csv_file(CSV_SCHOOL, None, ';', 'infer')
    grp_schools = school.group_disctrict_city_into_one_value(schools, INSEE_CODE)
    assert any(grp_schools['Code commune'].isin(['75056']))
    assert any(grp_schools['Code commune'].isin(['13055']))
    assert any(grp_schools['Code commune'].isin(['69123']))

def test_district_city_code_should_not_be_in_dataframe():
    schools = dt.read_csv_file(CSV_SCHOOL, None, ';', 'infer')
    grp_schools = school.group_disctrict_city_into_one_value(schools, INSEE_CODE)
    assert grp_schools['Code commune'].isin(['75105']).any().any() == False
    assert grp_schools['Code commune'].isin(['13205']).any().any() == False
    assert grp_schools['Code commune'].isin(['69385']).any().any() == False

def test_city_code_column_should_only_have_unique_value():
    schools = dt.read_csv_file(CSV_SCHOOL, None, ';', 'infer')
    grp_schools = school.group_disctrict_city_into_one_value(schools, INSEE_CODE)
    assert grp_schools['Code commune'].is_unique 

