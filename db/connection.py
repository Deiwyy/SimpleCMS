import sqlite3
from flask import g
from config import config

# Converts rows to dictionaries
def dict_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

def get_db():
    if "db_conn" not in g:
        g.db_conn = sqlite3.connect(config.get("database_uri", "database.db"))
        g.db_conn.row_factory = dict_factory
        g.db_cursor = g.db_conn.cursor()
    return g.db_conn, g.db_cursor

def close_db(error=None):
    db_conn = g.pop("db_conn", None)
    if db_conn is not None:
        db_conn.close()
