from peewee import *
from database import BaseModel
from apps.cities.models import City

class Doctor(BaseModel):
    city_code = ForeignKeyField(City, field='city_code')
    doctor_count = IntegerField()

Doctor.create_table()