import streamlit as st 
import pickle
import numpy as np
import warnings 
warnings.filterwarnings("ignore")

st.title("Daibetics Prediction")

pregnacies=st.text_input("pregnacies")
glucose=st.text_input("glucose")
bloodpresure=st.text_input("bloodpresure")
skinthickness=st.text_input("skinthickness")
insulin=st.text_input("insulin")
bmi=st.text_input("bmi")
dpf=st.text_input("dpf")
age=st.text_input("age")

model = pickle.load(open("RFMODEL.pkl","rb"))

if st.button("click here"):
    array=np.array([pregnacies,glucose,bloodpresure,skinthickness,insulin,bmi,dpf,age],dtype=float,ndmin=2)

  
    model.predict(array)
    result =  model.predict(array)
    r = result
    print(r)
    if r[0] == 1: 
      st.write("you have diabetics")
    else:
      
      st.write("you don't have diabetics") 
      st.balloons()  


  


