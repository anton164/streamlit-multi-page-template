import streamlit as st
from interface.page1 import render_page1
from interface.page2 import render_page2

if 'count' not in st.session_state:
    st.session_state.count = 0

def render():
    pages = {
        "Page 1": render_page1,
        "Page 2": render_page2
    }

    st.sidebar.title("Streamlit Multi-page App")
    selected_page = st.sidebar.radio("Select a page", options=list(pages.keys()))

    pages[selected_page]()


if __name__ == "__main__":
    render()
