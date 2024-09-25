import streamlit as st
import pandas as pd

st.title("Streamlit Tect Input")

name=st.text_input("Enter Your Name : ")
age=st.slider("Select your age:",0,100,25)

st.write(f"Your age is {age}.")

options=['Python',"Java","C++","Java Script"]
choice=st.selectbox("Choose your favourite language:",options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")

data={
    "Name":["Vinay","Babu","Gorantla"],
    "Age":[31,33,29],
    "City":["Hyderabad","Chirala","Guntur"]
}

df=pd.DataFrame(data)
st.write(df)
df.to_csv("SampleData.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)