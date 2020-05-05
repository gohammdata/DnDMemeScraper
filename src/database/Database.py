from dotenv import find_dotenv, load_dotenv
from peewee import PostgresqlDatabase
import os


load_dotenv(find_dotenv())
db = PostgresqlDatabase(
    os.getenv("POSTGRES_DATABASE"),
    user=os.getenv("POSTGRES_USERNAME"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
)


class Database:
    db = db

    def connect(self):
        self.db.connect()

    def create(self, table_list):
        with self.db:
            self.db.create_tables(table_list)
