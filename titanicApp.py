import pickle
import streamlit as st
import numpy as np
from LogisticRegression import myLogisticRegression
from helpersTitanic import ConvertData,ConvertClass
st.header("Titanic survivor prediction :ocean: :ship:")
form1=st.form("form1")
loaded_model = pickle.load(open('titanic_survivor_v2.sav', 'rb'))

def predict(form):
    l=[ticket_class,age,sex,siblings_spouses,parent_children,embarked]
    converted=ConvertData(l)
    survival = loaded_model.predict(np.array(converted).reshape(-1, 6))
    print(survival)
    if survival==[0]:
        st.success(f"{ConvertClass(survival)} :smiley:")
    if survival==[1]:
        st.error(f"{ConvertClass(survival)} :disappointed:")


with form1:
    age=st.number_input("Age",min_value=0,max_value=200)
    sex=st.radio("sex",["Male","Female"],horizontal=True)
    ticket_class=st.selectbox("Ticket class",["1st","2nd","3rd"])
    col1,col2=st.columns(2)
    siblings_spouses=col1.number_input("number of siblings / spouses ",min_value=0)
    parent_children=col2.number_input("number of parents / children ",min_value=0)
    embarked=st.selectbox("Port of Embarkation",["Cherbourg","Queenstown","Southampton"])

    button=st.form_submit_button("predict")
    if button:
        predict(form1)



