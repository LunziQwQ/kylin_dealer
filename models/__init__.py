import os

from peewee import SqliteDatabase, Model, TextField, IntegerField, ForeignKeyField, DateField

db_file = "database.db"
if not os.path.exists(db_file):
    with open(db_file, "wb") as f:
        f.write(b'')

database = SqliteDatabase(db_file)


class BaseModel(Model):
    class Meta:
        database = database

#
# class CargoType(BaseModel):
#     name = TextField(unique=True)
#     life = IntegerField(default=270)
#     unit = TextField(default="箱")
#     count = IntegerField(default=0)
#     price = IntegerField(default=0)
#
#     @staticmethod
#     def create(name, unit, life, price):
#         c = CargoType()
#         c.name = name
#         c.unit = unit
#         c.life = life
#         c.price = price
#         return c
#
#
# class Cargo(BaseModel):
#     # cargo_type = ForeignKeyField(CargoType, related_name='name')
#     production_date = DateField()
#     count = IntegerField(default=0)
#     comment = TextField()
#
#
# class Custom(BaseModel):
#     name = TextField(unique=True)
#     phone = TextField()
#     addr = TextField(default="")
#     comment = TextField(default="")
#     trade_money = IntegerField(default=0)
#     owe_money = IntegerField(default=0)
#
#
# class Order(BaseModel):
#     # cargo_type = ForeignKeyField(Cargo, related_name='cargo_type')
#     # production_date = ForeignKeyField(Cargo, related_name='production_date')
#     # custom_name = ForeignKeyField(Custom, related_name='name')
#     size = IntegerField(default=0)
#     comment = TextField(default="")
#     need_pay = IntegerField(default=0)
#     now_pay = IntegerField(default=0)
#     owe_money = IntegerField(default=0)
#     date = DateField()
#
#
# database.create_tables([CargoType, Cargo, Custom, Order])
