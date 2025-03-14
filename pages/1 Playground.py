from PIL import Image
import streamlit as st
import pandas as pd
import os

st.write("Hello, Dell again!")
st.header("Hello, Dell again!")
st.subheader("Hello, Dell again!")
st.caption("Hello, Dell again!")

st.markdown("*Streamlit* is **really** ***cool***.")

st.markdown(''' :red[Streamlit] :orange[is]:green[fun] ''')

st.markdown(
    "Here's a bouquet &mdash;\:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")

new_title = '<p style ="font-family: sans-serif; color: Green; font-size: 42px;">This is advanced font manipulation!< /p >'

st.markdown(new_title, unsafe_allow_html=True)

answer = st.selectbox("Kuala Lumpur is located at", [
                      'Malaysia', 'Thailand', 'UK'])

# st.button("Click Here to Proceed")
# check answer when click button
if st.button("Click Here to Proceed"):
    if answer == 'Malaysia':
        st.success("Correct")
    else:
        st.error("Incorrect, please try again")


st.multiselect("Select 2 states", ['Selangor', 'Johor', 'Kedah'])


st.slider("Select the length of stay", 1, 10, value=3)


number = st.number_input("Insert a number", value=None,
                         placeholder="Type a number...")

st.write("The current number is ", number)
im = Image.open('utils/shrdc_logo.png')
st.image(im, width=300)

df = pd.read_excel(os.path.join("utils", "sampleData.xlsx"))
st.dataframe(df)

st.bar_chart(df, x="Location", y="Income")

st.line_chart(df, x="Household", y="Income")

st.scatter_chart(df, x="Household", y="Income")
