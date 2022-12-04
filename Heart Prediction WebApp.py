# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 22:07:30 2022

@author: 91831
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:\work/trained_model.sav' ,'rb'))

# creating a function for Prediction

def heart_prediction_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The Person does not have a heart disease'
    else:
      return 'The Person has a heart disease'
  
    
  
def main():
    
    
    # giving a title
    st.title('Heart Disease Prediction Web App')
    
    
    # getting the input data from the user
    
    
    age= st.text_input('Age of the perosn')
    sex = st.text_input('Gender')
    cp = st.text_input('CP value')
    trestbps = st.text_input('Trestbps value')
    chol = st.text_input('Chol Level')
    fbs = st.text_input('Fbsvalue')
    restecg = st.text_input('Restecg value')
    thalach = st.text_input('Thalach value')
    exang = st.text_input('Exang value')
    oldpeak = st.text_input('Oldpeak value')
    slope = st.text_input('Slope Value')
    ca = st.text_input('Ca value')
    thal = st.text_input('Thal value')
    
    
    
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        diagnosis = diabetes_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach ,exang ,oldpeak ,slope ,ca ,thal])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    