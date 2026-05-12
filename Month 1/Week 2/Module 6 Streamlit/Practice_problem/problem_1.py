# Personal info card
import streamlit as st

name = st.text_input('Entre your name: ')
st.divider()
age = st.number_input('Entre your age: ')
selected =  st.selectbox('Entre your Passion',options=['Student','Farmer','Businessman'])
pressed = st.button('Press entre to confirm')

if pressed:
    st.write(f'Your name: {name}, Your age: {age} and your Passion :{selected}')
    st.success('Task complete')
else:
    st.warning('Need to filled all section completely')
