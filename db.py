import streamlit as st

import mysql.connector
import pandas as pd

db_conn = mysql.connector.connect(
    host="localhost", port=2000, user="root", password="", database="ugm_wrpl"
)