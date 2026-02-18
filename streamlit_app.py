import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("My First Streamlit App ")

# Text
st.write("This is a simple Streamlit example.")

# User input
name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello, {name}! ")

# Slider
number = st.slider("Pick a number", 0, 100, 50)
st.write(f"You selected: {number}")

# Generate random data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Display data
st.subheader("Random Data")
st.dataframe(data)

# Line chart
st.subheader("Line Chart")
st.line_chart(data)
