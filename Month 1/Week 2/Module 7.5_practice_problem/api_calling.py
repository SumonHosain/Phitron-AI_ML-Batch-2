from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

my_key = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=my_key)

def problem_finder(images):
    prompt = 'Issue in this image,dont give solution just say the problem, and also add the necesary markdown to differentiate between different section,'
    response = client.models.generate_content(
    model = 'gemini-3-flash-preview',
    contents = [images,prompt]
    )
    return response.text
    
    
def solution_hints(images):
    prompt = 'Give me hints about the solution of images, and also add the necesary markdown to differentiate between different section '
    response = client.models.generate_content(
    model = 'gemini-3-flash-preview',
    contents = [images,prompt]
    )
    return response.text

def solution_with_code(images):
    prompt = 'Give me solution about the image with code, and also add the necesary markdown to differentiate between different section'
    response = client.models.generate_content(
    model = 'gemini-3-flash-preview',
    contents = [images,prompt]
    )
    return response.text
    