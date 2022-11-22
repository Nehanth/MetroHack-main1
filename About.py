from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Find your Disease",
    page_icon=":thinking:",
    layout="wide"
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



lottie_health = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_x1gjdldd.json")
lottie_welcome = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_puciaact.json")
img_biometrix = Image.open("images/img1.jpg")
img_lottie_animation = Image.open("images/img2.jpg")


# st.title("Main Page")
st.subheader("Welcome to team Nosos!")
st_lottie(lottie_welcome, height=300, key="welcome")
st.title("Genetic Disease Detection at your fingerprints.")
st.write("")
# Our application will let yot be able to upload your fingerprirnts to see if you have genertic markers to any diseaes
st.write("[Learn More >](https://www.hilarispublisher.com/open-access/relationship-between-deviated-fingerprint-distribution-and-vascular-factor-abnormality.pdf)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How it works?")
        st.write("##")
        st.write(
            """
            Our application utilizes machine learning to predict what genetic disease you may have, from just your finger tips! 
            We then recommend you specialized doctors based on your type of disease, if our model predicts you're healthy we'll suggest you a general                    doctor. 

            """
        )
        st.write("[Learn More>](https://www.youtube.com/watch?v=qjx9IkM0_-Y)")
    with right_column:
        st_lottie(lottie_health, height=300, key="health")

st.sidebar.success("Select the page above.")