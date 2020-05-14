from database import RedditPost
from scraper import RedditScraper

from dotenv import find_dotenv, load_dotenv
import os


def main():
    posts = RedditPost.select()
    load_dotenv(find_dotenv())

    scraper = RedditScraper(
        os.getenv("REDDIT_APP_ID"),
        os.getenv("REDDIT_SECRET_KEY"),
        os.getenv("REDDIT_USERAGENT"),
        os.getenv("REDDIT_USERNAME"),
        os.getenv("REDDIT_PASSWORD"),
    )

    for post in posts:
        if post.author and post.subreddit:
            print(f"Skipping {post.rid} because data already exists")
            continue
        # get reddit post from PRAW
        print(f"<{post.rid}> {post.title}")
        r_post = scraper.get_post_by_rid(post.rid)
        print(f"{r_post.author} {r_post.subreddit}")
        post.author = r_post.author
        post.subreddit = r_post.subreddit
        post.save()


if __name__ == "__main__":
    main()
