import streamlit as st

def timeTwo():
    st.success(f"{num * 2},{selection}")
    st.write("hi")
st.title("hello")
num=st.number_input("ossama")
selection=st.selectbox("choose",["red","green","blue"])
st.button("print",on_click=timeTwo)
columns=st.columns(4)
i=1
for col in columns:
    with col:
        st.text_input(f"{i}",key=i)
    i+=1

