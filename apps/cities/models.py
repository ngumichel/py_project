from peewee import *
from database import BaseModel

class City(BaseModel):
    name = CharField()
    population = IntegerField()
    city_code = CharField()
    long_deg = DecimalField(max_digits=9, decimal_places=6)
    lat_deg = DecimalField(max_digits=9, decimal_places=6)

City.create_table()