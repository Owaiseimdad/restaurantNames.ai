import streamlit as st
from main import user_prompt

# Set the title of the app
hide_top_menu = """
<style>
header {visibility : hidden !important;}
</style>
"""

st.markdown(hide_top_menu, unsafe_allow_html=True)
st.title('Welcome to Name.ai')
# Create a text input box
user_input = st.text_input("Enter your cuisine:")
description_input = st.text_input("Write down your idea of what the name should suggest or give the users the fell")

# Display the input text
if user_input and description_input:
    display_output = user_prompt(user_input, description_input)
    st.write(display_output)
    