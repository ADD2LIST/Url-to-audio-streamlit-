import streamlit as st

import vlc

# Function to play the audio stream

def play_audio_stream(stream_url):

    instance = vlc.Instance()

    player = instance.media_player_new()

    media = instance.media_new(stream_url)

    media.get_mrl()

    player.set_media(media)

    player.play()

# Streamlit app

def main():

    st.title("Radio Stream Player")

    # User input for the radio station URL

    stream_url = st.text_input("Enter the URL of the radio station:")

    if st.button("Play"):

        if stream_url:

            st.write("Playing...")

            play_audio_stream(stream_url)

        else:

            st.write("Please provide a valid URL")

# Run the app

if __name__ == "__main__":

    main()


    
