from peewee import SqliteDatabase, fn, IntegerField, CharField
from playhouse.signals import Model, pre_save

db = SqliteDatabase("parser.db")

class Database():
    db = db

    def connect():
        self.db.connect()

    def create(table_list):
        self.db.create_tables(table_list)
