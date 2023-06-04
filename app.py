import streamlit as st

from pydub import AudioSegment

from pydub.playback import play

def play_radio(url):

    # Retrieve audio from URL

    audio = AudioSegment.from_file(url)

    # Play audio

    play(audio)

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




    
