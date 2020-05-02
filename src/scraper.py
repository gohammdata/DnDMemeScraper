from database import Database, RedditPost
from dotenv import find_dotenv, load_dotenv
from scraper import RedditScraper
import os


def main():
    # load .env environment files
    load_dotenv(find_dotenv())
    # create database
    db = Database()
    db.create([RedditPost])
    # create scraper
    scraper = RedditScraper(
        os.getenv('REDDIT_APP_ID'),
        os.getenv('REDDIT_SECRET_KEY'),
        os.getenv('REDDIT_USERAGENT'),
        os.getenv('REDDIT_USERNAME'),
        os.getenv('REDDIT_PASSWORD')
    )

    posts = scraper.parse_subreddit('dndmemes')
    for post in posts:
        # create database object
        tmp_reddit_post = RedditPost(
            rid=post.id,
            title=post.title,
            score=post.score,
            url=post.url,
            comments=post.num_comments,
            created=post.created,
            body=post.selftext,
        )
        print(tmp_reddit_post)
        tmp_reddit_post.save()


if __name__ == "__main__":
    main()
