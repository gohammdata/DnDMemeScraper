#!/usr/bin/env python3
import os
import discord
import scraper.py from ./scaper as scraper
from dotenv import load_dotenv #dotenv (.env) or direnv (.envrc)?  Using dotenv and (.env) as I think works best for Heroku.

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
memes = scraper.__main__

client = discord.Client()
"""
We can either use classes or just direct events. I commented out the class
option. I'd recommend we use OOP and this option; but I know Python probably has stuff that
would make it more efficient not too.

Here is OOP route. I don't know how to do other route with Python.
"""
"""
class MemeClient(discord.Client):
    async def on_ready(self):
        if message.author == client.user:
            return
        print(f'{self.user} has connected to Discord!')
        async def first_memes(message):
            i = 0
            n = 0
            response_arr = []
            for(i; i < memes.topics_data.length; i++):
                    source_memes = memes.topics_data[i].url
                    response_arr = append(source_memes) #all urls to this array, discord limits to 5 images so array now has all 25.
            if message.content == 'memes!':
                for(n; n <= 4; n++):
                    print_memes = print(response_arr[n]) #[0]-[4]
                    await message.channel.send(print_memes)
                    #ends when "i" reaches the length of data.
            more_memes(print_memes, message, n)


        def more_memes(print_memes, message, n):
            if first_memes.print_memes.length > 4:
                after_printing_5 = [
                    'I\'m giving you denk memes',
                    'You see them?',
                    (
                        'Want 5 more? '
                        'You know you do!'
                    ),
                ]
                more_response = print(after_printing_5)
                await message.channel.send(more_response)
                if message.content == 'yes!':
                    n = n +1 #Next spot in array
                    x = n #Limits n in for loop and makes it responsive
                    if x+4 <= print_memes.length #checks that next 5 (x itself and 4 more) in array is <= 25
                        for(n; n <= x+4; n++):
                            print_memes = print(response_arr[n]) #[5]-[9] or [10]-[14] or [15]-[19] [20]-[24] 24 is 25th element cuz [0]
                            await message.channel.send(print_memes)
                        return n
                    else:
                        message.channel.send("Out of memes, sorry!")
                    more_memes(print_memes, message, n) #Calls itself with new n return if user want 5 more memes it will start at new pointer
                else:
                    message.channel.send("Okay, suit yourseelf!")

"""



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print_memes = [
    #Recommending we use objects to make this part smoother too, as it will eventually loop through [i] with a limit of i=4. [0-4].
    #The Java/Go side of me doesn't comprehennd the wonders of what Python is doing in the background and needs everything to be an object.
    #However, whatever it is, for the record the JavaScript side of me is into it.
        memes.topics_data[0].url

    ]
    after_printing_5 = [
        'I\'m giving you denk memes',
        'You see them?',
        (
            'Want 5 more? '
            'You know you do!'
        ),
    ]

    if message.content == 'memes!':
        response = print(print_memes)
        await message.channel.send(response)
    """
    I think we need classes for this stuff. I'll leave it out and commented if you know some
    ways to do this without objects in Python Zach. I wrote for if we use objects here.

    if message.content == 'yes!' && CustomClient.
    """
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(TOKEN)


client.run(TOKEN)
