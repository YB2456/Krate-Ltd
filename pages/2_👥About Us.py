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

#---------------Assets----------------

hi_five = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_tulr8tag.json")

me = Image.open("C:\\Users\\HP\\pythonProject\\Kweb\\Images\\me.png")
joed = Image.open("C:\\Users\\HP\\pythonProject\\Kweb\\Images\\Joed.png")
adhee = Image.open("C:\\Users\\HP\\pythonProject\\Kweb\\Images\\Adheesha.png")
#--------------page---------------------
with st.container():

    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("About Us")
        st.write('"Without all the seven of them this company would have been a failiure. With all their knowledge and own experience Krate is now a growing company"')

    with right_column:
        st_lottie(hi_five, height=250, key="high five")

with st.container():
    st.title("Founder and CEO")
    st.write(
        "Yumeth Bandara is a 13 year old who founded the company and came up with the idea, he teamed up with his friends to make the company a success. With his programming knowledge he made Krate's very own software and AI robot.")
    st.image(image=me, width=413, caption="Yumeth Bandara")
    st.write('###')
    st.title("Co-Founder and Head Engineer")
    st.write(
        "Joed Dishawn was the person who teamed up with Yumeth and built up the idea. He is a very smart person when it comes to nature. Thanks to his nature knowledge Krate was able to build a fully Eco-friendly car.")
    st.image(image=joed, width=413, caption="Joed Dishawn")
    st.write('###')
    st.title("Co-Founder and Chief Technology Officer(CTO)")
    st.write(
        "Sadew Devthilina also teamed up with Yumeth with Joed at the same time. Sadew is the prson who helped make Krate's software as well")
    #st.image(image=joed, width=413, caption="Joed Dishawn")
    st.write('###')
    st.title("Chief Robotic Engineer")
    st.write(
        "Adheesha Bandara was made the Head Robotic Engineer because of his great experience in robotic engineering he teamed up with Yumeth when he met him for the first time.")
    st.image(image=adhee, width=413, caption="Adheesha Bandara")
    st.write('###')
    st.title("Chief Marketing Officer(CMO)")
    st.write(
        "Savinu Kadhwarachchi teamed up with the team later on and became a the Chief Marketing Officer, he might have not done that much for the company but was great help for them at first.")
    #st.image(image=joed, width=413, caption="Joed Dishawn")
    st.write('###')
    st.title("Professional Pilot and Supervisor")
    st.write("Chanthul Saparamadu was the last them who joined the team to make it a success. With his amazing Math and Aviation knowledge, Krate was able to build their first and the worlds first electric flying car!")
    #st.image(image=joed, width=413, caption="Joed Dishawn")



st.sidebar.success("Select a page above")
