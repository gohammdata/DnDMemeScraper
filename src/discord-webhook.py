#!/usr/bin/env python3

import os
from datetime import datetime

from discord_webhook import DiscordEmbed, DiscordWebhook
from dotenv import find_dotenv, load_dotenv

from database import RedditPost

# load .env environment files
load_dotenv(find_dotenv())

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

random_meme = RedditPost().get_random_post()

converted_date = datetime.utcfromtimestamp(random_meme.created).strftime("%Y-%m-%d")

if random_meme.author is None:
    author = "Unknown"
else:
    author = random_meme.author

webhook = DiscordWebhook(url=f"{WEBHOOK_URL}")

# create embed object for webhook
embed = DiscordEmbed(title=f"{random_meme.title}")

embed.add_embed_field(name="Meme Creator", value=f"{author}")
embed.add_embed_field(name="Originally Created", value=f"{converted_date}")

# set image
embed.set_image(url=f"{random_meme.url}")

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()

if response.status_code == 204:
    RedditPost().update_post_date(random_meme.id)
