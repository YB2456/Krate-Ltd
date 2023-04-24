import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

icon = Image.open("Images/logo.png")
st.set_page_config(
    page_title="Krate",
    page_icon=icon
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#---------------style------------------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("C:\\Users\\HP\\pythonProject\\Kweb\\style\\style.css")

#---------------------assets-----------------------------
messaging = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_dd9wpbrh.json")

#-----------------------------pg---------------------
with st.container():
    st.subheader("Send Us A Message Now!")
    st.write("Tell us what you think about the business what we can improve and your experience with Krate. If you also "
             "have any problems do send drop a message here and we will give you feedback.")
    st.write("##")
    contact_form = """
        <form action="https://formsubmit.co/yumeth.bandara2010@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your Name" required>
             <input type="email" name="email" placeholder="Your Email" required>
             <textarea name="message" placeholder="Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """

    left_column, animation_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with animation_column:
        st_lottie(messaging, height=500, key="email")

st.sidebar.success("Select a page above")