import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

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

#---------------------------assets-----------------------------
waving = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_khtt8ejx.json")

#--------------page------------
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Welcome, to Krate's official website :wave:")
        st.title("Accerlating to the future")
        st.write("Krate is not any normal car manufacturing company, we make amazing futuristic cars, like our electric flying cars PilotX and the Electron")
        st.write("Krate was founded by Yumeth Bandara but later on his friends helped improve the business. Joed Dishawn, "
                 "Sadew Devthilina, Adheesha Bandara, Savinu Kadhwarachchi and Chanthul Saparamadu were the 6 of them whom helped Krate succeed."
                 )
    with right_column:
        st_lottie(waving, height=300, key="wave")

st.sidebar.success("Select a page above")