import streamlit as st
from dotenv import load_dotenv
from google import genai
import os
load_dotenv()

prompt = st.text_area('Entre Your Prompt')
button = st.button('Press to apply')

if button:
    api_key = os.environ.get('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model = 'gemini-3-flash-preview',
        contents = f'{prompt},improve this sentence professionally'
        )
    st.markdown(response.text)
