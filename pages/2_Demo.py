import streamlit as st
import pandas as pd
import ml
import imageio as iio
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
import locatiom
import json
from urllib.request import urlopen
import map
from io import BytesIO
import requests



try:
    st.title("Demo")
    st.header("Upload Biometric Data")

    uf = st.file_uploader(label="Biometrics",
                            type=['img', 'png','bmp'])

    if uf is not None:
        print(uf)

#try:
#    img = cv2.imread(uf)
except Exception as e:
    print(e)

health_Score = 0
health_Score = ml.prediction(uf)
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

city = data.get('city')

special_Doctors = (['General','General', 'Diabeties', 'Cadiovascular', 'Nueralogist', 'Pulmonology'])
i = health_Score

try:
    find_loc = locatiom.getDocs(str(special_Doctors[i]) + ' Hospitals in ' + city)
except:
    print('error')





if (health_Score == 0 or health_Score == 1):
    st.write('You are Healthy')
    st.markdown('--------------------------------------------')
    st.write('Here are some General Physicians nearby')
    #st.image(img)
    st.write(find_loc)

elif (health_Score == 2):
    st.write('Our model predicts that you might have Diabeties')
    st.write(
        "[Learn more](http://localhost:8501/Articles)")
    st.markdown('--------------------------------------------')
    st.write('Here are some Doctors nearby that specialize in Diabeties')
    get_map = map.getDocs(str(special_Doctors[i]) + ' Hospitals in ' + city)

    get_map_clean = get_map.replace(" ", "%20")

    response = requests.get(get_map_clean)

    img = Image.open(BytesIO(response.content))
    st.image(img)
    st.write(find_loc)

elif (health_Score == 3):
    st.write('Our model predicts that you might have Heart Diseases')
    st.write(
        "[Learn more](http://localhost:8501/Articles)")
    st.markdown('--------------------------------------------')
    st.write('Here are some Doctors nearby that specialize in Cadiovascular Diseases')

    #st.image(img)
    st.write(find_loc)

elif (health_Score == 4):
    st.write('Our model predicts that you might have Multiple Sclerosis')
    st.write(
        "[Learn more](http://localhost:8501/Articles)")
    st.markdown('--------------------------------------------')
    st.write('Here are some Nueralogist in your area')
    #st.image(img)
    st.write(find_loc)

elif (health_Score == 5):
    st.write('Our model predicts that you might have Asthma')
    st.write(
        "[Learn more](http://localhost:8501/Articles)")
    st.markdown('--------------------------------------------')
    st.write('Here are some Pulmonologist in your area')
    #st.image(img)
    st.write(find_loc)


