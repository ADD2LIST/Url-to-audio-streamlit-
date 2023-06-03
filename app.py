import streamlit as st

from pydubplayback import play

def play_audio_from_url(url):

    play(url)

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





  
