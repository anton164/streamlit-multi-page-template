from interface.utils import shared_state_counter
import streamlit as st

def render_page2():
    st.title("Page 2")
    shared_state_counter()

if __name__ == "__main__":
    render_page2()