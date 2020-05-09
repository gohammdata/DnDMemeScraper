#!/usr/bin/env python3

import os

from discord_webhook import DiscordWebhook
from dotenv import find_dotenv, load_dotenv

from database import RedditPost

# load .env environment files
load_dotenv(find_dotenv())

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

random_meme = RedditPost().get_random_post()
random_meme_url = random_meme.url

webhook = DiscordWebhook(url=f"{WEBHOOK_URL}", content=f"{random_meme_url}")
response = webhook.execute()

if response.status_code == 204:
    RedditPost().update_post_date(random_meme.id)
