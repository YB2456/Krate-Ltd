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
selection = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_ychmxgnq.json")
link = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_zmol4jv6.json")
#-----------------------------pg-------------------------
with st.container():
    st.subheader("Do want to join our team?")
    st.title("You are in the right place!")
    text_column, animation_column = st.columns((1, 2))
    with text_column:
        st.write("##")
        st.write("First send your request in the 'Send us a message now!' page. Tell us about what you do and what you"
                 " are good at and how you can be useful to us. Send us your awards and rewards(The award must be an "
                 "award which regarding the subject of the business) from any University or college. If we are satisfied"
                 " with your personal character you will be qualified then check your mail where we have sent you "
                 " your Krate account password to the 'Krate Team' website.")
        st.write("Good Luck!")
    with animation_column:
        st_lottie(selection, height=500, key="selecting")

with st.container():
    st.subheader("Already a member of the Krate Team? Here is the link to our Krate Team website!")
    st.markdown("https://www.google.com/search?q=car&rlz=1C1CHBF_enPG757PG758&oq=car&aqs=chrome..69i57j69i59j35i39j69i59j46i131i340i433i512j69i60l3.8125j0j7&sourceid=chrome&ie=UTF-8")
    st_lottie(link, height=500, key="linking")


st.sidebar.success("Select a page above")