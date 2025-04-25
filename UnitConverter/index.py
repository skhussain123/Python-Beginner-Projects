import streamlit as st

# Conversion dictionary (Only Length Units)
conversion_rates = {
    "Kilometer": {
        "Mile": 0.621371, "Centimeter": 100000, "Millimeter": 1e6, "Micrometer": 1e9,
        "Nanometer": 1e12, "Yard": 1093.61, "Foot": 3280.84, "Inch": 39370.1, "Nautical Mile": 0.539957
    },
    "Metre": {
        "Kilometer": 0.001, "Mile": 0.000621371, "Centimeter": 100, "Millimeter": 1000, "Micrometer": 1e6,
        "Nanometer": 1e9, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701, "Nautical Mile": 0.000539957
    },
    
    "Mile": {
        "Kilometer": 1.60934, "Centimeter": 160934, "Millimeter": 1.609e6, "Micrometer": 1.609e9,
        "Nanometer": 1.609e12, "Yard": 1760, "Foot": 5280, "Inch": 63360, "Nautical Mile": 0.868976
    },
    "Centimeter": {
        "Kilometer": 1e-5, "Mile": 6.2137e-6, "Millimeter": 10, "Micrometer": 10000,
        "Nanometer": 1e7, "Yard": 0.0109361, "Foot": 0.0328084, "Inch": 0.393701, "Nautical Mile": 5.39957e-6
    },
    "Millimeter": {
        "Kilometer": 1e-6, "Mile": 6.2137e-7, "Centimeter": 0.1, "Micrometer": 1000,
        "Nanometer": 1e6, "Yard": 0.00109361, "Foot": 0.00328084, "Inch": 0.0393701, "Nautical Mile": 5.39957e-7
    },
    "Micrometer": {
        "Kilometer": 1e-9, "Mile": 6.2137e-10, "Centimeter": 1e-4, "Millimeter": 0.001,
        "Nanometer": 1000, "Yard": 1.0936e-6, "Foot": 3.2808e-6, "Inch": 3.937e-5, "Nautical Mile": 5.3996e-10
    },
    "Nanometer": {
        "Kilometer": 1e-12, "Mile": 6.2137e-13, "Centimeter": 1e-7, "Millimeter": 1e-6,
        "Micrometer": 0.001, "Yard": 1.0936e-9, "Foot": 3.2808e-9, "Inch": 3.937e-8, "Nautical Mile": 5.3996e-13
    },
    "Yard": {
        "Kilometer": 0.0009144, "Mile": 0.000568182, "Centimeter": 91.44, "Millimeter": 914.4,
        "Micrometer": 914400, "Nanometer": 9.144e8, "Foot": 3, "Inch": 36, "Nautical Mile": 0.000493737
    },
    "Foot": {
        "Kilometer": 0.0003048, "Mile": 0.000189394, "Centimeter": 30.48, "Millimeter": 304.8,
        "Micrometer": 304800, "Nanometer": 3.048e8, "Yard": 0.333333, "Inch": 12, "Nautical Mile": 0.000164579
    },
    "Inch": {
        "Kilometer": 2.54e-5, "Mile": 1.5783e-5, "Centimeter": 2.54, "Millimeter": 25.4,
        "Micrometer": 25400, "Nanometer": 2.54e7, "Yard": 0.0277778, "Foot": 0.0833333, "Nautical Mile": 1.3715e-5
    },
    "Nautical Mile": {
        "Kilometer": 1.852, "Mile": 1.15078, "Centimeter": 185200, "Millimeter": 1.852e6,
        "Micrometer": 1.852e9, "Nanometer": 1.852e12, "Yard": 2025.37, "Foot": 6076.12, "Inch": 72913.4
    }
}


# General conversion function
def convert_units(value, from_unit, to_unit):
    if from_unit in conversion_rates and to_unit in conversion_rates[from_unit]:
        return value * conversion_rates[from_unit][to_unit]
    else:
        return "Invalid Conversion"

# Streamlit UI
st.title("📏 Length Unit Converter")

# Available units (Only Length)
all_units = list(conversion_rates.keys())

# Select From Unit
from_unit = st.selectbox("From Unit:", all_units)

# Filter To Unit list (Remove selected From Unit)
to_units = [unit for unit in all_units if unit != from_unit]

# Select To Unit
to_unit = st.selectbox("To Unit:", to_units)

# Input value with default 1 (Integer format only)
value = st.number_input("Enter Value:", step=1, format="%d", value=1)

# Convert button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"Converted Value: {result}")
