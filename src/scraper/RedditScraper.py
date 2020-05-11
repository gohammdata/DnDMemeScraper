import praw
from praw.exceptions import PRAWException


class RedditScraper:
    db = None
    topics_dict = {
        "title": [],
        "author": [],
        "score": [],
        "id": [],
        "url": [],
        "comms_num": [],
        "created": [],
        "body": [],
    }

    def __init__(self, appid, secretkey, useragent, username, password):
        self.appid = appid
        self.secretkey = secretkey
        self.useragent = useragent
        self.username = username
        self.password = password
        try:
            self.praw = praw.Reddit(
                client_id=appid,
                client_secret=secretkey,
                user_agent=useragent,
                username=username,
                password=password,
            )
        except PRAWException:
            self.praw = None
            print(
                "Error: Failed to make Reddit connection. Check your variables and ensure Reddit is up and responding."
            )
            quit()

    def parse_subreddit(self, subreddit_name):
        # verify praw object is set up
        if not self.praw:
            return

        subreddit = self.praw.subreddit(subreddit_name)

        posts = subreddit.hot(limit=100)

        return posts
