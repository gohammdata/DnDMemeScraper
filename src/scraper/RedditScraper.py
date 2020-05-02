import praw
from praw.exceptions import PRAWException
import pandas


class RedditScraper():
    topics_dict = {
        "title": [],
        "score": [],
        "id": [],
        "url": [],
        "comms_num": [],
        "created": [],
        "body": [],
    }

    def __init__(self, cid, csecret, uagent, user, passwd):
        self.cid = cid
        self.csecret = csecret
        self.uagent = uagent
        self.user = user
        self.passwd = passwd
        try:
            self.praw = praw.Reddit(
                self.cid,
                self.csecret,
                self.uagent,
                self.user,
                self.passwd
            )
        except PRAWException:
            self.praw = None

    def parse_subreddit(self, subreddit_name):
        # verify praw object is set up
        if not self.praw:
            return

        subreddit = self.praw.subreddit(subreddit_name)

        top_posts = subreddit.top(limit=25)
        for post in top_posts:
            self.topics_dict["title"].append(post.title)
            self.topics_dict["score"].append(post.score)
            self.topics_dict["id"].append(post.id)
            self.topics_dict["url"].append(post.url)
            self.topics_dict["comms_num"].append(post.num_comments)
            self.topics_dict["created"].append(post.created)
            self.topics_dict["body"].append(post.selftext)

    def save_to_csv(self, outName):
        if not self.topics_dict:
            return

        topics_df = pandas.DataFrame(self.topics_dict)
        topics_df.to_csv(outName, index=False)
