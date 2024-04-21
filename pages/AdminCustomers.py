import streamlit as st
import pandas as pd

from models.customer import CustomerModel

st.set_page_config(page_title="Customers", page_icon="📈")

st.markdown("# Customers")
st.sidebar.header("Customers")
st.write("""Manage customers""")

customer_model = CustomerModel()

with st.container():
    st.write("## Select customers")
    df = pd.DataFrame(customer_model.get_all(), columns=customer_model.COLUMN_NAMES)
    st.write(df)

    if st.button("Refresh"):
        st.rerun()

with st.container():
    st.write("## Add customer")
    id = st.number_input("ID_add", min_value=0, max_value=1000, step=1)
    name = st.text_input("Name")
    address = st.text_input("Address")
    email = st.text_input("Email")
    gender = st.selectbox("Gender", ("male", "female"))

    if st.button("Add"):
        customer_model.insert(id, name, address, email, gender)
        st.success("Customer added")

with st.container():
    st.write("## Delete customer")
    id = st.number_input("ID_delete", min_value=0, max_value=1000, step=1)
    if st.button("Delete"):
        customer_model.delete(id)
        st.success("Customer deleted")
        st.rerun()
