from peewee import CharField, DateField, IntegerField, Model, TextField, fn

from datetime import datetime

from .Database import db


class RedditPost(Model):
    rid = CharField(unique=True)
    title = TextField()
    score = IntegerField()
    url = CharField()
    comments = IntegerField()
    created = IntegerField()
    body = CharField()
    post_date = DateField(null=True)

    class Meta:
        database = db

    def get_random_post(self):
        query = self.select().order_by(fn.Random())
        post = query.get()
        return post

    def update_post_date(self, id):
        post_date = datetime.today().strftime("%Y-%m-%d")

        self.update(post_date=post_date).where(self.rid == id)
