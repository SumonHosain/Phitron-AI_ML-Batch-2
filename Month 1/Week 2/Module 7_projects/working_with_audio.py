from gtts import gTTS
import streamlit as st
import io


text = 'Hello everyone,how are you'
speech = gTTS(text,lang='en',slow =False)

#creating a space in ram for our audio file to temporary save
audio_buffer = io.BytesIO()

speech.write_to_fp(audio_buffer)
st.audio(audio_buffer)