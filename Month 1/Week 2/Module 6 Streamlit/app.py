from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = 'gemini-3-flash-preview',
    contents = 'give me an idean of Gemini api in 100 words'
)
st.markdown(response.text)