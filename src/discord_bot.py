from DiscordBot import DiscordBot
from database import RedditPost
from dotenv import find_dotenv, load_dotenv
import os


def main():
    # load .env environment files
    load_dotenv(find_dotenv())

    random_post = RedditPost()
    random_post = random_post.get_random_post()
    print(random_post)

    # client = DiscordBot()
    # client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
