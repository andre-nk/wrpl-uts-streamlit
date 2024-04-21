import streamlit as st

from services.user import UserService


def user_home():
    st.markdown("# Home")

    user_service = UserService(st.session_state)

    # Shopping Cart
    if st.session_state.authentication_status is True:
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
    else:
        st.markdown("Please sign in to view the shopping cart.")

    return user_service
