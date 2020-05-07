from peewee import CharField, DateField, IntegerField, Model, TextField, fn

from .Database import db


class RedditPost(Model):
    rid = CharField(unique=True)
    title = TextField()
    score = IntegerField()
    url = CharField()
    comments = IntegerField()
    created = IntegerField()
    body = CharField()
    post_date = DateField()

    class Meta:
        database = db

    def get_random_post(self):
        query = self.select().order_by(fn.Random())
        post = query.get()
        return post
