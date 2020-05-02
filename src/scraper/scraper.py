#!/usr/bin/env python3
import praw
import pandas
import random


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i : i + n]


def main():
    reddit = praw.Reddit(
        client_id="./.envrc/id",
        client_secret="./.envrc/key",
        user_agent="DnD Memes",
        username="./.envrc/user",
        password="./.envrc/password",
    )

    topics_dict = {
        "title": [],
        "score": [],
        "id": [],
        "url": [],
        "comms_num": [],
        "created": [],
        "body": [],
    }

    subreddit = reddit.subreddit("dndmemes")

    top_subreddit = subreddit.top(limit=25)

    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)

    url_list = []

    for url in topics_dict["url"]:
        url_list.append(url)

    shuffled_url_list = random.shuffle(url_list)

    dank_memes = list(divide_chunks(shuffled_url_list, 5))
    print(dank_memes)


if __name__ == "__main__":
    main()
