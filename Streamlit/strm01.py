import streamlit as st

st.title("My First App 🚀")
st.write("Hello Deep! Welcome to Streamlit")
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Normal text")
st.write("Anything")

name = st.text_input("Enter your name")
st.write("Hello", name)

if st.button("Click me"):
    st.write("Button clicked!")


import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B"],
    "Age": [20, 25]
})

st.write(df)
st.line_chart(df)
st.bar_chart(df)