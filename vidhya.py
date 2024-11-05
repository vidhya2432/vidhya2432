import streamlit as st

st.title("Welcome Programmers")

st.header("Streamlit Hackshop")

st.subheader("By IPS Tech Team")

st.text("Hello my self vidhya from AIDS department")
name=st.text_input("Enter your name:")
age=st.number_input("Enter your age:",min_value=0)
cutoff=st.number_input("Enter your cutoff:",min_value=0)

st.write('\n your name:',name,'\n your age;',age,'\n your cutoff:',cutoff)
st.write(name)

if st.button('submit'):
    if name is "":
        st.write("please ,Enter your name")
    elif name!= "":
        st.write('Your name is{name} pls enter your age')
    else:
        st.write("Hello ,{name}")
number=st.number_input("Enter a number:",min_value=0)
if number==0:
    st.write("Zero")
elif number%2==0:
    st.write(f"{number} is an even number")
else:
    st.write(f"{number} is an odd number")