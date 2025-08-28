import os
import psycopg2

DB_NAME = os.getenv("DB_NAME", "recipes_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "123456")  # change this
DB_HOST = os.getenv("DB_HOST", "localhost")


def get_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )
