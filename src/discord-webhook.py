#!/usr/bin/env python3

import os
import random
from datetime import datetime

from discord_webhook import DiscordEmbed, DiscordWebhook
from dotenv import find_dotenv, load_dotenv

from database import RedditPost

# load .env environment files
load_dotenv(find_dotenv())

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

footer_texts = [
    "Lovingly pulled from",
    "Organically sourced from",
    "Culled from the herd of",
    "Harvested by hand from",
    "From the private collection of",
    "Gathered by the natives of",
    "Rescued from the dragon hoard of",
]

random_meme_gif = True

while random_meme_gif is True:
    random_meme = RedditPost().get_random_post()
    random_meme_gif = random_meme.url.endswith(".gif")

converted_date = datetime.utcfromtimestamp(random_meme.created).strftime("%Y-%m-%d")

if random_meme.author is None:
    author = "Unknown"
else:
    author = random_meme.author

webhook = DiscordWebhook(url=WEBHOOK_URL)

embed = DiscordEmbed(title=random_meme.title)

embed.add_embed_field(name="Meme Creator", value=author)

embed.add_embed_field(name="Originally Created", value=converted_date)

embed.set_image(url=random_meme.url)

embed.set_footer(text=f"{random.choice(footer_texts)} https://reddit.com/r/dndmemes")

webhook.add_embed(embed)

response = webhook.execute()

if response.status_code == 204:
    RedditPost().update_post_date(random_meme.id)
