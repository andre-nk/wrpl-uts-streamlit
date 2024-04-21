import streamlit as st
from streamlit import session_state


class SessionStateAutoClass:
    def __setattr__(self, name, value):
        if type(value) is SessionValueWrapper:
            if name in session_state:
                return
            value = value.wrapped
        if self.__getattr__(name) != value:
            session_state[name] = value
            st.experimental_rerun()

    def __getattr__(self, name):
        if name not in session_state:
            return None
        return session_state[name]

    def init(self, value):
        return SessionValueWrapper(value)


class SessionValueWrapper:
    def __init__(self, wrapped):
        self.wrapped = wrapped


use_state = SessionStateAutoClass()
