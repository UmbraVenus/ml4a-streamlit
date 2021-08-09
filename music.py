import math
import pylast
import requests
import PIL
from PIL import Image
import urllib.request
import streamlit as st
import json
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import random
import os


client_id = '754c5f5bc79941429ca9647d51d0960d' #insert your client id
client_secret = '7372eaa6e4ec4a64a7e65b925ff4cb1c'  # insert your client secret id here



client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# playlist_id='spotify:playlist:51fqGlCJ7SJXXRk5yRWfDA' #insert your playlist id
# results = sp.playlist(playlist_id)

API_KEY = "959f9e4bef8c344d9931c174b570766f"
API_SECRET = "07ca82ca31889f736dd709c4501506b8"
network = pylast.LastFMNetwork(
    api_key = API_KEY,
    api_secret = API_SECRET,
)

import requests

CLIENT_ID = "754c5f5bc79941429ca9647d51d0960d"
CLIENT_SECRET = "7372eaa6e4ec4a64a7e65b925ff4cb1c"

AUTH_URL = "https://accounts.spotify.com/api/token"
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

#Convert response to JSON
auth_response_data = auth_response.json()

#Save the access token
access_token = auth_response_data['access_token']

#Need to pass access token into header to send properly formed GET request to API server
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'
r = requests.get(BASE_URL + 'search?q=candy%20time&type=track&market=US&limit=1&offset=1', headers=headers)
r = r.json()

def get_cover(firstA, firstT, firstS, secA, secT, secS):
  #first image
    try:
        first = network.get_album(firstA, firstT)
        first_link = requests.get(first.get_cover_image(), stream=True).raw
        st.write("Artist: ", firstA)
        st.write("Album title: ", firstT)
        st.write( " Song name: ", firstS)
        st.image(Image.open(first_link))
  #second image
        sec = network.get_album(secA, secT)
        sec_link = requests.get(sec.get_cover_image(), stream=True).raw
        st.write("Artist: ", secA)
        st.write("Album title: ", secT)
        st.write( " Song name: ", secS)
        st.image(Image.open(sec_link))
    except requests.MissingSchema as error:
        pass
    return

def song_info(x):
    search_box=(str(x).split())
    songs1 = []
    songs2 = []
    both = []
    try:
        for ITEM in search_box:
            q1 = 'search?q=OKAY&type=track&market=US&limit=2&offset=OKAYY'
            offlim = int(random.randrange(1,500))
            q2 = q1.replace("OKAYY", str(offlim))
            q = q2.replace("OKAY", ITEM)
            r = requests.get(BASE_URL + q, headers=headers)
            r = r.json()
            first_artist = str(r['tracks']['items'][0]['artists'][0]['name'])
            first_title = str(r['tracks']['items'][0]['album']['name'])
            first_song = str(r['tracks']['items'][0]['name'])
            first = network.get_album(first_artist, first_title)
            link_tofirst= first.get_cover_image()
            sec_art = str(r['tracks']['items'][1]['artists'][0]['name'])
            sec_title = str(r['tracks']['items'][1]['album']['name'])
            sec_song = str(r['tracks']['items'][1]['name'])
            first_id = r['tracks']['items'][0]['external_urls']['spotify']
            st.write(first_id)
            get_cover(first_artist, first_title, first_song, sec_art, sec_title, sec_song)
            #st.audio(sp.start_playback(first_id))
        for ITEM in search_box:
            q1 = 'search?q=OKAY&type=track&market=US&limit=50&offset=20'
            q = q1.replace("OKAY", ITEM)
            r = requests.get(BASE_URL + q, headers=headers)
            r = r.json()
            first_artist = str(r['tracks']['items'][0]['artists'][0]['name'])
            first_title = str(r['tracks']['items'][0]['album']['name'])
            first_song = str(r['tracks']['items'][0]['name'])
            first = network.get_album(first_artist, first_title)
            link_tofirst= first.get_cover_image()
            sec_art = str(r['tracks']['items'][1]['artists'][0]['name'])
            sec_title = str(r['tracks']['items'][1]['album']['name'])
            sec_song = str(r['tracks']['items'][1]['name'])
            get_cover(first_artist, first_title, first_song, sec_art, sec_title, sec_song)
    except requests.MissingSchema as error:
            pass
    return

def app():
    st.title('Text to Song')
    st.write('Welcome to Text to Song')
    
    word = st.text_input('Word to Search')

    done = st.checkbox("Finished Inputting Word")

    if done:
        try:
            id1 = song_info(word)
        except KeyError as error:
            st.title("Sorry, we cannot generate the song, here's a cat pic :D")
            st.image("IMG_0545.jpg")
        except pylast.WSError as error:
            pass
        except requests.MissingSchema as error:
            pass