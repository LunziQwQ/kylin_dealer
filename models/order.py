from peewee import Model, CharField, IntegerField, ForeignKeyField, DateField

from models import database
from models.cargo import Cargo
from models.custom import Custom


class Order(Model):
    class Meta:
        database = database

    cargo_type = ForeignKeyField(Cargo, related_name='cargo_type')
    production_date = ForeignKeyField(Cargo, related_name='production_date')
    custom_name = ForeignKeyField(Custom, related_name='name')
    size = IntegerField(default=0)
    comment = CharField(default="")
    need_pay = IntegerField(default=0)
    now_pay = IntegerField(default=0)
    owe_money = IntegerField(default=0)
    date = DateField()


Custom.create_table()
