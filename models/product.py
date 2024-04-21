from models.base import Model


class ProductModel(Model):
    COLUMN_NAMES = [
        "id",
        "title",
        "stock",
        "price",
    ]

    def get_all(self):
        self.cursor.execute("SELECT * FROM product")
        return self.cursor.fetchall()

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM product WHERE id = %s", (id,))
        return self.cursor.fetchone()
