from peewee import CharField, IntegerField

from models import BaseModel


class OfficeExp(BaseModel):
    name = CharField()
    money = IntegerField(default=0)
    comment = CharField(default="")

    @staticmethod
    def build(name, money, comment):
        o = OfficeExp()
        o.name = name
        o.money = int(float(money) * 100)
        o.comment = comment
        return o


OfficeExp.create_table()
