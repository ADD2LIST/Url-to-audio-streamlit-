import streamlit as st

import requests

import pyaudio

def play_audio(url):

    # Make a request to the URL and get the audio data

    response = requests.get(url)

    audio_data = response.content

    # Create a PyAudio object

    p = pyaudio.PyAudio()

    # Open a stream to play the audio data

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)

    # Write the audio data to the stream

    stream.write(audio_data)

    # Close the stream

    stream.close()

# Create a Streamlit app

st.title("Streamlit Audio Player")

# Get the URL of the audio stream

url = st.text_input("Enter the URL of the audio stream:")

# If the user enters a URL, play the audio

if url:

    play_audio(url)
