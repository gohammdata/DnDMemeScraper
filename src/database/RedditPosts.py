from peewee import SqliteDatabase, fn, IntegerField, CharField
from playhouse.signals import Model, pre_save

from Database import db


class RedditPosts(Model):
    rid = CharField(unique=True)
    title = CharField()
    score = IntegerField()
    url = CharField()
    comments = IntegerField()
    created = IntegerField()
    body = CharField()

    class Meta:
        database = db
