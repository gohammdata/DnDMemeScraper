from discord import Client


class DiscordBot(Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')    
