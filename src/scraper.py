#!/usr/bin/env python3

import os

from dotenv import find_dotenv, load_dotenv

from database.Database import create_post_from_reddit

from scraper.RedditScraper import RedditScraper


def main():
    # load .env environment files
    load_dotenv(find_dotenv())
    # create scraper
    scraper = RedditScraper(
        os.getenv("REDDIT_APP_ID"),
        os.getenv("REDDIT_SECRET_KEY"),
        os.getenv("REDDIT_USERAGENT"),
        os.getenv("REDDIT_USERNAME"),
        os.getenv("REDDIT_PASSWORD"),
    )

    posts = scraper.parse_subreddit("dndmemes")
    for post in posts:
        # make sure it's an image post
        if not post.selftext:
            db_post = create_post_from_reddit(post)
            print(db_post)


if __name__ == "__main__":
    main()
