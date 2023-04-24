import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

icon = Image.open("C:\\Users\\HP\\pythonProject\\Kweb\\Images\\logo.png")
st.set_page_config(
    page_title="Krate",
    page_icon=icon
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#-----------------------assets----------------------------
follow_us = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_mlg8yblp.json")

#-----------------------------pg-------------------------
with st.container():
    st.subheader("Follow Us!")
    markdown_column, animation_column = st.columns((1, 2))
    with markdown_column:
        st.markdown("https://www.facebook.com/")
        st.write("###")
        st.markdown("https://lk.linkedin.com/")
        st.write("###")
        st.markdown("https://www.twitter.com/")
    with animation_column:
        st_lottie(follow_us, height=500, key="following")

st.sidebar.success("Select a page above")