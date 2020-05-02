#!/usr/bin/env python3
import praw
import os
import pandas as pd
import datetime as dt
from dotenv import load_dotenv  #dotenv (.env) or direnv (.envrc)?  Using dotenv and (.env) as I think works best for Heroku.

def main():
    reddit = praw.Reddit(
        client_id= os.getenv('CLIENT_ID'),
        client_secret= os.getenv('CLIENT_SECRET'),
        user_agent="DnD Memes",
        username= os.getenv('REDDITMEMES_USERNAME'),
        password = os.getenv('REDDITMEMES_PASSWORD'),
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

    topics_data = pd.DataFrame(topics_dict)
    topics_data.to_csv("top25.csv", index=False)


if __name__ == "__main__":
    main()  #Recommended in Discord Bot, but can we implement classes and OOP? Python probably has whiz stuff around this, but I like objects.
