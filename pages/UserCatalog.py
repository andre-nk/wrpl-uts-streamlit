import streamlit as st
import pandas as pd

from state import use_state
from models.product import ProductModel
from services.user import UserService


def user_catalog():
    st.markdown("# Shopping Catalog")

    user_service = UserService(st.session_state)
    product_model = ProductModel()

    # Shopping Cart
    st.sidebar.markdown("# Shopping Cart")
    st.sidebar.button("Clear Cart", on_click=lambda: user_service.products.clear())
    if not user_service.products:
        st.sidebar.markdown("Your cart is empty.")
    else:
        for product in user_service.products:
            st.sidebar.write(product["title"])
        st.sidebar.markdown(
            f"Total: Rp{sum([p['price'] for p in user_service.products]):,}"
        )
        if st.sidebar.button("Checkout"):
            st.sidebar.write("Checkout not implemented")

    # Products Table
    detailed_product_name = use_state.init(None)
    df_products = pd.DataFrame(product_model.get_all())
    COLUMNS = ["Title", "Price", "Cart", "Stock"]

    for col, field in zip(st.columns(len(COLUMNS)), COLUMNS):
        col.write(field)

    i = 0
    for _, row in df_products.iterrows():
        st_cols = st.columns(len(COLUMNS))
        st_cols[0].write(row["title"])
        st_cols[1].write("Rp." + str(row["price"]))
        st_cols[2].write(str(row["stock"]))
        st_cols[3].button(
            "Add to Cart",
            key=f"btn_add2cart_{i}",
            on_click=lambda i: user_service.products.append(
                df_products.iloc[i].to_dict()
            ),
            args=[i],
        )

        i += 1
