#!/usr/bin/env python3

import os

from dotenv import find_dotenv, load_dotenv

from database import Database, RedditPost
from scraper import RedditScraper


def main():
    # create database
    db = Database()
    db.create([RedditPost])

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
            # create database object
            tmp_reddit_post = RedditPost(
                rid=post.id,
                author=post.author,
                title=post.title,
                score=post.score,
                url=post.url,
                comments=post.num_comments,
                created=post.created,
                body=post.selftext,
            )
            reddit_post = RedditPost.get_or_none(rid=f"{post.id}")
            if reddit_post is None:
                tmp_reddit_post.save()
                print(f"<{post.id}> {post.title}")
            else:
                print(f"{post.id} already in cache")

    # random_meme = RedditPost().get_random_post()
    # random_meme_url = random_meme.url
    # print(random_meme_url)
    # RedditPost().update_post_date(random_meme.id)


if __name__ == "__main__":
    main()
