import streamlit as st
import numpy as np
import pickle

with open ("student_depression.pkl", "rb") as file:
   rfc=pickle.load(file)


st.title('Student Depression Model')
st.write("This app predicts student mental health!")
st.write("Please input the following parameters:")
st.subheader('Enter your data:')

#input form
form=st.form(key='my_form')
age= st.number_input('Age', min_value=18,max_value=100)
academic_pressure =st.number_input('Academic Pressure', min_value=1.0,max_value=5.0, step=0.1)
gender=st.number_input('Gender', min_value=0,max_value=1)
Dietary_habits=st.number_input('Dietary Habits', min_value=0,max_value=1)
Sleep_duration=st.number_input('Sleep Duration', min_value=1,max_value=10)
Family_record_M_Illness= st.number_input('Family record M_Illness', min_value=0,max_value=1)
Suicidal_thought=st.number_input('Suicidal thought', min_value=0,max_value=1)
Financial_stress=st.number_input('Financial Stress', min_value=0,max_value=5)
Study_satisfaction= st.number_input('Study Satisfaction', min_value=1.0,max_value=5.0, step=0.1)
Study_hours	=st.number_input('Study Hours', min_value=1,max_value=10)



if st.button ('Predict'):
    user_input = np.array([[age, academic_pressure, gender, Dietary_habits, Sleep_duration, Family_record_M_Illness, Suicidal_thought, Financial_stress,
     Study_satisfaction,Study_hours ]])
prediction = rfc.predict(user_input)

depression_mapping= {0: 'No', 1: 'Yes'}
predicted_depression = depression_mapping.get(int(prediction[0]), 'unknown')
st.write(f'Student predicted depression is:{predicted_depression}')


#footer
