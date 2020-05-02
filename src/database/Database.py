from peewee import SqliteDatabase, fn, IntegerField, CharField
from playhouse.signals import Model, pre_save

db = SqliteDatabase("parser.db")


class ParseData(Model):
    rid = CharField()
    title = CharField()
    score = IntegerField()
    url = CharField()
    comments = IntegerField()
    created = IntegerField()
    body = CharField()

    class Meta:
        database = db
