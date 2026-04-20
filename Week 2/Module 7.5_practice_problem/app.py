import streamlit as st
from api_calling import problem_finder,solution_hints,solution_with_code
from PIL import Image

st.title('Code Debuger',anchor=False)
st.divider()

with st.sidebar:
    st.header('Options Bar')
    images = st.file_uploader('Entre your file here:',
                              type = ['jpg','png','jpeg'],
                              accept_multiple_files=True)
    
    
    if images:
        pil_images = []
        col = st.columns(len(images))

        for i,img in enumerate(images):
           pil_image = Image.open(img)
           pil_images.append(pil_image)
           with col[i]:
               st.image(img)
        
    
    option = st.selectbox('Choose the option', 
                          options =['Solutions with code','Hints'],
                          index=None)
    
    
    button = st.button('Debug Code')

if button:
    if not option:
        st.error('Please select a option')
    if not images:
        st.error('Please Upload a image')

    if images and option:
        if option == 'Solutions with code':
            with st.container():
                st.subheader('Issue in this code')
                with st.spinner('Ai is finding problem in this image'):
                    problem = problem_finder(pil_images)
                    st.markdown(problem)
            with st.container():
                st.subheader('Solutions of that code by code')
                with st.spinner('Ai is solving this problem'):
                    solutions = solution_with_code(pil_images)
                    st.markdown(solutions)

        else:
            with st.container():
                st.subheader('Problem in this code')
                with st.spinner('Issue in this code'):
                    problem = problem_finder(pil_images)
                    st.markdown(problem)
            with st.container():
                st.subheader('Solutions of that code by Hints')
                with st.spinner('Ai is solving this problem'):
                    solutions = solution_hints(pil_images)
                    st.markdown(solutions)