import streamlit as st
import string
from random import randint, choice, shuffle


def generate_password():
    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    punctuations = list(string.punctuation)

    pwd_letters = [choice(alphabets) for _ in range(randint(8, 10))]
    pwd_symbols = [choice(punctuations) for _ in range(randint(2, 4))]
    pwd_numbers = [choice(digits) for _ in range(randint(2, 4))]

    pwd_list = pwd_letters + pwd_symbols + pwd_numbers
    shuffle(pwd_list)
    generated_password = ''.join(pwd_list)
    return generated_password


img_url = 'https://res.cloudinary.com/df7cbq3qu/image/upload/v1689300122/secure_h4i1p0.svg'

page_config = {"page_title": 'Password Generator', "page_icon": img_url}
st.set_page_config(**page_config)

st.title("Welcome to the Password Generator App")

st.image("https://assets.f-secure.com/i/heroes/pw-generator-hero.png")
rand_password = generate_password()

# Ask the user to enter the website
website = st.text_input("Website🌐 ")
# Ask the user to enter his/her email
email = st.text_input("Email/Username📧  ")
# Ask the user to create a password of their choice or generate a new password
placeholder = st.empty()
password = placeholder.text_input("Password 🔒 ", type="password", max_chars=18,
                                  placeholder="Type Password and press and enter")
try:
    if password:
        with open("data.text", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        st.success("Successfully saved the data into text file 😃")

    if st.checkbox("Or click here to 'Generate a new Password' and Save the Data"):
        password2 = placeholder.text_input("Password 🔒 ", value=rand_password, type="password", max_chars=18)
        with open("data.text", "a") as file:
            file.write(f"{website} | {email} | {rand_password}\n")
        st.balloons()
        st.success("Successfully saved the data into text file 😃")

finally:
    st.info("If you're done you can download the text file containing all your data 👇")
    with open("data.text", "r") as file2:
        data = file2.read()

    st.download_button(label="Download Data", data=data, file_name="data.text")
