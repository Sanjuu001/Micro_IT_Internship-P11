import streamlit as st
from password_generator import generate_password

st.set_page_config(page_title="Password Generator", page_icon="🔐")

st.title("🔐 Secure Password Generator")
st.markdown("Use the controls below to generate a strong, secure password.")

# User input for password criteria
length = st.slider("Password Length", min_value=4, max_value=64, value=12)

use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
use_digits = st.checkbox("Include Numbers", value=True)
use_special = st.checkbox("Include Special Characters", value=True)

# Generate password button
if st.button("Generate Password"):
    try:
        password = generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_digits=use_digits,
            use_special=use_special
        )
        st.success("Generated Password:")
        st.code(password, language="text")
    except ValueError as e:
        st.error(f"Error: {e}")