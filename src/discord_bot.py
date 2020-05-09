#!/usr/bin/env python3

import os

import discord
from dotenv import find_dotenv, load_dotenv

from database import RedditPost

# load .env environment files
load_dotenv(find_dotenv())

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "Meme Me, Brother!":
        random_meme = RedditPost().get_random_post()
        random_meme_url = random_meme.url
        RedditPost().update_post_date(random_meme.id)
        response = random_meme_url
        await message.channel.send(response)


client.run(TOKEN)
