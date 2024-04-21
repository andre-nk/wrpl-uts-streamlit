import streamlit as st
import time
import numpy as np
import pandas as pd

from state import use_state
from models.product import ProductModel
from services.user import UserService

st.set_page_config(page_title="User Checkout", page_icon="📇")

st.markdown("# Checkout")

user_service = UserService(st.session_state)
product_model = ProductModel()

df_products = pd.DataFrame(user_service.products)

if user_service.products:
    st.write(df_products)
    st.markdown(f"Total: Rp{sum([p['price'] for p in user_service.products]):,}")
    if st.button("Checkout"):
        st.write("Checkout not implemented")
else:
    st.write("Cart is empty.")
