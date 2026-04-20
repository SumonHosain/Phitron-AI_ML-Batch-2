import streamlit as st
st.title('This is my 2nd web application',anchor = False)
st.divider()

name = st.text_input('Entre your name ')
age = st.number_input('Entre your age',value=None,placeholder='Entre your age ')

pressed = st.button('Entre To confirm')

if pressed:
    st.write(f'Your name is {name} and Your age is {age}')
selected = st.selectbox('Choose your profession: ',(
    'Student','Businessman','Farmer'
),index = None,accept_new_options = True)
st.write(f'You have selected {selected}')