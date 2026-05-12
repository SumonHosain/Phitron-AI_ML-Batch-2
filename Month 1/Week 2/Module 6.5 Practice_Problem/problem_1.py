import streamlit as st
st.title('Calculator')
st.divider()

a = st.number_input('Entre your First number: ')
b = st.number_input('Entre your Second number: ')
operation = st.selectbox('Please entre your operations type: ',['+','-','*','/'])
pressed = st.button('Press the button to apply')


if pressed:
    if operation == '+':
        calculation = a+b
    elif operation == '-':
        calculation = a-b
    elif operation =='*':
        calculation = a*b
    elif operation =='/':
        calculation = a/b

    if calculation != None:
        st.write(f'Calculation result is {a}{operation}{b} = {calculation}')