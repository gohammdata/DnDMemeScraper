from peewee import CharField, DateField, IntegerField, Model, TextField, fn

from datetime import date, timedelta

from .Database import db

today = date.today()


class RedditPost(Model):
    rid = CharField(unique=True)
    title = TextField()
    author = TextField()
    score = IntegerField()
    url = CharField()
    comments = IntegerField()
    created = IntegerField()
    body = CharField()
    post_date = DateField(null=True)

    class Meta:
        database = db

    def check_post_date(self, post):
        if post.post_date is not None:
            last_posted = today - post.post_date
        else:
            last_posted = timedelta(days=1000, minutes=0, seconds=00)

        return last_posted

    def get_random_post(self):
        query = self.select().order_by(fn.Random())
        post = query.get()

        last_posted = timedelta(days=20, minutes=0, seconds=00)

        while last_posted < timedelta(days=30):
            query = self.select().order_by(fn.Random())
            post = query.get()
            last_posted = self.check_post_date(post)

        return post

    def update_post_date(self, id):
        self.set_by_id(f"{id}", {"post_date": today})
