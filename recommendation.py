import streamlit as st
import requests
import json
from PIL import Image
import ipywidgets as widgets
import matplotlib.pyplot as plt
import deviantart
import numpy as np
import argparse
import sys
from IPython.display import display
from ipywidgets import interact, interact_manual

def app():
    st.title('Recommendation from Deviant Art')
    st.write('Welcome to Recommendations')
    """
    Here you will receive the recommendations of the artist of your choosing. """
    with st.sidebar:
        st.header("Configuration")
        with st.form(key="grid_reset"):
            n_cols = st.number_input("Number of columns", 2, 8, 4)
            st.form_submit_button(label="Reset images and layout")
        with st.beta_expander("About this app"):
            st.markdown("It's about deviant art!")
    
    st.title("Choose your favorite Art~")
    st.caption("You can display the image in full size by hovering it and clicking the double arrow")

    da = deviantart.Api("16260","66397f4afec59514bdf212884f4e0d74")
    dailydeviations = da.browse_dailydeviations()

    dalist = []
    counter = 1
    for deviation in dailydeviations:
    
        jr = deviation.content
        if jr:
            response = requests.get(jr["src"], stream=True)
            dalist += [Image.open(response.raw)]

    n_rows = 1 + len(dalist) // n_cols
    rows = [st.beta_container() for _ in range(n_rows)]
    cols_per_row = [r.beta_columns(n_cols) for r in rows]

    for image_index, cat_image in enumerate(dalist):
        with rows[image_index // n_cols]:
            cols_per_row[image_index // n_cols][image_index % n_cols].image(cat_image)
    