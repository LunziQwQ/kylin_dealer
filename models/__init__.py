import os

from peewee import SqliteDatabase, Model

db_file = "database.db_production"
if not os.path.exists(db_file):
    with open(db_file, "wb") as f:
        f.write(b'')

database = SqliteDatabase(db_file)


class BaseModel(Model):
    class Meta:
        database = database
