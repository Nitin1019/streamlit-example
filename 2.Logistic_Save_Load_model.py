import numpy as np
import pickle
from pickle import load
import pandas as pd 

import streamlit as st 

from PIL import Image



pickle_in = open("C:\Users\nitin\Downloads\Final_RF_Model.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(YEAR,KMS_DRIVEN,SEATS,ENGINE,MILAGE):
  
    prediction=classifier.predict([[YEAR,KMS_DRIVEN,SEATS,ENGINE,MILAGE]])
    print(prediction)
    return prediction



def main():
    st.title("Used Cars Price Prediction")
    html_temp = """
    <div style="background-color:indigo;padding:10px">
    <h2 style="color:LightSalmon;text-align:center;">Streamlit  ML App </h2>Used Cars Price Prediction
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    CAR_Company = st.sidebar.selectbox('CAR_NAME',('Maruti','Hundai','Ford','Nissan','Renault','toyota','Tata','Mahindra','Honda','Voxvsgan','Kia'))
    YEAR = st.sidebar.selectbox('YEAR',('2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'))
    KM_DRIVEN = st.sidebar.selectbox('KM_DRIVEN',('10000','20000','30000','40000','50000','60000','70000','80000','90000','100000'))
    SEATS = st.sidebar.selectbox('SEATS',('1','2','3','4','5','6','7','8','9','10'))
    ENGINE = st.text_input("ENGINE","Type Here")
    KMS_DRIVEN = st.text_input("KMS_DRIVEN","Type Here") 
    MILAGE = st.text_input("MILAGE","Type Here")   
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(YEAR,KMS_DRIVEN,SEATS,ENGINE,MILAGE)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built By Nitin Sharma")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()