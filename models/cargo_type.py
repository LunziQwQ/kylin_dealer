from peewee import Model, CharField, IntegerField

from models import database


class CargoType(Model):
    class Meta:
        database = database

    name = CharField(primary_key=True)
    life = IntegerField(default=270)
    unit = CharField(default="箱")
    price = IntegerField(default=0)


CargoType.create_table()
