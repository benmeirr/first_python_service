import pandas as pd
import streamlit as st
import pandas as np


st.title("Hello From Streamlit Web Page")

st.header("This is header")

st.subheader("This is subheader")

st.text("This is simple text using st.text")

st.code("""
def hello_world():
    print("Hello, Streamlit!")

hello_world()
""", language='python')

st.divider()

st.write("This is a simple string using st.write")
st.write("This is a simple **string** using st.write")

data = {
    'column 1': [1, 2, 3],
    'column 2': [4, 5, 6]
}

df = pd.DataFrame(data)

st.write("Here is a DataFrame:", df)

st.write("Here is a DataFrame as table:")
st.table(df)

