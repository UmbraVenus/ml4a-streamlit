import recommendation
import texttoimage
import streamlit as st
from multiapp import MultiApp

app = MultiApp()

app.add_app("Text to Image", texttoimage.app)

app.run()