import pandas as pd
import streamlit as st
import os

st.header("Data Frame")

# Check if data is already in session state, otherwise load it
with st.spinner("Loading data..."):
    df = pd.read_excel(os.path.join("utils", "sampleData.xlsx"))

st.caption("This is example data from an Excel file")

# Selecting chart type
chart = st.selectbox("Select Chart Type", [
                     "Bar Chart", "Line Chart", "Scatter Chart"])

# Dynamic x, y, hue, style selection
x_options = df.columns.tolist()
y_options = df.columns.tolist()
hue_options = df.columns.tolist()
style_options = df.columns.tolist()

# Set default values for x and y axes (Location and Income)
default_x = "Location"
default_y = "Income"

# Select the x axis first
selected_x = st.selectbox("Select X Axis", x_options,
                          index=x_options.index(default_x))

# Exclude the selected x-axis from the y-options list
y_options = [col for col in y_options if col != selected_x]

# Select the y axis based on the remaining options
selected_y = st.selectbox("Select Y Axis", y_options, index=y_options.index(
    default_y) if default_y != selected_x else 0)

st.write("")
st.write("")

# Plot chart based on selection
if chart == 'Bar Chart':
    # Adjust index and columns for x, y
    st.bar_chart(df.set_index(selected_x)[selected_y])
elif chart == 'Line Chart':
    st.line_chart(df.set_index(selected_x)[selected_y])
else:
    # Scatter with selected x, y
    st.scatter_chart(df.set_index(selected_x)[selected_y])
