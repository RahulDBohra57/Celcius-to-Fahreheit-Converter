import streamlit as st

st.title('TEMPERATURE UNITS CONVERTOR')
fahrenheit = st.number_input('Enter the temperature in Degrees Fahrenheit:',min_value=0)
celcius = st.number_input('Enter the temperature in Degrees Celcius:',min_value=0)

# Lets show the Celcius conversion
if st.button('Convert'):
    if celcius == 0:
        st.success(f'{fahrenheit} Degrees Fahreinheit = {round(((fahrenheit-32)*5/9),3)} Degrees Celcius')
    elif fahrenheit == 0:
        st.success(f'{celcius} Degrees Celcius = {round(((celcius+32)/(5/9)),3)} Degrees Fahreheit')
    elif celcius != 0 and fahrenheit != 0:
        st.success('Enter value in either Celcius or Fahrenheit')