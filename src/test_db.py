from pony.orm import db_session, set_sql_debug

from database.database import RedditPost, get_random_post, get_post
import datetime


set_sql_debug(True)


class TestDB:
    @db_session
    def test_db_select_random(self):
        post = get_random_post()
        assert isinstance(post, RedditPost)

    @db_session
    def test_unique(self):
        db_post = get_post(292)
        assert isinstance(db_post, RedditPost)

    @db_session
    def test_update_date(self):
        db_post = get_post(292)
        today_date = datetime.datetime.now().date()
        db_post.post_date = today_date
        assert db_post.post_date == today_date
