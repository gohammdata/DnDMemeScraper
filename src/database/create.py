from Database import db
from RedditPosts import RedditPosts


def create_db():
    print('Creating tables..')
    with db:
        db.create_tables([RedditPosts])
    print('Tables created!')

if __name__ == "__main__":
    create_db()
