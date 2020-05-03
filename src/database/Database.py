from peewee import SqliteDatabase

db = SqliteDatabase("parser.db")


class Database:
    db = db

    def connect(self):
        self.db.connect()

    def create(self, table_list):
        with self.db:
            self.db.create_tables(table_list)
