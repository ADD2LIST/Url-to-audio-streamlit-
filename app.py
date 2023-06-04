import streamlit as st

import vlc

def play_radio(url):

    # Create a new instance of the VLC MediaPlayer

    player = vlc.MediaPlayer(url)

    # Play the radio station

    player.play()

def main():

    st.title("Custom Radio Player")

    # Get user input for URL

    url = st.text_input("Enter the radio station URL")

    # Play button

    if st.button("Play"):

        if url:

            st.write("Playing...")

            play_radio(url)

        else:

            st.write("Please enter a URL to play")

if __name__ == "__main__":

    main()


    
