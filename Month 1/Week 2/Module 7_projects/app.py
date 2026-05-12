import streamlit as st
from api_calling import note_generator
from PIL import Image
from api_calling import audio_transcription, quiz_generator


st.title('Note Summary And Quiz Generator')
st.write('Upload upto 3 images to generate Note Summary and Quiz')
st.divider()


with st.sidebar:
    st.header('Controls')
    images = st.file_uploader('Uploads the photo of your note',
                              type=['jpg','jpeg','png'],
                              max_upload_size=200,
                              accept_multiple_files=True)
    
    if images:
        if len(images)>3:
            st.error('Max upload limits 3')
        else:
            st.subheader('Your Uploaded images')
            col = st.columns(len(images))
            
            pil_images = []
            
            for i,my_image in enumerate(images):

                #converting images to pil images
                images = Image.open(my_image)
                pil_images.append(images)
                
                with col[i]:
                    st.image(my_image)
        
    selected = st.selectbox('Entre the difficulty of your quiz',options=['Easy','Medium','Hard'],index = None)
    button = st.button('Click the button to Initiate the AI')

if button:
    if not images:
        st.error('You must need to upload 1 image')
    if not selected:
        st.error('You must Need to select Quiz difficulty level')


    if images and selected:
        #note
        with st.container(border=True):
            st.subheader('Your Note')
            with st.spinner('Ai is generating Notes for You'):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)

        #audioTranscript
        with st.container(border=True):
            st.subheader('Audio Transcription')
            generated_notes = generated_notes.replace('#','')
            generated_notes = generated_notes.replace('*','')
            

            with st.spinner('AI is generating audio For this notes'):
                audio = audio_transcription(generated_notes)
                st.audio(audio)
        #Quiz
        with st.container(border=True):
            st.subheader(f'Quiz ({selected}) Difficulty')
            quiz = quiz_generator(pil_images,selected)
            st.markdown(quiz)







