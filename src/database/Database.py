from dotenv import find_dotenv, load_dotenv
import os
from pony.orm import Database, Required, Optional, db_session, select, commit
import datetime

load_dotenv(find_dotenv())

db = Database()

# print(os.getenv("POSTGRES_USERNAME"))
# print(os.getenv("POSTGRES_PASSWORD"))
# print(os.getenv("POSTGRES_HOST"))
# print(os.getenv("POSTGRES_PORT"))

db.bind(
    provider="postgres",
    user=os.getenv("POSTGRES_USERNAME"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
)


class RedditPost(db.Entity):
    rid = Required(str)
    title = Required(str)
    author = Required(str)
    score = Required(int)
    url = Required(str)
    comments = Required(int)
    created = Required(float)
    body = Optional(str)
    post_date = Optional(datetime.date)
    subreddit = Optional(str)

    def __str__(self):
        return f"<{self.rid}> {self.title}"


@db_session
def get_post(rid):
    post = RedditPost[rid]
    return post


@db_session
def get_random_post():
    thirty_days_ago = datetime.datetime.now().date() - datetime.timedelta(days=30)
    return select(p for p in RedditPost if p.post_date < thirty_days_ago).random(1)[0]


@db_session
def create_post_from_reddit(post):
    db_post = RedditPost(
        rid=post.id,
        title=post.title,
        author=str(post.author),
        score=post.score,
        url=post.url,
        comments=post.num_comments,
        created=post.created,
        body=post.selftext,
        post_date=datetime.date(2010, 1, 1),
        subreddit=str(post.subreddit),
    )
    commit()
    return db_post


@db_session
def update_post_date(rid):
    post = get_post(rid)
    post.post_date = datetime.date.today()


db.generate_mapping(create_tables=True)
