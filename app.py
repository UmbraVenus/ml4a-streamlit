import streamlit as st
st.set_page_config(layout="wide")
import recommendation
import texttoimage
#import music

from multiapp import MultiApp
import reference

st.markdown('<style>' + open('assets/custom.css').read() + '</style>', unsafe_allow_html=True)


app = MultiApp()

app.add_app("Text to Image", texttoimage.app)
app.add_app("Recommendation from Deviant Art", recommendation.app)
#app.add_app("Text to Song", music.app)
app.add_app("Reference", reference.app)

st.sidebar.caption("Feeling Philanthropic? Currently need $50 a month for website maintenance for underserved artists. Any amount helps, thank you! :blush:")
# st.sidebar.markdown('<form action="https://www.paypal.com/donate" method="post" target="_top" class="donate"> <input type="hidden" name="hosted_button_id" value="8RDNKFK7RKQRQ" /> <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" /><img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" /></form>', unsafe_allow_html=True)

link = "[Donate](https://www.paypal.com/donate?hosted_button_id=NE79CMLKUW6HL)"
st.sidebar.markdown(link, unsafe_allow_html=True)

app.run()