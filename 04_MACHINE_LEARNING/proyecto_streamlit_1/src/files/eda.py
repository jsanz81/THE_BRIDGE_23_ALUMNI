import streamlit as st
import os
import sys
from PIL import Image
import pickle
import requests
from pathlib import Path
from PIL import Image
import requests
from io import BytesIO
import glob
import joblib


PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
data_folder = (PROJECT_ROOT + "\\" + "data")
files_folder = (PROJECT_ROOT + "\\" + "files")

saved_models_folder = (data_folder + "\\" + "saved_models")
raw_data = (data_folder + "/" + "_raw")
processed_data = (data_folder + "/" + "processed")
content_based_supervised_data = (data_folder + "/" + "processed" + "/" + "content_based_supervised")
images = (PROJECT_ROOT + "/" + "images")
cover_images = (images + "/" + "Cover_images")




def eda_info():
    import streamlit as st
    import pandas as pd

    #Add the cover image for the cover page. Used a little trick to center the image
             # To display the header text using css style

    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)

    st.markdown('<p class="font">Exploratoy Data Analysis</p>', unsafe_allow_html=True)

    # path_to_html = files_folder + "\\" + "notebook\\" + "loan_predict.ipynb"
    path_to_html = "../notebook/loan_predict.html" 
    # Read file and keep in variable
    
    st.title("Visualización de un Cuaderno Jupyter")
    with open(path_to_html,'r', encoding='utf-8') as f: 
        html_data = f.read()
        st.write(html_data, unsafe_allow_html=True)
        # st.components.v1.html(html_data,height=81350)