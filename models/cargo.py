from peewee import Model, CharField, IntegerField, DateField, ForeignKeyField

from models import database
from models.cargo_type import CargoType


class Cargo(Model):
    class Meta:
        database = database

    cargo_type = ForeignKeyField(CargoType, related_name='name')
    production_date = DateField()
    size = IntegerField(default=0)
    comment = CharField()


Cargo.create_table()
