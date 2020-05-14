from dotenv import find_dotenv, load_dotenv
import os
from pony.orm import Database, Required, db_session
import datetime

load_dotenv(find_dotenv())

db = Database()

db.bind(
    provider='postgres',
    user=os.getenv("POSTGRES_USERNAME"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
)


class RedditPost(db.Entity):
    rid = Required(str)
    title = Required(str)
    author = Required(str)
    score = int
    url = Required(str)
    comments = int
    created = Required(int)
    body = str
    post_date = datetime
    subreddit = datetime


@db_session
def get_post(rid):
    post = RedditPost[rid]
    return post



