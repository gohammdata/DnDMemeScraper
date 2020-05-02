from peewee import (
    SqliteDatabase, fn, IntegerField, CharField
)
from playhouse.signals import Model, pre_save

db = SqliteDatabase('parser.db')


class ParseData(Model):
    # auto inc id, uses pre_save hook to autoinc
    pid = IntegerField()
    title = CharField()
    score = IntegerField()
    rid = CharField()
    url = CharField()
    comments = IntegerField()
    created = IntegerField()
    body = CharField()

    class Meta:
        database = db


@pre_save(sender=ParseData)
def on_save_handler(model_class, instance, created):
    # find max value of temp_id in model
    # increment it by one and assign it to model instance object
    next_value = ParseData.select(fn.Max(ParseData.pid))[0].temp_id + 1
    instance.pid = next_value
