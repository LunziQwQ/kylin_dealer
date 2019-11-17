from peewee import CharField, IntegerField, ForeignKeyField, DateField, TextField

from models import BaseModel
from models.cargo import Cargo
from models.cargo_type import CargoType
from models.custom import Custom


class Order(BaseModel):
    cargo_list = TextField()
    custom_name = ForeignKeyField(Custom, related_name='order_list')
    comment = CharField(default="")
    need_pay = IntegerField(default=0)
    now_pay = IntegerField(default=0)
    owe_money = IntegerField(default=0)
    date = DateField()


Custom.create_table()
