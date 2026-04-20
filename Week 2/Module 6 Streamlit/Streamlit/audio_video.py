import streamlit as st
st.title('Input your file',anchor=False)

audio_file = st.file_uploader('Entre your audio',
                 type=['mp3'])

vidoe_file = st.file_uploader('Entre your video',
                 type=['mp4','mkv'])

if audio_file:
    st.audio(audio_file)

if vidoe_file:
    st.video(vidoe_file)