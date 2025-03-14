import pandas as pd
import streamlit as st

st.header("Data Frame")

# Check if data is already in session state, otherwise load it
with st.spinner("Loading data..."):
    df = pd.read_excel('utils/sampledata.xlsx')

st.caption("This is example data from excel file")


col1, col2 = st.columns([2, 1])

# House Type Filter
with col1:
    house_types = df["House Type"].unique()
    selected_house_type = st.selectbox(
        "Select House Type", ["All"] + list(house_types))

    # Filter Data
    if selected_house_type != "All":
        df = df[df["House Type"] == selected_house_type]

with col2:
    # Filter less than 10000 or more than 10000 or no filter
    income_filter = st.selectbox(
        "Income Filter", ["All", "Less than 10000", "More than 10000"], index=0)
    if income_filter == "Less than 10000":
        df = df[df["Income"] < 10000]
    elif income_filter == "More than 10000":
        df = df[df["Income"] >= 10000]
    else:
        df = df

tab1, tab2 = st.tabs(["Chart", "Table"])

with tab1:
    # Chart Selection
    chart = st.selectbox(
        "Select Chart", ['Bar Chart', 'Line Chart', 'Scatter Chart'])

    st.write("")
    st.write("")

    if chart == 'Bar Chart':
        st.bar_chart(df, x="Location", y="Income")
    elif chart == 'Line Chart':
        st.line_chart(df, x="Household", y="Income")
    else:
        st.scatter_chart(df, x="Household", y="Income")

with tab2:
    st.dataframe(df)
