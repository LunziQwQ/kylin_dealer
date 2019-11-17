import datetime
import json

from peewee import CharField, IntegerField, ForeignKeyField, DateField, TextField

from models import BaseModel
from models.custom import Custom


class Order(BaseModel):
    sale_list = TextField(default="[]")
    custom = ForeignKeyField(Custom, related_name='order_list')
    comment = CharField(default="")
    need_pay = IntegerField(default=0)
    now_pay = IntegerField(default=0)
    owe_money = IntegerField(default=0)
    date = DateField()

    @staticmethod
    def build(custom, sale_dict, need_pay, now_pay, owe, date, comment):
        order = Order()
        order.custom = custom
        order.comment = comment
        order.need_pay = need_pay
        order.now_pay = now_pay
        order.owe_money = owe
        order.date = datetime.date(*date)

        sale_list = []
        for cargo, count in sale_dict.items():
            cargo_type = cargo.cargo_type
            item = {
                "cargo_type": cargo_type.name,
                "production_date": str(cargo.production_date),
                "count": count,
                "unit": cargo_type.unit,
                "price": cargo_type.price,
                "life": cargo_type.life
            }
            sale_list.append(item)
            print(type(item), item)

        order.sale_list = json.dumps(sale_list)
        return order


Order.create_table()
