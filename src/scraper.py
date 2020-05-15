#!/usr/bin/env python3

import os

from dotenv import find_dotenv, load_dotenv

from database.Database import create_post_from_reddit

# from database.Database import Database
# from database.RedditPost import RedditPost
from scraper.RedditScraper import RedditScraper


def main():
    # create database
    # db = Database()
    # db.create([RedditPost])

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
            # create database object
            # tmp_reddit_post = RedditPost(
            #     rid=post.id,
            #     author=post.author,
            #     title=post.title,
            #     score=post.score,
            #     url=post.url,
            #     comments=post.num_comments,
            #     created=post.created,
            #     body=post.selftext,
            #     subreddit=post.subreddit,
            # )

    # random_meme = RedditPost().get_random_post()
    # random_meme_url = random_meme.url
    # print(random_meme_url)
    # RedditPost().update_post_date(random_meme.id)


if __name__ == "__main__":
    main()
