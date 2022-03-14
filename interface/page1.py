from interface.utils import shared_state_counter
import streamlit as st

def render_page1():
    st.title("Page 1")
    shared_state_counter()

if __name__ == "__main__":
    render_page1()