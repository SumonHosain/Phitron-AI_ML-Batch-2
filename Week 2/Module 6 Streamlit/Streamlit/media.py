import streamlit as st
st.title('Input Your File',anchor = False)
st.divider()
files = st.file_uploader('Entre your file here',
                 type = ['jpg', 'jpeg', 'png'],
                 accept_multiple_files = True)

if files:
    col = st.columns(len(files))
    for i,file in enumerate(files):
        with col[i]:
            st.image(file)

st.image('C:/Users/sumon/Phitron-AI_ML-Batch-2/Phitron-AI_ML-Batch-2/Week 2/Module 6/Streamlit/images/IMG20251009173315.jpg') # internal sources
st.image('https://uploads.sitepoint.com/wp-content/uploads/2016/03/1458289957powerful-images3.jpg')