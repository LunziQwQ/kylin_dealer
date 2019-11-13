from peewee import CharField, IntegerField

from models import BaseModel


class Custom(BaseModel):
    name = CharField(unique=True)
    phone = CharField()
    addr = CharField(default="")
    comment = CharField(default="")
    trade_money = IntegerField(default=0)
    owe_money = IntegerField(default=0)


Custom.create_table()
