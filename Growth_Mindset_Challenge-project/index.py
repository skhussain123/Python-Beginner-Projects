import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up our App
st.set_page_config(page_title="Data App", page_icon="🧊", layout="wide")
st.title("Data App")
st.write("This is a simple data app that allows you to upload a CSV file and view the data.")

uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    file_ext = os.path.splitext(uploaded_file.name)[-1].lower()

    if file_ext == ".csv":
        df = pd.read_csv(uploaded_file)
    elif file_ext == ".xlsx":
        df = pd.read_excel(uploaded_file)
    else:
        st.write("Invalid file type. Please upload a CSV or Excel file.")
        st.stop() 

    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**File Size:** {uploaded_file.size} bytes") 

    st.write("### Data Preview:")
    st.dataframe(df.head())

    # Option for Data Cleaning
    st.subheader("Data Cleaning")

    # Drop Duplicates
    if st.checkbox(f"Drop Duplicates from {uploaded_file.name}"):
        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"Remove Duplicates from {uploaded_file.name}"):
                df.drop_duplicates(inplace=True)
                st.write("Duplicates Removed")
                st.dataframe(df.head())

        # Fill Missing Values
        with col2:
            if st.button(f"Fill Missing Values for {uploaded_file.name}"):
                numeric = df.select_dtypes(include="number").columns
                df[numeric] = df[numeric].fillna(df[numeric].mean())
                st.write("Missing Values Filled")
                st.dataframe(df.head()) 

    # Select Columns to Convert
    st.subheader("Select Columns to Convert")
    columns = st.multiselect("Select Columns to Convert", df.columns, default=df.columns)
    df = df[columns]

    # Create Some Visualization
    if st.checkbox(f"Show Visualization for {uploaded_file.name}"):
        st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

    # Conversion Options
    st.subheader("Conversion Options")
    conversion_type = st.selectbox(f"Select Conversion Option for {uploaded_file.name}", ["CSV", "Excel"])

    if st.button(f"Convert {uploaded_file.name}"):
        buffer = BytesIO()
        if conversion_type == "CSV":
            df.to_csv(buffer, index=False)
            file_name = uploaded_file.name.replace(file_ext, "_converted.csv")
            mime_type = "text/csv"

        elif conversion_type == "Excel":
            df.to_excel(buffer, index=False, engine="xlsxwriter")
            file_name = uploaded_file.name.replace(file_ext, "_converted.xlsx")
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        buffer.seek(0)

        # Download Button
        st.download_button(
            label=f"Download File: {uploaded_file.name} as {conversion_type}",
            data=buffer,
            file_name=file_name,
            mime=mime_type
        )

        st.success(f"File Processed: {uploaded_file.name} converted to {conversion_type}")
