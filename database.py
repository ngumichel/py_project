from peewee import *

db = SqliteDatabase('ranking.db')

class BaseModel(Model):
    class Meta:
        database = db