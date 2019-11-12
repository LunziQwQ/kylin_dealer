from peewee import IntegerField, DateField, ForeignKeyField, TextField

from models import BaseModel
from models.cargo_type import CargoType


class Cargo(BaseModel):
    cargo_type = ForeignKeyField(CargoType, related_name="cargo_list")
    production_date = DateField()
    count = IntegerField(default=0)
    comment = TextField()


Cargo.create_table()
