from peewee import IntegerField, CharField, Model

from .Database import db


class RedditPost(Model):
    rid = CharField(unique=True)
    title = CharField()
    score = IntegerField()
    url = CharField()
    comments = IntegerField()
    created = IntegerField()
    body = CharField()

    class Meta:
        database = db
