import datetime

from peewee import IntegerField, DateField, ForeignKeyField, TextField

from models import BaseModel
from models.cargo_type import CargoType


class Cargo(BaseModel):
    cargo_type = ForeignKeyField(CargoType, related_name="cargo_list")
    production_date = DateField()
    count = IntegerField(default=0)
    comment = TextField()

    @staticmethod
    def build(cargo_type, production_date, count, comment):
        c = Cargo()
        c.cargo_type = cargo_type
        c.production_date = datetime.date(*production_date)
        c.count = int(count)
        c.comment = comment
        return c


Cargo.create_table()
