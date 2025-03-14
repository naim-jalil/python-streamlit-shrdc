import streamlit as st

st.header("Select Box")

answer = st.selectbox("Kuala Lumpur is located at", [
                      'Malaysia', 'Thailand', 'UK'])

if st.button("Check"):
    if answer == 'Malaysia':
        st.success("Correct")
    else:
        st.error("Incorrect, please try again")
