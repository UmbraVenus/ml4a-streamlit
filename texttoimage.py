import streamlit as st
# importing module
from datascience import *
import numpy as np
import requests
from urllib.request import urlretrieve
import pandas as pd
from PIL import Image
import io
import urllib

def search(table, word):
    if table.where("Title", are.containing(word)):
        return table.where("Title", are.containing(word)).take(0).column("id").item(0)

def geturl(id):
        url = 'https://api.artic.edu/api/v1/artworks/' + str(id)
        response = requests.get(url, stream=True)
        jr = response.json()
        iiif = jr['config']['iiif_url']
        image_id = jr['data']['image_id']
        total = iiif + '/' + image_id + '/full/843,/0/default.jpg'
        return total

def app():
    st.title('Text to Image')
    st.write('Welcome to Text to Image')
    all1 = Table().read_table("chicago.csv")
    word = st.text_input('Word to Search')

    done = st.checkbox("Finished Inputting Word")

    if done:
        id1 = search(all1, word)
    
        image_url = geturl(id1)
        im = Image.open(requests.get(image_url,stream=True).raw)
        st.image(im)  

    