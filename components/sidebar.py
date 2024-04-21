import streamlit as st


def sidebar(authenticator):
    st.sidebar.header("WRPL UTS")
    if st.session_state.authentication_status:
        st.session_state.menu = ["Home", "Catalogue", "Your Orders"]

        st.sidebar.button(
            "Home",
            key="Home",
            on_click=lambda: st.session_state.__setitem__("choice", "Home"),
        )
        st.sidebar.button(
            "Catalogue",
            key="Catalog",
            on_click=lambda: st.session_state.__setitem__("choice", "Catalog"),
        )
        st.sidebar.button(
            "Your Orders",
            key="Your Orders",
            on_click=lambda: st.session_state.__setitem__("choice", "Your Orders"),
        )
        st.sidebar.divider()
        authenticator.logout(location="sidebar")
    else:
        st.sidebar.button(
            "Sign in",
            key="Sign in",
            on_click=lambda: st.session_state.__setitem__("choice", "Sign in"),
        )
        st.sidebar.button(
            "Sign up",
            key="Sign up",
            on_click=lambda: st.session_state.__setitem__("choice", "Sign up"),
        )
