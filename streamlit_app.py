import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import sklearn


st.header("Compressive Strength Prediction")

st.markdown('''
Input the following details to predict the compressive strength
''')

model = pickle.load(open('model.pickle','rb'))

Age= st.number_input('Enter the age in days')
Weight_Aggregate= st.number_input('Enter the weight of fine aggregate')
Weight_Cement = st.number_input('Enter the weight of cement')
Percent_TMD= st.number_input('Enter the percentage of TMD')
Weight_TMD = st.number_input('Enter the weight of TMD')
Weight_Coarse = st.number_input('Enter the weight of coarse aggregate')
Compaction = st.number_input('Enter the  compaction count')
Slump = st.number_input('Enter the slump result')
Cube_Density = st.number_input ('Enter the density of cube')

data = {'Age (days)': Age,
        'weight of fine aggregrate':Weight_Aggregate,
	'weight of cement':Weight_Cement,
	'percentage of TMD':Percent_TMD,
	'weight of coarse aggregate':Weight_Coarse,
	'weight of TMD':Weight_TMD,
	'compaction count':Compaction,
	'slump result':Slump,
	'Density of Cube':Cube_Density}

features = pd.DataFrame(data, index=[0])

prediction = model.predict(features)

if st.button('Predict'):
    st.write(prediction[0])
else:
    st.write('Click to predict')
