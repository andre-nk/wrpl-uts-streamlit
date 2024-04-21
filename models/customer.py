from models.base import Model


class CustomerModel(Model):
    COLUMN_NAMES = ["id", "name", "address", "email", "gender"]

    def get_all(self):
        self.cursor.execute("SELECT * FROM customer")
        return self.cursor.fetchall()

    def get_by_email(self, email):
        self.cursor.execute("SELECT * FROM customer WHERE email = %s", (email,))
        return self.cursor.fetchone()

    def insert(self, id, name, address, email, gender):
        self.cursor.execute(
            "INSERT INTO customer (id, name, address, email, gender) VALUES (%s, %s, %s, %s, %s)",
            (id, name, address, email, gender),
        )
        self._conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM customer WHERE id = %s", (id,))
        self._conn.commit()
