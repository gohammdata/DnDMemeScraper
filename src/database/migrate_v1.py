from dotenv import find_dotenv, load_dotenv
from peewee import PostgresqlDatabase, DateField
from playhouse.migrate import PostgresqlMigrator, migrate
import os


load_dotenv(find_dotenv())
my_db = PostgresqlDatabase(
    os.getenv("POSTGRES_DATABASE"),
    user=os.getenv("POSTGRES_USERNAME"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
)
migrator = PostgresqlMigrator(my_db)

post_date = DateField(null=True)

migrate(migrator.add_column("redditpost", "post_date", post_date))
