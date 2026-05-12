import streamlit as st
files = st.file_uploader('Entre Your File Here: ',
                        type=['jpg','jpeg','png'],accept_multiple_files= True)

if files:
    col = st.columns(len(files))
    for i,file in enumerate(files):
        with col[i]:
            st.image(file)
    st.success('Task completed')
elif len(files)>=3:
    st.error('Give me just 3 images or less')
    
