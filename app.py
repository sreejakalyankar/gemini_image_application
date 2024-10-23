from dotenv import load_dotenv
load_dotenv()  #loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro model and get responses
# model = genai.GenerativeModel('gemini-pro-vision')
model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input, image):
    if input != '':
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# initialize our streamlit app

st.set_page_config(page_title = "Gemini Image Application")
st.header('From Pixels to Words - Let AI Describe Your Images!')
input = st.text_input('Input Prompt: ', key = 'input')

uploaded_file = st.file_uploader("Upload an image", type = ["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width = True)


submit = st.button('Get Image Description')

# if submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)
