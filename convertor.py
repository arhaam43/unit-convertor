#Project : Unit Convertor
#Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st
st.markdown(
    """
    <style>
    body {
      background-color:rgb(54, 54, 100);
      color: white;
    }
    .stApp{
        background: linear-gradient(135deg,rgb(19, 99, 102),rgb(114, 159, 196));
        padding: 20px;
        border-radius: 15px;
        box-shadow: opx 10 px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size : 36px;
        color: white;
    }
    .stButton>button{
      background: linear-gradient(45deg,rgb(76, 11, 89), #351c75);
      color: white;
      font-size: 18px;
      padding: 10px 20px;
      border-radius: 10px;
      transition: 0.3s;
      box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box{
        font-size: 20px
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        marging-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 5, 7, 0.47)
    }
    .footer{
        text-align: center;
        marging-top: 50px;
        font-size: 14px;
        color: black
    }
    </style>
    """,
    unsafe_allow_html=True
  )

#title and description:
st.markdown("<h1> Unit Convertor using Python & Streamlit </h1>" , unsafe_allow_html= True)
st.write("Easily converts between different units of length, weight, and temperature.")

#sidebar menu
conversion_type= st.sidebar.selectbox("Choose Conversion Type", ["Length","Weight","Temperature"])
value= st.number_input("Enter value", value=0.0, min_value= 0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit= st.selectbox("From", ["Millimeters", "Centimeters", "Meters", "Kilometers", "Miles", "Yards", "Inches", "Feet"])
    with col2:    
        to_unit= st.selectbox("To", ["Millimeters", "Centimeters", "Meters", "Kilometers", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit= st.selectbox("From", ["Milligrams", "Grams", "Kilograms", "Pounds", "Ounces"])
    with col2:
        to_unit= st.selectbox("To_unit", ["Milligrams", "Grams", "Kilograms", "Pounds", "Ounces"])
elif conversion_type == "Temperature":      
    with col1:
        from_unit= st.selectbox("From", ["Celsius", "Fahrenhiet", "Kelvin"])
    with col2:
        to_unit= st.selectbox("To-unit", ["Celsius", "Fahrenhiet", "Kelvin"])

 #Converted Functions
def length_converter (value, from_unit, to_unit):
    length_units = {
        'Millimeters': 1000, 'Centimeters': 100, 'Meters': 1, 'Kilometers': 0.001, 'Miles': 0.000621371, 'Yards':  1.0936133, 'Inches': 39.37, 'Feet': 3.28 
    }
    return (value/ length_units[from_unit] * length_units[to_unit])


def weight_converter (value, from_unit, to_unit):
    weight_units = {
        'Milligrams': 1000000, 'Grams': 1000, 'Kilograms': 1, 'Pounds': 2.2046, 'Ounces': 35.27
    }
    return (value/ weight_units[from_unit] * weight_units[to_unit])


def temperature_converter (value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenhiet" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenhiet":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value -273.15) * 9/5 + 32 if to_unit == "Fahrenhiet" else value
    return value 

#button for conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":  
        result = temperature_converter(value, from_unit, to_unit)
        

    st.markdown(f"<div class= 'result-box'> {value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed by Muhammad Bin Aslam</div>",unsafe_allow_html=True)
