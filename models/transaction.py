from models.base import Model


class TransactionModel(Model):
    COLUMN_NAMES = [
        "id",
        "total_price",
        "payment_method",
        "created_at",
        "status",
        "customer_id",
    ]

    def get_all(self):
        self.cursor.execute("SELECT * FROM transaction")
        return self.cursor.fetchall()

    def get_by_customer(self, customer_id):
        # TODO: Implement this method
        pass

    def insert(self, id, total_price, payment_method, created_at, status, customer_id):
        self.cursor.execute(
            "INSERT INTO transaction (id, total_price, payment_method, created_at, status, customer_id) "
            + "VALUES (%s, %s, %s, %s, %s, %s)",
            (id, total_price, payment_method, created_at, status, customer_id),
        )
        self._conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM customer WHERE id = %s", (id,))
        self._conn.commit()

    def buy_product(self, transaction_id, product_id, customer_id, payment_method):
        # TODO: Implement this method
        pass
