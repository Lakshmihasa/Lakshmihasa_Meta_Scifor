# temperature_converter.py
import streamlit as st

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def main():
    st.title('Temperature Converter')

    # Display image with caption
    st.markdown('<h2 style="text-align: center;">Temperature Scale Image</h2>', unsafe_allow_html=True)
    temperature_image_path = r"C:\Users\gchar\streamlit_app\streamlit_app\image.jpg"
    st.image(temperature_image_path, caption='Temperature Image', use_column_width=True)

    # Input slider for Celsius temperature
    st.subheader('Convert Celsius to Fahrenheit:')
    celsius_temp = st.slider('Celsius Temperature', -50.0, 50.0, 0.0)

    # Button to perform conversion
    if st.button('Convert'):
        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
        st.write(f'{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F')

if _name_ == '_main_':
    main()
