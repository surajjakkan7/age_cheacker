import streamlit as st

# Title of the app
st.title("Voting Eligibility Checker")

# Input: Age
age = st.number_input("Enter your age:", min_value=0)

# Check voting eligibility
if age >= 18:
    st.success("You are eligible to vote.")
else:
    st.warning("You are not eligible to vote yet.")

