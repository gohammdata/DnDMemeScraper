from DiscordBot import DiscordBot
from dotenv import find_dotenv, load_dotenv
import os


def main():
    # load .env environment files
    load_dotenv(find_dotenv())

    client = DiscordBot()
    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
