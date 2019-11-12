from peewee import Model, CharField, IntegerField, TextField

from models import database


class CargoType(Model):
    class Meta:
        database = database

    name = TextField(unique=True)
    life = IntegerField(default=270)
    unit = TextField(default="箱")
    count = IntegerField(default=0)
    price = IntegerField(default=0)


CargoType.create_table()
