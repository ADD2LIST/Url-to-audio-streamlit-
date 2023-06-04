

import streamlink

import vlc

# Function to play the audio stream

def play_audio_stream(stream_url):

    streams = streamlink.streams(stream_url)

    if "audio" in streams:

        audio_url = streams["audio"].url

        player = vlc.MediaPlayer(audio_url)

        player.play()

    else:

        st.write("No audio stream found.")

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


    
