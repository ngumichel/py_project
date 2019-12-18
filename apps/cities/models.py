from peewee import *
from database import BaseModel

class City(BaseModel):
    name = CharField()
    population = CharField()
    city_code = CharField()
    long_deg = DecimalField(max_digits=9, decimal_places=6)
    lat_deg = DecimalField(max_digits=9, decimal_places=6)

City.drop_table(safe=True)
City.create_table()