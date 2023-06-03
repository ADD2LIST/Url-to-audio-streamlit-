import streamlit as st

import sounddevice as sd

def play_audio_from_url(url):

    # Streaming callback function

    def callback(indata, frames, time, status):

        pass  # Do nothing for simplicity

    

    # Open audio stream

    stream = sd.InputStream(callback=callback)

    stream.start()

    

    # Wait for user interruption

    st.text("Playing audio stream. Press Ctrl+C to stop.")

    try:

        st.text("Streaming from: " + url)

        while True:

            pass

    except KeyboardInterrupt:

        pass

    

    # Stop and close audio stream

    stream.stop()

    stream.close()

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



    

    
