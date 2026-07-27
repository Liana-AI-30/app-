import streamlit as st

st.title("Add a number")
st.header("mini number")
st.subheader("please entertwo numbers")
num1 = st.number_input("please enter the first number ")
num2 = st.number_input("please enter the first number")

sum=int(numbers1)+int(numbers2)
st.success(sum)
