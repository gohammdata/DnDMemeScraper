from peewee import fn

from .RedditPost import RedditPost


class RandomPost:
    def get_random_post():
        query = RedditPost.select().order_by(fn.Random())
        post = query.get()
        post_url = post.url
        return post_url
