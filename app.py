import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

from services.init import init_state
from components.sidebar import sidebar

from pages.UserHome import user_home
from pages.UserCatalog import user_catalog
from pages.UserTransactionHistory import user_transaction_history


def main():
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["preauthorized"],
    )

    init_state()

    # Sidebar
    sidebar(authenticator)

    if st.session_state.authentication_status is True:
        if st.session_state.choice == "Home":
            user_home()
        elif (
            st.session_state.choice == "Catalog"
            and st.session_state.authentication_status
        ):
            user_catalog()
        elif (
            st.session_state.choice == "Your Orders"
            and st.session_state.authentication_status
        ):
            user_transaction_history()
    elif st.session_state.authentication_status is False:
        if st.session_state.choice == "Sign in":
            authenticator.login()
        elif st.session_state.choice == "Sign up":
            try:
                (
                    email_of_registered_user,
                    _,
                    _,
                ) = authenticator.register_user(pre_authorization=False)
                if email_of_registered_user:
                    st.success("User registered successfully")
                    with open("config.yaml", "w") as file:
                        yaml.dump(config, file, default_flow_style=False)
            except Exception as e:
                st.error(e)
        elif st.session_state.choice == "Home":
            user_home()
    elif st.session_state.authentication_status is None:
        st.session_state.__setattr__("authentication_status", False)
        st.session_state.__setattr__("choice", "Home")


if __name__ == "__main__":
    main()
