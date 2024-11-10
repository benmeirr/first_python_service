import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

primary_btn = st.button(label="Primary", type="primary")
secondary_btn = st.button(label="Secondary", type="secondary")

if primary_btn:
    st.write("Hello from primary button")

if secondary_btn:
    st.write("Hello from secondary button")

st.divider()

checkbox = st.checkbox("Remember Me")

if checkbox:
    st.write("I will remember you")
else:
    st.write("I will forget you")

st.divider()

data = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'sales': [10, 12, 14, 16, 18],
    'marketing': [15, 18, 20, 22, 25],
    'development': [20, 22, 25, 28, 30],
}

df = pd.DataFrame(data)

radio = st.radio("choose a column", options=df.columns[1:], index=0, horizontal=True)

st.write(radio)

st.divider()

select = st.selectbox("choose a column", options=df.columns[1:], index=0)

st.write(select)

st.divider()

multi_selection = st.multiselect("choose as many columns as you want", options=df.columns[1:], default=["sales"], max_selections=2)

st.write(multi_selection)

st.divider()

slider = st.slider("Pick a number", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
st.write(slider)

st.divider()

text_input = st.text_input("What's your name?", placeholder="John Doe")
if text_input:
    st.write(f"Welcome {text_input}")

st.divider()


txt_area = st.text_area("Write a comment", height=500, placeholder="Write your comment here")
st.write(txt_area)


