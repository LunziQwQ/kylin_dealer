import os

from peewee import SqliteDatabase

db_file = "database.db"
if not os.path.exists(db_file):
    with open(db_file, "wb") as f:
        f.write(b'')

database = SqliteDatabase(db_file)