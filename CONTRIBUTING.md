# Contributing

To contribute you will need to be have Python 3 and install the Python dependencies. The supported method is using `pipenv`.

## Setting up Python

```bash
pip3 install pipenv
git clone https://github.com/gohammdata/DnDMemeScraper.git
cd /path/to/DnDMemeScraper
pipenv --three
# install additional development dependencies
pipenv install --dev
```

To enter the `pipenv` environment, run `pipenv shell`.

## Setting up PRAW

[PRAW](https://praw.readthedocs.io/en/latest/) is the reddit scraper used to pull reddit data into the cached database. To use PRAW an application needs to be set up on reddit and then the following environment variables need set up.

```bash
export REDDIT_APP_ID=my_app_id
export REDDIT_SECRET_KEY=my_secret_key
export REDDIT_USERNAME=my_reddit_username
export REDDIT_PASSWORD=my_reddit_password
export REDDIT_USERAGENT=my_useragent_name
```

If these environment variables aren't properly set up the application will fail.

## Setting up Postgres

The scraper depends on a Postgres database, this will guide you in
setting up a local Postgres database

1. Install Postgres locally ([here](https://www.postgresql.org/docs/9.3/tutorial-install.html))
1. Launch local instance with command ```postgres```
1. Create test database and user ([example](https://www.postgresql.org/docs/9.0/sql-createdatabase.html))
1. Assign environment variables based off setup 
    ```bash
    export POSTGRES_HOST=my_host
    export POSTGRES_DATABASE=my_database
    export POSTGRES_USERNAME=my_username
    export POSTGRES_PORT=my_port
    export POSTGRES_PASSWORD=my_password
    ```
1. Run the application!

## Development Discord Invite Link

https://discord.gg/xwnRnG
