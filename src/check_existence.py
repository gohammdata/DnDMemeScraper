#!/usr/bin/env python3

import requests

from database.Database import RedditPost, get_all_posts


def main():
    posts = get_all_posts()

    for post in posts:
        response = requests.get(post.url)
        print(f"Verifying {post.rid}: {post.title}")
        if response.status_code == 404:
            RedditPost.delete(post.rid)
            print(f"Deleted {post.rid}: {post.title}")


if __name__ == "__main__":
    main()
