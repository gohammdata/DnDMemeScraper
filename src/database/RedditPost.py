from peewee import CharField, IntegerField, Model, TextField

from .Database import db


class RedditPost(Model):
    rid = CharField(unique=True)
    title = TextField()
    score = IntegerField()
    url = CharField()
    comments = IntegerField()
    created = IntegerField()
    body = CharField()

    class Meta:
        database = db
