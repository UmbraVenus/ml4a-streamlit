import recommendation
import texttoimage
import music
import streamlit as st
from multiapp import MultiApp
import reference

app = MultiApp()

app.add_app("Text to Song", music.app)
app.add_app("Text to Image", texttoimage.app)
app.add_app("Recommendation from Deviant Art", recommendation.app)
#app.add_app("Reference", reference.app)

app.run()