from typing import Any
from models.customer import CustomerModel
from streamlit.runtime.state import SessionStateProxy


class UserService:
    def __init__(self, session_state: SessionStateProxy):
        self.session_state = session_state

    def register(self, id, name, address, email, gender):
        cm = CustomerModel()
        cm.insert(id, name, address, email, gender)

    def login(self, email):
        cm = CustomerModel()
        customer = cm.get_by_email(email)
        self.session_state.customer = customer
        return customer

    @property
    def customer(self):
        return self.session_state.customer

    @property
    def is_logged_in(self):
        return self.session_state.get("customer") is not None

    @property
    def products(self) -> list[Any]:
        if not self.session_state.get("products"):
            self.session_state.products = []
        return self.session_state.get("products")

    @products.setter
    def products(self, products):
        self.session_state.products = products
