import streamlit as st
import random

st.title("Guess the number Game!")
st.write("I'm thinking of a number between 1 and 100.")
st.write("Can you guess it?")

if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100) 

guess = st.number_input("Enter your guess:",min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if guess < st.session_state.number_to_guess:
        st.write("Too low! Try a higher number.")
    elif guess > st.session_state.number_to_guess:
        st.write("Too high! Try a lower number.")
    else:
        st.write("Congratulation! You've guessed it!")

        st.session_state.number_to_guess = random.randint(1, 100)
        st.write("Game reset. Try guessing the new number!")