from peewee import *
from database import BaseModel
from apps.cities.models import City

class School(BaseModel):
    city_code = ForeignKeyField(City, field='city_code', backref='schools')
    total_raw_success_rate = FloatField()
    expected_success_rate = FloatField()
    success_rate_spread = FloatField()

School.create_table()