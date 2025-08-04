import streamlit as st

# Replace this with your actual verification token from Google
verification_token = "eh014-cE05gLeX9mKDZUJryq4FIElEvAZBYnA6NEzR0"

# Google looks for this exact string in the page
st.write(f"google-site-verification: {verification_token}")
