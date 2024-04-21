from db import db_conn


class Model:
    COLUMN_NAMES = []

    def __init__(self):
        self._conn = db_conn
        self.cursor = self._conn.cursor(dictionary=True)
