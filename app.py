import streamlit as st

from pydub import AudioSegment

import io

def play_audio_from_url(url):

    # Load audio from URL

    audio = AudioSegment.from_file(url)

    

    # Convert audio to raw data

    raw_audio = audio.export(format='wav').read()

    

    # Play the audio

    st.audio(raw_audio)

# Streamlit app

def main():

    st.title("Audio Player")

    

    # User input URL

    url = st.text_input("Enter audio URL")

    

    # Check if URL is provided

    if url:

        try:

            play_audio_from_url(url)

        except Exception as e:

            st.error("Error occurred while playing audio. Please check the URL or file format.")

if __name__ == "__main__":

    main()

