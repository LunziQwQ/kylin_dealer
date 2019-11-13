from peewee import IntegerField, TextField

from models import BaseModel


class CargoType(BaseModel):
    name = TextField(unique=True)
    life = IntegerField(default=270)
    unit = TextField(default="箱")
    count = IntegerField(default=0)
    price = IntegerField(default=0)

    @staticmethod
    def build(name, unit, life, price):
        c = CargoType()
        c.name = name
        c.unit = unit
        c.life = life
        c.price = int(float(price) * 100)
        return c


CargoType.create_table()
